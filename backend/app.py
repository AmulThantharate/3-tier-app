import os
import time
from threading import Lock
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError


db = SQLAlchemy()
_db_init_lock = Lock()
_db_initialized = False


class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://notes:notes@localhost:3306/notes",
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}

    db.init_app(app)

    def ensure_database_ready(retries=5, delay_seconds=2):
        global _db_initialized

        if _db_initialized:
            return True

        with _db_init_lock:
            if _db_initialized:
                return True

            with app.app_context():
                for attempt in range(1, retries + 1):
                    try:
                        db.create_all()
                        _db_initialized = True
                        return True
                    except OperationalError as exc:
                        db.session.rollback()
                        app.logger.warning(
                            "Database unavailable during startup attempt %s/%s: %s",
                            attempt,
                            retries,
                            exc,
                        )
                        if attempt < retries:
                            time.sleep(delay_seconds)

        return False

    @app.before_request
    def _prepare_database():
        if request.endpoint == "health":
            return None

        if not ensure_database_ready():
            return {"error": "Database unavailable"}, 503

        return None

    ensure_database_ready()

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.get("/")
    def index():
        notes = Note.query.order_by(Note.created_at.desc()).all()
        return render_template("index.html", notes=notes)

    @app.post("/notes")
    def create_note():
        title = request.form.get("title", "").strip()
        body = request.form.get("body", "").strip()

        if not title or not body:
            flash("Title and body are required.")
            return redirect(url_for("index"))

        note = Note(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        flash("Note saved.")
        return redirect(url_for("index"))

    return app


app = create_app()
