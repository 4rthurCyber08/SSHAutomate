
<!-- Your monitor number = #$34T# -->


## ⛅ Warm Up for Day 4.

### Setup your Day 1 BUT DO NOT configure any device.

<br>

## 🎯 Review
### 1. Which two encoding methods are supported by REST APIs? (Choose Two)
	A. SGML
	B. YAML
	C. XML
	D. JSON
	E. EBCDIC

<br>

### 2. Which output displays a JSON data representation?
A.
~~~
	{
	  "response":{
	  "taskld":{};
	  "url": "string"
	  };
	  "version": "string"
	}
~~~

<br>

B.
~~~
	{
	  "response"-{
	  "taskld"-{},
	  "url"- "string"
	  },
	  "version"- "string"
	}
~~~

<br>

C.
~~~
	{
	  "response":{
	  "taskld":{},
	  "url": "string"
	  },
	  "version": "string"
	}
~~~

<br>

D.
~~~
	{
	  "response",{
	  "taskld",{};
	  "url", "string"
	  };
	  "version", "string"

	}
~~~

&nbsp;
---
&nbsp;

### 3. OSPF Configuration
Refer to the Topology.   
All routers are configured with IP addressing EXCEPT for the link between R1 & R3.  
Finish the configuration by completing the ff:  

<br>

Task 1.  
	Using the 172.16.160.0/21 network,   
	- assign the 1st VALID ip address on R1's e0/1 interface.
	- assign the Last VALID ip address on R3's e0/1 interface.

<br>

Task 2.  
	Configure single area OSPF on all routers with the ff:  
	- All routers belong to AREA 2
	- Use OSPF Process 5
	- Assign each router's LOOPBACK 0 as their router ID.
	- The link between R2 & R3 must be point-to-point.
	- R1 must have the lowest priority on its e0/0 & e0/1 interfaces.
	- Advertise all Connected routes.

<br>

Task 3.  
	Configure static routes.  
	- Configure a static host route on R1 destined for R3's LOOPBACK 
	using R3 as the next hop.
	- Configure a floating static route on R1 destined for R3's LOOPBACK 
	using R2 as the next hop with an Administrative Distance equal 
	to EXTERNAL EIGRP.

<br>
<br>

ANSWER HERE  
Task 1.  
~~~
@R1
conf t
 interface ___
  ip add ___.___.___.___  ___.___.___.___
  no shut
  end

@R3
conf t
 interface ___
  ip add ___.___.___.___  ___.___.___.___
  no shut
  end
~~~

<br>

Task 2.
~~~
@R1
conf t
 interface ___
  ip ospf ___ ___
 interface ___
  ip ospf ___ ___
 router ospf ___
  router-id ___.___.___.___
  network ___.___.___.___  ___.___.___.___ area ___
  network ___.___.___.___  ___.___.___.___ area ___
  network ___.___.___.___  ___.___.___.___ area ___
  end

@R2
conf t
 interface ___
  ip ospf ___ ___
  exit
 router ospf ___
  router-id ___ 
  network ___.___.___.___  ___.___.___.___ area ___
  network ___.___.___.___  ___.___.___.___ area ___
  network ___.___.___.___  ___.___.___.___ area ___
  end
  
@R3
conf t
 interface ___
  ip ospf ___ ___
  exit
 router ospf 5
  router-id ___ 
  network ___.___.___.___  ___.___.___.___ area ___
  network ___.___.___.___  ___.___.___.___ area ___
  network ___.___.___.___  ___.___.___.___ area ___
  end
~~~  

<br>

Task 3.
~~~
@R1
conf t
 ip route 192.168.5.33 255.255.255.___  ___.___.___.___
 ip route 192.168.5.33 255.255.255.___  ___.___.___.___  ___
 end
~~~

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

ANSWERS:  
Task 1.  
~~~
@R1
conf t
 interface e0/1
  ip add 172.16.160.1 255.255.248.0
  no shut
  end

@R3
conf t
 interface e0/1
  ip add 172.16.167.254 255.255.248.0
  no shut
  end
~~~

<br>

Task 2.
~~~
@R1
conf t
 interface e0/0
  ip ospf priority 0
 interface e0/1
  ip ospf priority 0
 router ospf 5
  router-id 172.16.97.111
  network 172.16.97.111 0.0.0.0 area 2
  network 10.0.15.64 0.0.0.31 area 2
  network 172.16.160.0 0.0.7.255 area 2
  end

