#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime
from pyfiglet import figlet_format
from termcolor import cprint
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty())

subprocess.call('clear', shell=True)
subprocess.call('clear', shell=True)
cprint(figlet_format('PortScanner', font='shadow'),
       'green', attrs=['bold'])
print(colored('Version 1.0                                        Made by Fsociety10\n', 'red'))

remoteHost = input(colored("\n\n\n\nEnter the Ip adress: ",'blue'))

print("_" * 60)
print(colored('[*] Please wait, scanning remote host {}'.format(remoteHost),'magenta'))

t1 = datetime.now()

try:
    for port in range(21,23):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((remoteHost,port))
        if result == 0:
            print(colored("[+] Port {}: Open".format(port), 'green'))
            sock.close()
except KeyboardInterrupt:
    print(colored("[-] Ctr+C was pressed. Exiting", 'red'))
    sys.exit()

except socket.gaierror:
    print(colored("[-] Could not resolve hostname. Exiting", 'red'))
    sys.exit()

except socket.error:
    print(colored("[-] Couldn't reach server. Exiting", 'red'))
    sys.exit()

t2 = datetime.now()
print(colored("[+] Scan started {}".format(t1), 'cyan'))
print(colored("[+] Scan ended {}".format(t2), 'cyan'))
