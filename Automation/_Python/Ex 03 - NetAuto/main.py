import script
from netmiko import ConnectHandler

# RST IP
_rst_ip = input('What is the IP address of your RST VM? ')

# Device Ports
_C1 = 2262
_S1 = 2263
_S2 = 2264
_S3 = 2265
_S4 = 2266
_F1 = 2267
_E1 = 2268
_E2 = 2269
_E3 = 2270
_I1 = 2271
_R1 = 2272

# ConnectHandler Arguments
device_info = {
    'device_type': 'cisco_ios_telnet',
    'ip': _rst_ip,
    'password': 'pass',
    'secret': 'pass',
    'port': 2001
}

config_order = [
    'C1', 
    'S1', 
    'S2', 
    'S3', 
    'S4', 
    'F1', 
    'E1', 
    'E2', 
    'E3', 
    'I1', 
    'R1'
]

# Configure Devices
for device in config_order:
    if device == 'C1':
        device_info['port'] = _C1
    elif device == 'S1':
        device_info['port'] = _S1
    elif device == 'S2':
        device_info['port'] = _S2
    elif device == 'S3':
        device_info['port'] = _S3
    elif device == 'S4':
        device_info['port'] = _S4
    elif device == 'F1':
        device_info['port'] = _F1
    elif device == 'E1':
        device_info['port'] = _E1
    elif device == 'E2':
        device_info['port'] = _E2
    elif device == 'E3':
        device_info['port'] = _E3
    elif device == 'I1':
        device_info['port'] = _I1
    elif device == 'R1':
        device_info['port'] = _R1
    
    access_cli = ConnectHandler(**device_info)
    access_cli.enable()

    print(f'Configuring {device}.. ')

    if device == 'C1':
        access_cli.send_config_set(script.C1_config)
    elif device == 'S1':
        access_cli.send_config_set(script.S1_config)
    elif device == 'S2':
        access_cli.send_config_set(script.S2_config)
    elif device == 'S3':
        access_cli.send_config_set(script.S3_config)
    elif device == 'S4':
        access_cli.send_config_set(script.S4_config)
    elif device == 'F1':
        access_cli.send_config_set(script.F1_config)
    elif device == 'E1':
        access_cli.send_config_set(script.E1_config)
    elif device == 'E2':
        access_cli.send_config_set(script.E2_config)
    elif device == 'E3':
        access_cli.send_config_set(script.E3_config)
    elif device == 'I1':
        access_cli.send_config_set(script.I1_config)
    elif device == 'R1':
        access_cli.send_config_set(script.R1_config)
    
    print(f'Configuration Complete. \n \n')