@R2
conf t
 interface e0/1
  ip ospf network point-to-point
  exit
 router ospf 5
  router-id 10.46.187.22 
  network 10.46.187.22 0.0.0.0 area 2
  network 10.0.15.64 0.0.0.31 area 2
  network 192.168.0.152 0.0.0.3 area 2
  end
  
@R3
conf t
 interface e0/0
  ip ospf network point-to-point
  exit
 router ospf 5
  router-id 192.168.5.33
  network 192.168.5.33 0.0.0.0 area 2
  network 192.168.0.152 0.0.0.3 area 2
  network 172.16.160.0 0.0.7.255 area 2
  end
~~~

<br>

Task 3.
~~~
@R1
conf t
 ip route 192.168.5.33 255.255.255.255 172.16.167.254
 ip route 192.168.5.33 255.255.255.255 10.0.15.90 170
 end
~~~

</details>

<br>
<br>

---
&nbsp;

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

<br>
<br>

---
&nbsp;




























































### 03. Domain Name System
"Connect to websites through IP addresses alone"

@cmd
ping google.com         ___.___.___.___
ping cisco.com     
ping rivanit.com   



Set up your own DNS Server.
 - Create a Zone File for ccna#$34T#.com
   Forward & Reverse

 - DNS Records

@cmd
ping ns.google.com      ___.___.___.___
ping www
ping imap
ping pop
ping smtp


Exercise 02: Configure DNS records for devices:
  CoreBABA,   cb
  CoreTaas,   ct
  CUCM,       cm
  EDGE,       ed
  AP,         ap
  WLC,        wc
  Cam6,       c6
  Cam8,       c8
  Ephone1,    e1
  Ephone2,    e2


Configure a webserver for ccna#$34T#.com



















__________
**********
04. File Transfer

Upload configurations to FTP Server. (CoreTaas, CoreBaba, CUCM, EDGE)

@Cisco
copy run ftp://ccna#$34T#.com


How to copy the current IOS of a Cisco Switch

@Cisco
archive upload-sw ftp://ccna#$34T#.com



__________
**********
05. Mail Exchanger

Create an MX record on the Zone file.
	Install .NET Framework 3.5 Features


Create users and emails for ccna#$34T#.com and bpiph#$34T#.com

  User1: ac
  Pass: C1sc0123
  
  User: Support
  Pass: C1sc0123
  
  

__________
**********
06. SoftWare Defined Networking

On-Prem => Cloud

Infrastructure Layer / Data Plane - Processing of Data
Control Layer / Control Plane - Reference of Data
Application Layer / Management Plane - Graphical presentation of Data

@Cisco
show run

Meraki, SD-WAN, Cisco NSO



Get started with Meraki: https://account.meraki.com/login

MERAKI Account:
  Firewall 1 (Monitor Numbers that end with 1)
	USER: rivanmeraki1@gmail.com
	PASS: C1sc0,123
  
  Firewall 2 (Monitor Numbers that end with 2)
	USER: rivanmeraki2@gmail.com
	PASS: C1sc0,123
	

GMAIL Account (if asked for verification)
  Firewall 1 
    USER: rivanmeraki1@gmail.com
    PASS: C1sc0123$$

  Firewall 2
   USER: rivanmeraki2@gmail.com
   PASS: C1sc0123$$
  




__________
**********
07. OSI Layer

PDU (Protocol Data Unit)

7. Application Layer 

"Underlying service that supports applications"
SMTP
Resource sharing
Service advertisement
Gramaphone

6. Presentation Layer - File extension

Data
encryption
-tion
.wav .jpg .au .exe .psd


5. Session Layer - Session established

Data Stream
stateful

Commands: netstat -s -p tcp, telnet, ssh


4. Transport Layer - TCP/UDP

Segments
Three way handshake
Sliding Window

Commands: nmap -v 10.#$34T#.1.10

Well-known ports 0 - 1023
Registered ports 1024 - 49151
Ephemeral/Dynamic ports 49152 - 65535


3. Network Layer - IP addresses

Packets
Routing protocols
Forwarding packets

Commands: show ip int br, sh ip route


2. Data-link Layer - MAC Addresses

