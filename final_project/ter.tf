provider "aws" {
        region = "eu-central-1"
	shared_credentials_files = ["/var/jenkins_home/credentials"]
}

resource "aws_instance" "web" {
        ami = "ami-0d527b8c289b4af7f"
        instance_type = "t2.micro"
        vpc_security_group_ids = [aws_security_group.web.id]

        key_name = "Frankfurt"

        tags = {
                Name = "Target_Web"
        }

        lifecycle {
                create_before_destroy = true
        }
}

resource "aws_security_group" "web" {
        name = "Web Security Group"

        ingress {
                from_port = 22
                to_port = 22
                protocol = "tcp"
                cidr_blocks = ["0.0.0.0/0"]
        }

        ingress {
                from_port = 80
                to_port = 80
                protocol = "tcp"
                cidr_blocks = ["0.0.0.0/0"]
        }

        egress {
                from_port = 0
                to_port = 0
                protocol = "-1"
                cidr_blocks = ["0.0.0.0/0"]
        }

}

output "instance_ip" {
  value       = aws_instance.web.public_ip
}
