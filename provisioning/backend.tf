terraform {
  backend "s3" {
    bucket = "terra-state-bucket"
    key    = "tfstate"
    region = "eu-west-2"
  }
}