Frames
FCS
Preamble

Commands: show vlan brief


1. Physical Layer - "Things you touch"

Speed = b 
Data = B

Commands: show cdp neigh








__________
**********
08. Security Fundamentals

Setup

CSR1000v:
  Name: UTM-PH
  Size: Small
  Config: None
  
  NetAdapter: NAT         208.8.8.0 /24
  NetAdapter 2: VMnet2    192.168.102.0 /24
  NetAdapter 3: VMnet3    192.168.103.0 /24

  
!@UTM-PH
conf t
 hostname UTM-PH
 enable secret pass
 service password-encryption
 no logging console
 no ip domain lookup
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 line vty 0 24
  password pass
  login local
  exec-timeout 0 0
  transport input all
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 10.10.10.11 255.255.255.0
  no shut
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 ip name-server 8.8.8.8 10.#$34T#.1.10
 ip domain lookup
 end
wr


How to attack? Network scanning

@cmd
ping 10.k.100.8
nmap -sP 10.k.100.0/24
nmap -v 10.k.100.8

What ports are revealed?
 -
 -



SPAN

@CoreBABA
conf t
 monitor session 1 source interface fa0/3,fa0/5,fa0/7
 monitor session 1 destination interface fa0/1
 end

Real-time Transport Protocol


@cmd
nmap -sP 10.k.1.0/24
nmap -v 10.k.1.10

What ports are revealed?
139? 445?

That's a vulnerable system. No Firewall. Attack it.

net use \\10.k.1.10\ipc$     Privilege Escalation
net use x: /delete
net use x: \\10.k.1.10\c$


__________
**********
09. Packet Filtering

There's a big problem in humanity. 
It's corrupting everyone's brains.

@cmd
youporn.com
pornhub.com
redtube.com
faketaxi.com
bangbros.com
bangbus.com
pinayflix.com
xhamster.com
iyottube.com

Protect your most important asset: The brain


@UTM-PH
config t
 no ip access-list standard NOPORNFAP
 ip access-list standard NOPORNFAP
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  permit any
 int gi 1
  ip access-group NOPORNFAP in
  end
wr
show ip access-list int g1


Remove the access-list

@UTM-PH
config t
 int gi 1
  no ip access-group NOPORNFAP in
  end



Alternative: use standard ACL 1-99

@UTM-PH
config t
 no access-list 69
 access-list 69 deny 66.254.0.0 0.0.255.255
 access-list 69 deny 104.21.0.0 0.0.255.255
 access-list 69 deny 68.235.0.0 0.0.255.255
 access-list 69 deny 104.17.0.0 0.0.255.255
 access-list 69 deny 88.208.0.0 0.0.255.255
 access-list 69 deny 208.77.0.0 0.0.255.255
 access-list 69 deny 172.67.0.0 0.0.255.255
 access-list 69 permit any
 int gi 1
  ip access-group 69 in
  end


Exercise 04: Block schools

@cmd
ping www.dlsu.edu.ph 
ping www.ccp.edu.ph      
ping www.feu.edu.ph 
ping  www.ue.edu.ph 
ping  www.yourschool.edu.ph = _________


@UTM-PH
config t
 no ip access-list standard NOSKUL
 ip access-list standard NOSKUL
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  permit any
 int gi 1
  ip access-group NOSKUL in
  end
wr
show ip access-list int g1


Exercise 05: Block torrents

www.thepiratebay.org
www.limetorrents.com
www.freeanimeonline.com
www.torlock2.com
www.hentaisites.com
www.iptorrents.com

@UTM-PH
config t
 no ip access-list standard NOTOR
 ip access-list standard NOTOR
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  permit any
 int gi 1
  ip access-group NOTOR in
  end
wr
show ip access-list int g1



Exercise 06: Block Klassmates

config t
 no ip access-list standard NOCLASSMATES
 ip access-list standard NOCLASSMATES
  deny 10.__.0.0 0.0.255.255
  deny 10.__.0.0 0.0.255.255
  deny 10.__.0.0 0.0.255.255
  deny 10.__.0.0 0.0.255.255
  deny 10.__.0.0 0.0.255.255
  deny 10.__.0.0 0.0.255.255
  deny 10.__.0.0 0.0.255.255
  permit any
 int gi 0/0/1
 ip access-group NOCLASSMATES in
 end





