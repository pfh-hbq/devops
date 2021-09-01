terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}


provider "aws" {
  region = "eu-west-3c"
  profile = "default"
}

resource "aws_instance" "app" {
  ami = "ami-06602da18c878f98d"
  instance_type = "t2.micro"

  tags = {
    Name = "MSC time server"
  }
}