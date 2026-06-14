terraform {
  backend "s3" {
    bucket         = "sneha-024-terraform-state-eunorth1"
    key            = "project-3/terraform.tfstate"
    region         = "eu-north-1"
    dynamodb_table = "terraform-locks"
  }
}
