# 🚀 3-Tier Flask Application

> A production-ready **three-tier web application** deployed via Infrastructure-as-Code, featuring Flask, Nginx, and MySQL — all orchestrated with Terraform, Ansible, and Packer.

![Architecture](https://img.shields.io/badge/Architecture-3--Tier-blue?style=for-the-badge)
![Terraform](https://img.shields.io/badge/Terraform-1.0+-623CE4?style=for-the-badge&logo=terraform&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-2.14+-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Packer](https://img.shields.io/badge/Packer-1.9+-3473AE?style=for-the-badge&logo=packer&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-1.24+-009639?style=for-the-badge&logo=nginx&logoColor=white)

---

## 📖 Overview

This project demonstrates a **complete DevOps workflow** for deploying a three-tier web application to the cloud. It implements Infrastructure-as-Code (IaC) best practices using HashiCorp tools and Ansible for configuration management.

### 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        ☁️  CLOUD (AWS/GCP/Azure)                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    🌐 VPC / Network                        │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │    │
│  │  │  🔴 PUBLIC  │  │  🟡 PRIVATE │  │  🟢 DATA        │  │    │
│  │  │  SUBNET     │  │  SUBNET     │  │  SUBNET         │  │    │
│  │  │             │  │             │  │                 │  │    │
│  │  │ ┌─────────┐ │  │ ┌─────────┐ │  │ ┌─────────────┐ │  │    │
│  │  │ │  NGINX  │ │  │ │  FLASK  │ │  │ │   MYSQL     │ │  │    │
│  │  │ │  :80    │ │  │ │  :8000  │ │  │ │   :3306     │ │  │    │
│  │  │ │ (LB/    │ │  │ │ (Gunicorn)     │ │ (Managed or │ │  │    │
│  │  │ │ Reverse │ │  │ │          │  │ │  Self-hosted)│ │  │    │
│  │  │ │ Proxy)  │ │  │ │          │  │ │              │ │  │    │
│  │  │ └────┬────┘ │  │ └────┬────┘ │  │ └──────┬──────┘ │  │    │
│  │  └───────┼──────┘ └────┼──────┘  └────────┼────────┘  │    │
│  │          │             │                   │           │    │
│  └──────────┼─────────────┼───────────────────┼───────────┘    │
│             │             │                   │                │
│      ┌──────▼──────┐ ┌────▼──────┐     ┌──────▼──────┐        │
│      │ Internet    │ │  App      │     │  Database   │        │
│      │ Gateway     │ │  Security │     │  Security   │        │
│      │ (IGW/NAT)   │ │  Group    │     │  Group      │        │
│      └─────────────┘ └───────────┘     └─────────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

### 🎯 Three Tiers

| Tier | Technology | Purpose | Port |
|------|------------|---------|------|
| 🌐 **Web** | Nginx | Reverse proxy, SSL termination, static files | 80/443 |
| ⚙️ **Application** | Flask + Gunicorn | Business logic, REST API, template rendering | 8000 (internal) |
| 🗄️ **Data** | MySQL 8.0 | Persistent storage, ACID transactions | 3306 (internal) |

---

## 📁 Project Structure

```
3-tier-app/
├── 📁 ansible/                 # Configuration Management
│   ├── 📄 ansible.cfg          # Ansible configuration
│   ├── 📄 deploy.yaml          # Main deployment playbook
│   ├── 📄 inventory            # Inventory file (hosts)
│   └── 📁 templates/           # Jinja2 templates
│       ├── 📄 flask.env.j2     # Environment variables
│       ├── 📄 flask.service.j2 # Systemd service
│       ├── 📄 init.sql.j2      # Database initialization
│       └── 📄 nginx.conf.j2    # Nginx site config
│
├── 📁 backend/                 # Flask Application
│   ├── 📄 app.py               # Application factory
│   ├── 📄 wsgi.py              # WSGI entry point
│   ├── 📄 requirements.txt     # Python dependencies
│   ├── 📄 Dockerfile           # Container image
│   ├── 📁 static/              # Static assets (CSS, JS, images)
│   └── 📁 templates/           # Jinja2 HTML templates
│
├── 📁 db/                      # Database
│   └── 📄 init.sql             # Schema initialization
│
├── 📁 nginx/                   # Nginx Configuration
│   └── 📄 default.conf         # Reverse proxy config
│
├── 📁 packer/                  # Image Building
│   ├── 📄 ubuntu.pkr.hcl       # Packer template
│   ├── 📄 variables.pkrvars.hcl # Packer variables
│   └── 📁 scripts/
│       └── 📄 setup.sh         # Provisioning script
│
├── 📁 terraform/               # Infrastructure as Code
│   ├── 📄 main.tf              # Main configuration
│   ├── 📄 provider.tf          # Provider configuration
│   ├── 📄 vpc.tf               # Network resources
│   ├── 📄 variables.tf         # Input variables
│   ├── 📄 outputs.tf           # Output values
│   └── 📄 versions.tf          # Version constraints
│
├── 📄 .gitignore               # Git ignore rules
└── 📄 README.md                # This file
```

---

## 🚀 Quick Start

### Prerequisites

- [ ] **Terraform** ≥ 1.0
- [ ] **Ansible** ≥ 2.14
- [ ] **Packer** ≥ 1.9 (optional, for custom AMIs)
- [ ] **AWS CLI** / **GCP CLI** / **Azure CLI** (configured)
- [ ] **SSH key** for instance access

### 1️⃣ Build Custom AMI (Optional)

```bash
cd packer

# Initialize Packer plugins
packer init ubuntu.pkr.hcl

# Validate template
packer validate ubuntu.pkr.hcl

# Build AMI
packer build -var-file=variables.pkrvars.hcl ubuntu.pkr.hcl
```

### 2️⃣ Provision Infrastructure

```bash
cd terraform

# Initialize Terraform
terraform init

# Plan deployment
terraform plan -out=tfplan

# Apply infrastructure
terraform apply tfplan
```

### 3️⃣ Configure & Deploy Application

```bash
cd ansible

# Update inventory with your instance IPs
# Edit inventory file or use dynamic inventory

# Run playbook
ansible-playbook -i inventory deploy.yaml
```

### 4️⃣ Verify Deployment

```bash
# Get application URL from Terraform output
terraform output application_url

# Test health endpoint
curl http://<APP_URL>/health
# {"status": "ok"}

# Open in browser
open http://<APP_URL>
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | MySQL connection string | `mysql+pymysql://notes:notes@127.0.0.1:3306/notes` |
| `SECRET_KEY` | Flask secret key | `change-me` |
| `FLASK_ENV` | Flask environment | `production` |
| `GUNICORN_WORKERS` | Number of Gunicorn workers | `3` |

### Terraform Variables

```hcl
# terraform/terraform.tfvars
aws_region       = "us-east-1"
instance_type    = "t3.micro"
key_pair_name    = "my-key-pair"
vpc_cidr         = "10.0.0.0/16"
public_subnet_cidrs  = ["10.0.1.0/24", "10.0.2.0/24"]
private_subnet_cidrs = ["10.0.11.0/24", "10.0.12.0/24"]
db_subnet_cidrs      = ["10.0.21.0/24", "10.0.22.0/24"]
```

---

## 🔧 Development

### Local Development Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DATABASE_URL="mysql+pymysql://notes:notes@localhost:3306/notes"
export SECRET_KEY="dev-secret"
export FLASK_ENV="development"

# Initialize database
flask --app app init-db

# Run development server
flask --app app run --debug --port 5000
```

### Running Tests

```bash
cd backend

# Run with pytest
pytest -v

# Run with coverage
pytest --cov=app --cov-report=html
```

### Docker Development

```bash
cd backend

# Build image
docker build -t flask-notes:dev .

# Run container
docker run -d \
  -p 5000:5000 \
  -e DATABASE_URL="mysql+pymysql://notes:notes@host.docker.internal:3306/notes" \
  -e SECRET_KEY="dev-secret" \
  flask-notes:dev
```

---

## 🔐 Security Features

- 🔒 **Network Segmentation** — Public, private, and data subnets
- 🛡️ **Security Groups** — Least-privilege ingress/egress rules
- 🔐 **Secrets Management** — Environment variables, no hardcoded credentials
- 📜 **Audit Logging** — CloudTrail / Cloud Audit Logs enabled
- 🔑 **IAM Roles** — Instance profiles with minimal permissions
- 🌐 **HTTPS Ready** — Nginx configured for SSL/TLS termination
- 🛑 **Non-root Containers** — Application runs as unprivileged user

---

## 📊 Monitoring & Observability

### Health Checks

```bash
# Application health
curl http://<APP_URL>/health

# Database connectivity
curl http://<APP_URL>/health/db

# Full system status
curl http://<APP_URL>/health/full
```

### Logging

- **Application logs**: `/var/log/flask-notes/`
- **Nginx logs**: `/var/log/nginx/`
- **Systemd logs**: `journalctl -u flask-notes -f`

### Metrics (Optional)

Add Prometheus metrics endpoint:

```python
# In app.py
from prometheus_flask_exporter import PrometheusMetrics
metrics = PrometheusMetrics(app)
```

---

## 🧪 Testing Strategy

| Test Type | Tool | Command |
|-----------|------|---------|
| Unit Tests | pytest | `pytest backend/tests/unit` |
| Integration | pytest | `pytest backend/tests/integration` |
| Linting | ruff, black | `ruff check . && black --check .` |
| Type Check | mypy | `mypy backend` |
| Security | bandit | `bandit -r backend` |
| IaC Validation | terraform validate | `terraform validate` |
| Playbook Syntax | ansible-lint | `ansible-lint ansible/deploy.yaml` |

---

## 🚢 Deployment Strategies

### Blue-Green Deployment

```bash
# Terraform supports blue-green via workspace or modules
terraform workspace new blue
terraform apply -var="deployment_color=blue"

# Switch traffic via load balancer / DNS
terraform workspace new green
terraform apply -var="deployment_color=green"
```

### Rolling Updates (Ansible)

```bash
# Limit to subset of hosts
ansible-playbook -i inventory deploy.yaml --limit "app[0]"

# Rolling with batch size
ansible-playbook -i inventory deploy.yaml --forks 1
```

---

## 💰 Cost Optimization

- 💡 **Right-size instances** — Use `t3.micro`/`t3.small` for dev
- 💡 **Spot Instances** — For fault-tolerant workloads (up to 90% savings)
- 💡 **Auto-scaling** — Scale based on CPU/memory metrics
- 💡 **RDS vs Self-hosted** — Compare managed DB costs
- 💡 **S3 for Static Assets** — Offload to CDN (CloudFront/CloudFlare)

---

## 🛠️ Troubleshooting

### Common Issues

<details>
<summary><b>🔴 Application won't start</b></summary>

```bash
# Check systemd status
sudo systemctl status flask-notes

# Check logs
sudo journalctl -u flask-notes -f --no-pager

# Verify environment file
cat /etc/flask-notes.env

# Test database connection
mysql -u notes -pnotes -h 127.0.0.1 notes
```
</details>

<details>
<summary><b>🔴 Nginx 502 Bad Gateway</b></summary>

```bash
# Check if Flask is running on port 8000
curl http://127.0.0.1:8000/health

# Check Nginx config
sudo nginx -t

# Check Nginx error logs
sudo tail -f /var/log/nginx/error.log
```
</details>

<details>
<summary><b>🔴 Database Connection Failed</b></summary>

```bash
# Check MySQL status
sudo systemctl status mysql

# Check MySQL logs
sudo tail -f /var/log/mysql/error.log

# Verify user/permissions
mysql -u root -e "SHOW GRANTS FOR 'notes'@'127.0.0.1';"
```
</details>

<details>
<summary><b>🔴 Terraform State Lock</b></summary>

```bash
# Force unlock (use with caution!)
terraform force-unlock <LOCK_ID>

# Or remove lock from DynamoDB (if using S3 backend)
aws dynamodb delete-item \
  --table-name terraform-locks \
  --key '{"LockID": {"S": "<LOCK_ID>"}}'
```
</details>

---

## 📚 Learn More

- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [Ansible Documentation](https://docs.ansible.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Code Style

- **Python**: Black + Ruff (line length 100)
- **Terraform**: `terraform fmt`
- **Ansible**: `ansible-lint`
- **YAML**: 2-space indent, no tabs

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Bogdan** — DevOps Engineer

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">

**Built with ❤️ using Infrastructure-as-Code**

*Terraform • Ansible • Flask • Nginx • MySQL*

</div>
