import socket 
import termcolor


def scan(target, ports):
  print(termcolor.colored(('\n' + ' Starting Scan For ' + str(target)), 'green'))
  for port in range(1, ports): # Loop through all number of entered ports
    scan_port(target, port)

def scan_port(ipaddress, port):
  try:
    sock = socket.socket() # Initiate the socket instance
    sock.connect((ipaddress, port)) # Connect to our target
    print("[+] Port Opened " + str(port))
    sock.close()
  except:
    pass

#--------------- Main Program entry -------------------
targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
  print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green')) # Color terminal highlighting
  for ip_addr in targets.split(','): # Split different target if any found
    scan(ip_addr.strip(' '), ports)
else:
  scan(targets, ports)

  
