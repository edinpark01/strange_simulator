provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secre_key}"
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
      "sudo chmod 777 /simulator/provision_script.sh",
      "sudo chmod 777 /simulator/simulator.py",
      "sudo /simulator/provision_script.sh ${var.access_key} ${var.secre_key} ${var.instance_region} ${var.bucket_name}"
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