BLUE TEAM
@cmd
netstat -ano

Higher port = Hacker

SCAN for Vulnerable sites

www.sti.edu.ph
www.rivanit.com
www.cia.gov
www.nemsu.edu.ph

Which sites are secure?


RED TEAM
Make the firewall vulnerable to learn.

@UTM-PH
config t
 int gi 3
  no shut
  ip add 192.168.103.11 255.255.255.0
  ip add 192.168.103.10 255.255.255.0 Secondary
 service finger
 service tcp-small-servers
 service udp-small-servers
 ip dns server
 ip http server
 ip http secure-server
 ip host www.web310.com 192.168.103.10
 ip host www.web311.com 192.168.103.11
 end

Review: Create a DNS A record for www.ccna#$34T#.com
192.168.103.10 www.web310.com
192.168.103.11 www.web311.com
  
  or
  
Modify the hosts file: c:\Windows\system32\drivers\etc\hosts


Scan the sites:

@cmd
nmap -v www.web310.com
nmap -v www.web311.com



Exercise 07: BLUE TEAM, protect your POGO sites.
Open only the following port:
  www.web310.com open only http, https, ping
  www.web311.com open only dns, https, ssh
  
   protocol         hacker    victim       port
tcp,udp,icmp,IP     Any      web310/11

@UTM-PH
conf t
 service timestamps log datetime
 service timestamps debug datetime
 logging 10.#$34T#.1.10
 logging trap 5
 end
wr

@UTM-PH
conf t
 no ip access-list extended FWP1
 ip access-list extended FWP1
 permit tcp Any host www.web310.com eq __ log
 permit tcp Any host www.web310.com eq __ log
 permit __ Any host www.web310.com log
 permit tcp Any host www.web311.com eq __ log
 permit tcp Any host www.web311.com eq __ log
 permit tcp Any host www.web311.com eq __ log
 Int gi 3
  ip access-group FWP1 in
  end
  
Remove the Firewall:

@UTM-PH
config t
 int gi 3
  no ip access-group FWP1 in
end



Exercise 07: Attacking the wrong ports

@UTM-PH
telnet 208.8.8.11 19



CTRL + SHIFT + 6 Then X


Exercise 08: 
Create an access-list named FWP2 to open the following ports:

www.web310.com open only ssh, domain, ftp, mysql
www.web311.com open only imap, smtp, ping, daytime

@UTM-PH
conf t
 no ip access-list extended FWP2
 ip access-list extended FWP2
 permit __ Any host www.____.com eq __ log
 permit __ Any host www.____.com eq __ log
 permit __ Any host www.____.com log
 permit __ Any host www.____.com eq __ log
 permit __ Any host www.____.com eq __ log
 permit __ Any host www.____.com eq __ log
 Int gi 3
  ip access-group FWP2 in
  end


Exercise 09: You are the SUPERPRANING Admin for POGO sites:
www.web310.com open only https
www.web311.com open only ping

config t
 no ip access-list Extended PRANING3
 ip access-list Extended PRANING3
  ?
  ?
 int gi 3
  ip access-group PRANING3 in
  end


Exercise 10: You are taking the CCNA exam and these are the ports you should remember:

BUT FIRST: Go to UTM-PH GUI and activate CME

Then,

@UTM-PH
conf t
 no telephony-service
 telephony-service
  no auto assign
  no auto-reg-ephone
  max-ephones 5
  max-dn 20
  ip source-address 208.8.8.11 port 2000
  exit
 voice service voip
  allow-connections h323 to sip
          
  allow-connections sip to h323
  allow-connections sip to sip
  supplementary-service h450.12
 sip
   bind control source-interface g1
   bind media source-interface g1
   registrar server expires max 600 min 60
 voice register global
  mode cme
  source-address 208.8.8.11 port 5060
  max-dn 12
  max-pool 12
  authenticate register
  create profile sync syncinfo.xml
  end
  

Now, open the following ports otherwise you will work in Jollibee.

www.web310.com open only daytime, chargen, skinny-client-control-protocol
www.web311.com open only domain, discard, sip, finger, ping, ntp

@UTM-PH
config t
 no ip access-list ______ NOJOLLIBEEPLS
 ip access-list ______ NOJOLLIBEEPLS

 int gi 3
  ip ______  ___  ___
  end
  
  
