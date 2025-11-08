import json
from netmiko import ConnectHandler

# Read JSON file in Read only mode (r)
with open('device_info.json', 'r') as file:
    data = json.load(file)

# Parse Data from the JSON file
info = data['device_info']
config = data['device_config']

# Configurations
add_loop = [
    'int loopback 0',
    f'ip add {config["loop_1"]} {config["/32"]}',
    f'description {config["desc"]}',
    'end'
]

# Push Configs to Device
access_cli = ConnectHandler(**info)
access_cli.send_config_set(add_loop)
access_cli.disconnect()