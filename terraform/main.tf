resource "tls_private_key" "ansible-key" {
  algorithm = "ED25519"
}

resource "local_file" "private_key" {
  content  = tls_private_key.ansible-key.private_key_openssh
  filename = "${path.module}/ansible-key.pem"
}

resource "aws_key_pair" "ansible-key" {
  key_name   = "ansible-key-github"
  public_key = tls_private_key.ansible-key.public_key_openssh
}

data "aws_ami" "ubuntu" {
  most_recent = true

  owners = ["099720109477"]
  filter {
    name  = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "three_tier_app" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t2.micro"
  subnet_id                   = module.vpc.public_subnets[0]
  vpc_security_group_ids       = [aws_security_group.ansible-access.id]
  key_name                    =  aws_key_pair.ansible-key.key_name
  associate_public_ip_address = true
  tags = {
    Name = "three-tier-app"
  }
}