Make sure to remove firewall for next activity:

@UTM-PH
end
show run | s interface



__________
**********
10. Configure Cisco Network Services

NETWORK TIME PROTOCOL OR NTP 

@cmd
ping time.google.com

@UTM-PH
config t
ntp server 216.239.35.8
end
show ntp associations


Configure Master Time Server

@UTM-PH
config t
ntp master 1
ntp update-calendar
end
show ntp associations


__________
**********
11. Network Address Translation

INSIDE LOCAL    INSIDE GLOBAL    OUTSIDE LOCAL    OUTSIDE GLOBAL



@BLDG-1
sudo su
ifconfig eth0 192.168.103.21 netmask 255.255.255.0 up
route add default gw 192.168.103.11
ping 192.168.103.11

@BLDG-2
sudo su
ifconfig eth0 192.168.103.22 netmask 255.255.255.0 up
route add default gw 192.168.103.11
ping 192.168.103.11

@BLDG-3
sudo su
ifconfig eth0 192.168.103.23 netmask 255.255.255.0 up
route add default gw 192.168.103.11







STEP 1: Define INSIDE AND OUTSIDE

STEP 2: Create Access-list to permit IP of Inside

STEP 3: Create a NAT pool with overload


@UTM-PH
config t
 int gi 1
  ip nat OUTSIDE
 int gi 2
  ip nat INSIDE
 int gi 3
  ip nat INSIDE
 no access-list 8
 access-list 8 permit 192.168.102.0 0.0.0.255
 access-list 8 permit 192.168.103.0 0.0.0.255
 ip nat inside source list 8 interface Gi 1 overload
 ip nat inside source static 192.168.103.21 208.8.8.51
 ip nat inside source static 192.168.103.22 208.8.8.52
 end
show ip nat translations 

@BLDGS
ping   8.8.8.8    4.4.4.4     8.8.4.4





Remove Conflicts:

@UTM-PH
clear ip nat translations *
 no ip nat inside source list 8 interface Gi 1 overload
 no ip nat inside source static 192.168.103.21 208.8.8.51
 no ip nat inside source static 192.168.103.22 208.8.8.52
 end
show ip nat translations 






CREATING A WEB PROXY OR HIDING BEHIND NAT:

@ping
www.sti.edu.ph:      vs     www.dlsu.edu.ph:


Access the web of BLDG first.
192.168.103.21
192.168.103.22
192.168.103.23


Now hide behind the firewall.


@UTM-PH
config t
IP Nat inside source static tcp 192.168.103.21 80 208.8.8.101 8080
end
show ip nat translation

Now open 208.8.8.101:8080 on browser






__________
**********
12. S2S VPN with Certificate Auth

_____________________
********************* SETUP VMNETS

VMWare > Edit > Virtual Network Editor

Add/Edit the following VMNets:

VMNet 2, 
	VMNet Info: Host-only
	IP address: 192.168.102.0
	Subnet Mask: 255.255.255.0
	DHCP: Unchecked

VMNet 3, 
	VMNet Info: Host-only
	IP address: 192.168.103.0
	Subnet Mask: 255.255.255.0
	DHCP: Unchecked

VMNet 4, 
	VMNet Info: Host-only
	IP address: 192.168.104.0
	Subnet Mask: 255.255.255.0
	DHCP: Unchecked
	
VMNet 8(NAT)
	VMNet Info: NAT
	IP address: 208.8.8.0
	Subnet Mask: 255.255.255.0
	DHCP: Checked
	
	
_____________________
********************* DEPLOY CSRS AND LINUX

Note the following VM Files:

CSR1000v 17.x = VPN-EDGE
YVM-v6 = BLDG


Deploy 2 CSR1000v

1. VPN-PH
	Name of Virtual Machine: VPN-PH
	Deployment Options: Small
	Bootstrap:
		Router Name: VPN-PH
		Login User: admin
		Login Pass: pass

	Network Adapter: NAT
	Network Adapter 2: VMNet2
	Network Adapter 3: VMNet3
		
2. VPN-JP
	Name of Virtual Machine: VPN-JP
	Deployment Options: Small
	Bootstrap:
		Router Name: VPN-JP
		Login User: admin
		Login Pass: pass

	Network Adapter: NAT
	Network Adapter 2: VMNet2
	Network Adapter 3: VMNet4
	


