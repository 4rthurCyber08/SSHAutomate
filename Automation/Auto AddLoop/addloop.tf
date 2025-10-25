terraform {
  required_providers {
    iosxe = {
      source = "CiscoDevNet/iosxe"
    }
  }
}

provider "iosxe" {
  username = "admin"
  password = "pass"
  url      = "https://10.11.11.1"
}

resource "iosxe_interface_loopback" "example" {
  name               = 12
  description        = "Created-via-Terraform"
  shutdown           = false
  ipv4_address       = "12.12.12.12"
  ipv4_address_mask  = "255.255.255.255"
}