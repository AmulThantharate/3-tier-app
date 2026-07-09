output "public_ip" {
  value = aws_instance.three_tier_app.public_ip
}

output "private_key" {
  value     = tls_private_key.ansible-key.private_key_openssh
  sensitive = true
}