Deploy 2 YVM-v6

1. BLDG-PH
	Name of Virtual Machine: BLDG-PH
	Network Adapter: VMNet3
	
2. BLDG-JP
	Name of Virtual Machine: BLDG-JP
	Network Adapter: VMNet4


_____________________
********************* CONFIGURE DEVICES

!@VPN-PH
conf t
 hostname VPN-PH
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 10.10.10.40 255.255.255.224
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 end
wr


!@VPN-JP
conf t
 hostname VPN-JP
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line vty 0 14
  transport input all
  password pass
  login local 
  exec-timeout 0 0
 int g1
  ip add 208.8.8.12 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.12 255.255.255.0
  no shut
 int g3
  ip add 20.20.20.50 255.255.255.248
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 end
wr


!@BLDG-PH
sudo su
ifconfig eth0 10.10.10.41 netmask 255.255.255.224 up
route add default gw 10.10.10.40
ping 10.10.10.40


!@BLDG-JP
sudo su
ifconfig eth0 20.20.20.51 netmask 255.255.255.248 up
route add default gw 20.20.20.50
ping 20.20.20.50


_____________________
********************* CREATE USER ACCOUNTS ON BLDGs
!@BLDG-PH, BLDG-JP
sudo  su
adduser admin
> pass
> pass


_____________________
********************* Deploy CA Server & Issue Certificates

NetOps VM
	NetAdapter: NAT
	NetAdapter 2: VMNet2
	NetAdapter 3: VMNet3
	NetAdapter 4: Bridged (Replicate)

	Login: root
	Pass: C1sc0123
	

1. Configure IP addressing for NetAdapter 2 (Verify MAC ADDRESS of interface)

!@NetOps
ifconfig ens192 192.168.102.100 netmask 255.255.255.0 up
ifconfig ens224 192.168.103.100 netmask 255.255.255.0 up



2. Create a directory for keys and certificates.

!@NetOps
cd
mkdir keystore
cd keystore
mkdir rivankeys
cd rivankeys


3. Create a Private key with a Selfsigned Certificate (x509)

!@NetOps
openssl req -x509 -newkey rsa:2048 -days 365 -keyout key-rivan.pem -out ca-rivan.pem -nodes


