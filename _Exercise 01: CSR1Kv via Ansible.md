
## Requirements
1. CSR1000v
2. Linux with Ansible (NetOps or NetOps-Lite)

<br>
<br>

---
&nbsp;

## Setup CSR1000v
### 1. Open CSR OVA File
Double-click the `csr1000v-universalk9.17.03.01a (VOIP Features).ova` __[01]__

<br>

![csr_01](</img/00 autocsr-01.png>)

&nbsp;
---
&nbsp;

### 2. Import Virtual Machine
Add a name `DEVEDGE` __[02]__, then select `Next>` __[03]__

<br>

![csr_02](</img/00 autocsr-02.png>)

&nbsp;
---
&nbsp;

### 2. Deployment Options
Leave as default, select `Next>` __[04]__

<br>

![csr_03](</img/00 autocsr-03.png>)

&nbsp;
---
&nbsp;

### 3. Bootstrap Properties
Leave as default, select `Import` __[05]__

<br>

![csr_04](</img/00 autocsr-04.png>)

&nbsp;
---
&nbsp;

### 4. VM Network Connectivity
While the VM is booting, select the `LANCARDs` __[06]__, any of the three.

<br>

![csr_05](</img/00 autocsr-05.png>)

&nbsp;
---
&nbsp;

### 5. VMNets
Assign the following `VMNets` __[07]__ to the Virtual Machine

| NetAdapter        | VMNet  |
| ---               | ---    |
| Network Adapter   | NAT    |
| Network Adapter 2 | VMNet2 |
| Network Adapter 3 | VMNet3 |

<br>

Then, confirm by selecting `OK` __[08]__

<br>

![csr_06](</img/00 autocsr-06.png>)

<br>
<br>

---
&nbsp;

## Setup NetOps
### 1. Open NetOps OVA File
Double-click the `NetOps.ovf` __[09]__

<br>

![csr_07](</img/00 autocsr-07.png>)

&nbsp;
---
&nbsp;

### 2. Import Virtual Machine
Name the Virtual Machine, `NetOps` __[10]__

<br>

![csr_08](</img/00 autocsr-08.png>)

&nbsp;
---
&nbsp;

### 3. Edit VM Settings
Select `Edit Virtual Machine Settings` __[11]__

<br>

![csr_09](</img/00 autocsr-09.png>)

&nbsp;
---
&nbsp;

### 4. Modify Network Adapters
Assign the following `VMNets` __[12]__ to the Virtual Machine

| NetAdapter        | VMNet     |
| ---               | ---       |
| Network Adapter   | NAT       |
| Network Adapter 2 | VMNet2    |
| Network Adapter 3 | VMNet3    |
| Network Adapter 4 | Host-Only |

![csr_10](</img/00 autocsr-10.png>)

&nbsp;
---
&nbsp;

### 5. Network Adapter 2
Select `Network Adapter 2` __[13]__

<br>

![csr_11](</img/00 autocsr-11.png>)

&nbsp;
---
&nbsp;

### 6. Network Adapter 2 MAC Address
Select `Advanced...` __[14]__, then take note of the `MAC Address` __[15]__ assigned to the network adapter. Then, simply `Cancel` __[16]__ the window.

<br>

Then, simply click `OK` __[17]__

<br>

![csr_12](</img/00 autocsr-12.png>)

&nbsp;
---
&nbsp;

### 7. Identify Interface
Power on the NetOps VM
> Login: root
> Pass: C1sc0123

<br>

Once logged in, enter the command `ip -br link` Then identify which interface holds the MAC Address of VMNet2. In this example, it is `ens192`

<br>

![csr_13](</img/00 autocsr-13.png>)

&nbsp;
---
&nbsp;
