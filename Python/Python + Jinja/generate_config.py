from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('router_config.j2')

data = {
    "hostname": "R1",
    "interface": "GigabitEthernet0/0",
    "ip": "192.168.1.1",
    "mask": "255.255.255.0"
}

output = template.render(data)

print(output)
