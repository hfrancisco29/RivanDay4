import netmiko
from netmiko import ConnectHandler
import pprint as print
import json

### READ JSON FILE
with open('ph.json','r') as jfile:
    pfile = json.load(jfile)
    #print.pp(pfile)



### DEVICE INFO 
ph = {
    'device_type': 'cisco_ios',
    'host' : '192.168.102.11',
    'username': 'admin',
    'password': 'pass',
    'port': '22'
}


### COMMANDS
config = [
    f'interface {pfile['config']['type']} {pfile['config']['id']}',
    f'ip add {pfile['config']['ipv4']['ip']} {pfile['config']['ipv4']['mask']}',
    f'description {pfile['config']['desc']}',
    'end'
]


print.pp(config)

### CONNECT
cli = ConnectHandler(**ph) 
cli.enable() #SEND COMMAND ENABLE IN CLI

cli.send_config_set(config) #SEND "CONFIG" TO CLI

siib = cli.send_command('show ip int br') #CREATE FILE SIIB THAT CONTAIN THE CLI SEND COMMAND SH IP INT BR 

cli.disconnect()  # DISCONNECT TO TERMINAL

print.pp(siib)   # TO SHOW SHOW IP INT BR RESULTS