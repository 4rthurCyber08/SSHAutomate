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
  name               = 200
  description        = "My First TF Script Attempt"
  shutdown           = false
  ipv4_address       = "2.2.2.2"
  ipv4_address_mask  = "255.255.255.255"
}