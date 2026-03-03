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
  host     = "192.168.102.11"
}

resource "iosxe_interface_loopback" "example" {
  name               = 22
  description        = "My First TF Script Attempt"
  shutdown           = false
  ipv4_address       = "2.2.2.2"
  ipv4_address_mask  = "255.255.255.255"

}

