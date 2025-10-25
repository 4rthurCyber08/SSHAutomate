node 'cisco.example.com' {
  cisco_ios_interface { 'GigabitEthernet0/1':
    ensure => present,
    description => "Uplink to Core",
    speed => 'auto',
    duplex => 'auto',
    vlan_access => '10',
}