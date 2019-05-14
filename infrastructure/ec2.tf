provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region     = "${var.instance_region}"
}

resource "aws_instance" "EC2" {
  ami                   = "ami-098bb5d92c8886ca1"
  instance_type         = "t2.micro"
  iam_instance_profile  = "S3-Admin-Access"
  key_name              = "${aws_key_pair.terraform-key.key_name}"

  provisioner "remote-exec" {
    inline = [
      "sudo mkdir -p --mode=777 /simulator"
    ]
  }

  provisioner "file" {
    source      = "../python/"
    destination = "/simulator"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo chmod -R 777 /simulator/",
      "echo \"ACCESS_KEY=${var.access_key}\n\n$(cat ${var.sim_path})\" > ${var.sim_path}",
      "echo \"SECRET_KEY=${var.secret_key}\n$(cat ${var.sim_path})\"   > ${var.sim_path}",
      "echo \"REGION=${var.instance_region}\n$(cat ${var.sim_path})\"  > ${var.sim_path}",
      "echo \"BUCKET_NAME=${var.bucket_name}\n$(cat ${var.sim_path})\" > ${var.sim_path}",
      "echo \"#!/bin/bash\n$(cat ${var.sim_path})\"                    > ${var.sim_path}",
      "sudo /simulator/provision_script.sh"
    ]
  }

  connection {
    user        = "ec2-user"
    private_key = "${file("${path.module}/mykey")}"
  }
}

resource "aws_key_pair" "terraform-key" {
  key_name    = "mykey"
  public_key  = "${file("${path.module}/mykey.pub")}"
}

