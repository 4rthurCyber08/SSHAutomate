from netmiko import ConnectHandler

## Get Device Information
vm_ip = input('What is the ipv4 address of your RSTHayup VM? (x.x.x.x): ')
user_name = 'admin'
user_pass = 'pass'
enable_secret = 'pass'


# Values for ConnectHandler
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': vm_ip,
    'username': user_name,
    'password': user_pass,
    'secret': enable_secret,
    'port': 2001
}


# Device Port Numbers
p1 = 2001
p2 = 2002
a1 = 2003
a2 = 2004
s1 = 2005
d1 = 2006
d2 = 2007
s2 = 2008
r4 = 2009

## Device Configurations
p1_config = [
    'hostname Manila-PC',
    'int e0/0',
    'ip add 172.16.255.50 255.255.255.128',
    'no shut',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.126',
    'end'
]

p2_config = [
    'hostname CEBU-PC',
    'int e1/0',
    'ip add 172.16.255.150 255.255.255.128',
    'no shut',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.254',
    'end'
]

s1_config = [
    'hostname Manila-CAServer',
    'int e1/0',
    'ip add 172.16.255.55 255.255.255.128',
    'no shut',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.126',
    'end'
]

s2_config = [
    'hostname Cebu-FileServer',
    'int e1/0',
    'ip add 172.16.255.155 255.255.255.128',
    'no shut',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.254',
    'end'
]

a1_config = [
    'hostname Manila-CoreSW-A',
    'vlan 12',
    'name Branch-Manila',
    'vlan 14',
    'name Branch-Cebu',
    'int vlan 12',
    'ip add 172.16.255.1 255.255.255.128',
    'no shut',
    'exit',
    'int e0/0',
    'sw mo ac',
    'sw ac vlan 12',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.126',
    'end'
]

a2_config = [
    'hostname Cebu-CoreSW-A',
    'vlan 12',
    'name Branch-Manila',
    'vlan 14',
    'name Branch-Cebu',
    'int vlan 14',
    'ip add 172.16.255.129 255.255.255.128',
    'no shut',
    'exit',
    'int e1/0',
    'sw mo ac',
    'sw ac vlan 14',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.254',
    'end'
]

d1_config = [
    'hostname Manila-CoreSW-B',
    'ip routing',
    'router ospf 20',
    'router-id 172.16.255.3',
    'vlan 12',
    'name Branch-Manila',
    'vlan 14',
    'name Branch-Cebu',
    'int vlan 12',
    'ip add 172.16.255.2 255.255.255.128',
    'ip ospf 20 area 0',
    'no shut',
    'exit',
    'int vlan 14',
    'ip add 172.16.255.130 255.255.255.128',
    'ip ospf 20 area 0',
    'no shut',
    'exit',
    'int range e1/0,e2/0',
    'no shut',
    'sw mo ac',
    'sw ac vlan 12',
    'end'
]

d2_config = [
    'hostname Cebu-CoreSW-B',
    'ip routing',
    'router ospf 20',
    'router-id 172.16.255.4',
    'vlan 12',
    'name Branch-Manila',
    'vlan 14',
    'name Branch-Cebu',
    'int vlan 12',
    'ip add 172.16.255.3 255.255.255.128',
    'ip ospf 20 area 0',
    'no shut',
    'exit',
    'int vlan 14',
    'ip add 172.16.255.131 255.255.255.128',
    'ip ospf 20 area 0',
    'no shut',
    'exit',
    'int range e1/0,e2/1',
    'no shut',
    'sw mo ac',
    'sw ac vlan 14',
    'end'
]

r4_config = [
    'hostname Makati-Edge',
    'router ospf 20',
    'router-id 172.16.255.126',
    'passive-interface e3/3',
    'default-information originate always',
    'exit',
    'int e2/0',
    'ip add 172.16.255.126 255.255.255.128',
    'ip ospf 20 area 0',
    'no shut',
    'exit',
    'int e2/1',
    'ip add 172.16.255.254 255.255.255.128',
    'ip ospf 20 area 0',
    'no shut',
    'exit',
    'int e3/3',
    'ip ospf 20 area 0',
    'no shut',
    'ip add dhcp',
    'end'
]


## CONNECT To Devices
# Device to connect
device_list = ['P1', 'P2', 'S1', 'S2', 'A1', 'A2', 'D1', 'D2', 'R4']

for device in device_list:
    # Specify port number of the device
    if device == 'P1': 
        device_info['port'] = p1
    elif device == 'P2':
        device_info['port'] = p2
    elif device == 'S1':
        device_info['port'] = s1
    elif device == 'S2':
        device_info['port'] = s2
    elif device == 'A1':
        device_info['port'] = a1
    elif device == 'A2':
        device_info['port'] = a2
    elif device == 'D1':
        device_info['port'] = d1
    elif device == 'D2':
        device_info['port'] = d2
    elif device == 'R4':
        device_info['port'] = r4
    print(f"Configuring {device} ")
    # PUSH Configurations
    accesscli = ConnectHandler(**device_info)
    accesscli.enable()

        # Specify port number of the device
    if device == 'P1': 
        output = accesscli.send_config_set(p1_config)
    elif device == 'P2':
        output = accesscli.send_config_set(p2_config)
    elif device == 'S1':
        output = accesscli.send_config_set(s1_config)
    elif device == 'S2':
        output = accesscli.send_config_set(s2_config)
    elif device == 'A1':
        output = accesscli.send_config_set(a1_config)
    elif device == 'A2':
        output = accesscli.send_config_set(a2_config)
    elif device == 'D1':
        output = accesscli.send_config_set(d1_config)
    elif device == 'D2':
        output = accesscli.send_config_set(d2_config)
    elif device == 'R4':
        output = accesscli.send_config_set(r4_config)
        
    print("Configuration Complete!\n\n")
    print(output)
    
print(f'RST ({vm_ip}) Configured Successfully!!')
