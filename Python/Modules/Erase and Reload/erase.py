import multiprocessing
from netmiko import ConnectHandler

def eraseDevices(monitor):
    device_order = ['coretaas', 'cucm', 'corebaba', 'edge']
    device_info = {
        'device_type': 'cisco_ios_telnet',
        'host': f'10.{monitor}.1.2',
        'username': 'admin',
        'password': 'pass',
        'secret': 'pass',
        'port': 23
    }
    
    for device in device_order:
        if device == 'coretaas':
            device_info['host'] = f'10.{monitor}.1.2'
        elif device == 'cucm':
            device_info['host'] = f'10.{monitor}.100.8'
        elif device == 'corebaba':
            device_info['host'] = f'10.{monitor}.1.4'
        elif device == 'edge':
            device_info['host'] = f'200.0.0.{monitor}'
            
        access_cli = ConnectHandler(**device_info)
        access_cli.enable()
        
        print(f'Accessing {device_info["host"]}... ')
        
        output = access_cli.send_command_timing('write erase')
        if 'Continue?' in output:
            output += access_cli.send_command_timing('\n')
        
        if device == 'coretaas' or device == 'corebaba':
            output += access_cli.send_command_timing('delete vlan.dat')
            if '[vlan.dat]?' in output:
                output += access_cli.send_command_timing('\n')
                if 'flash:vlan.dat?' in output:
                    output += access_cli.send_command_timing('\n')
                    
        output = access_cli.send_command_timing('reload')
        if 'Save?' in output:
            output += access_cli.send_command_timing('No')
        if 'Proceed with reload?' in output:
            output += access_cli.send_command_timing('\n')
        
        print(f'{device_info['host']}: {output}')
        
        access_cli.disconnect()
        print(f'\n\n Closing connection to {device_info['host']} \n')
    

if __name__ == '__main__':
    last_m = input('Your Monitor Number: ')
    list_of_monitors = ['11', '12', '21', '22', '31', '32', '41', '42', '51', 
                    '52', '61', '62', '71', '72', '81', '82', '91', '92', '13']
    
    list_of_monitors.remove(last_m)
    process_list = []
    
    for _m in list_of_monitors:
        proc = multiprocessing.Process(target=eraseDevices, args=[_m])
        process_list.append(proc)
    
    for i in process_list:
        i.start()
    
    for i in process_list:
        i.join()
    
    input('All devices have been erased. (Press ENTER to also erase configs on your devices.)')
    
    eraseDevices(last_m)