Sample Output:
-----
Country Name (2 letter code) [XX]:PH
State or Province Name (full name) []:National Capital Region
Locality Name (eg, city) [Default City]:Makati
Organization Name (eg, company) [Default Company Ltd]:Rivancorp
Organizational Unit Name (eg, section) []:Head Quarters
Common Name (eg, your name or your server's hostname) []: Rivan Corporation Cybersecurity Institute
Email Address []:admin@rivancorp.com


Include -subj information so that no prompts appear:

!@NetOps
-subj "/C=PH/ST=NCR/L=Makati/O=Rivancorp/OU=HQ/CN=rivan.com/emailAddress=admin@rivancorp.com/subjectAltName=DNS:rivan.com,DNS:www.rivan.com,IP:192.168.102.100,DNS:software.rivan.com"


Display Certificate Info

!@NetOps
openssl x509 -in ca-rivan.pem -noout -text



4. Generate RSA Key Pair on both routers.

!@VPN-PH, VPN-JP
conf t
 crypto key generate rsa general-keys label rivankeys modulus 2048 exportable
 end



5. Create a trustpoint and import the CA.

!@VPN-PH
conf t
 crypto pki trustpoint rivantrust
  enrollment terminal pem
  hash sha512
  subject-name CN=siteph.rivan.com, C=PH, ST=NCR, L=Makati, O=Rivancorp, OU=SitePH, E=siteph@rivancorp.com
  subject-alt-name siteph.rivan.com
  subject-alt-name ph.rivan.com
  storage nvram: 
  primary
  revocation-check none
  rsakeypair rivankeys
  exit
 crypto pki authenticate rivantrust
> Paste the CA


!@VPN-JP
conf t
 crypto pki trustpoint rivantrust
  enrollment terminal pem
  hash sha512
  subject-name CN=siteph.rivan.com, C=JP, ST=Kanto, L=Tokyo, O=Rivancorp, OU=SiteJP, E=sitejp@rivancorp.com
  subject-alt-name sitejp.rivan.com
  subject-alt-name jp.rivan.com
  storage nvram: 
  primary
  revocation-check none
  rsakeypair rivankeys
  exit
 crypto pki authenticate rivantrust
> Paste the CA



6. Generate a CSR for both Routers

!@VPN-PH, VPN-JP
crypto pki enroll rivantrust

> Outputs a CSR . Must be signed by the CA



7. Import the CSR to the CA Server (NetOps)

!@NetOps
nano req-ph.pem
> paste VPN-PH's CSR
> ctrl + s (save)
> ctrl + x (exit)


!@NetOps
nano req-jp.pem
> paste VPN-JP's CSR
> ctrl + s (save)
> ctrl + x (exit



8. Sign the CSRs

!@NetOps
openssl x509 -req -in req-ph.pem -CA ca-rivan.pem -CAkey key-rivan.pem -out signed-ph.pem
openssl x509 -req -in req-jp.pem -CA ca-rivan.pem -CAkey key-rivan.pem -out signed-jp.pem

include subject names:
-subj "/C=PH/ST=NCR/L=Makati/O=Rivancorp/OU=SitePH/CN=Rivan Corporation PH/emailAddress=siteph@rivancorp.com/subjectAltName=DNS:siteph.rivan.com,DNS:ph.rivan.com,IP:208.8.8.11"
-subj "/C=JP/ST=Kanto/L=Tokyo/O=Rivancorp/OU=SiteJP/CN=Rivan Corporation PH/emailAddress=sitejp@rivancorp.com/subjectAltName=DNS:sitejp.rivan.com,DNS:jp.rivan.com,IP:208.8.8.12"
 
!@NetOps - obtain the signed CSRs
cat signed-rivansitea.pem
cat signed-rivansiteb.pem


6. Import the signed CSRs

!@VPN-PH, VPN-JP
conf t
 crypto pki import rivantrust certificate

> Paste the signed CSR

7. Verify existing certificates.

!@VPN-PH, VPN-JP
show crypto pki certificates

_____________________
********************* Configure GRE over IPSec via Certificate Authentication

1. GRE Tunnel

!@VPN-PH
conf t
 int tun1
  ip add 172.16.10.1 255.255.255.0
  tunnel source g1
  tunnel destination 208.8.8.12
  tunnel mode gre ip
  end

!@VPN-JP
conf t
 int tun1
  ip add 172.16.10.2 255.255.255.0
  tunnel source g1
  tunnel destination 208.8.8.11
  tunnel mode gre ip
  end


2. Routing Interesting traffic

!@VPN-PH
conf t
 ip route 20.20.20.48 255.255.255.248 172.16.10.2
 end
 
!@VPN-JP
conf t
 ip route 10.10.10.32 255.255.255.224 172.16.10.1
 end


3. Configure ISAKMP Policy

!@VPN-PH, VPN-JP
conf t
 crypto isakmp policy 1
  authentication rsa-sig
  encryption aes 256
  hash sha512
  group 14
  end


4. Configure IPSec Profile

!@VPN-PH, VPN-JP
conf t
 crypto ipsec transform-set IPSECTUNNEL esp-aes 256 esp-sha-hmac
  mode transport
  exit
 crypto ipsec profile RIVAN
  set transform-set IPSECTUNNEL
  set pfs group14
  end


5 Apply IPSec Profile Protection to Tunnel

!@VPN-PH, VPN-JP
conf t
 int tunnel 1
  tunnel protection ipsec profile RIVAN 
  end


_____________________
********************* Verification

!@VPN-PH, VPN-JP
show crypto isakmp sa
show crypto ipsec sa













Other

crypto isakmp key secretkey address 133.33.33.2



________________
****************
13. SSH Keygen Public key Authentication

@Linux
ssh-keygen -t rsa -b 2048 -f mine
fold -b -w 72 /home/ubuntu/.ssh/id_rsa.pub


3. Create a User with public key-chain.
@Cisco
conf t
 username aerin privilege 15
 ip ssh pubkey-chain
  username aerin
   key-string
    <PASTE PUB KEY>
	exit
   end


4. Disable Password authentication.

@Cisco
conf t
 ip ssh server algorithm authentication publickey
 no ip ssh server algorithm authentication password
 no ip ssh server algorithm authentication keyboard
 end



