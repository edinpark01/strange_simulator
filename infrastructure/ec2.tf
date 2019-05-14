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
      "sudo echo \"ACCESS_KEY=${var.access_key}\"   >> /etc/profile.d/aws_env.sh",
      "sudo echo \"SECRET_KEY=${var.secret_key}\"   >> /etc/profile.d/aws_env.sh",
      "sudo echo \"REGION=${var.instance_region}\"  >> /etc/profile.d/aws_env.sh",
      "sudo echo \"BUCKET_NAME=${var.bucket_name}\" >> /etc/profile.d/aws_env.sh",
      "/simulator/provision_script.sh"
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

