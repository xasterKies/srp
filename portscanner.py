import socket 



def scan(target, ports):
  for port in range(1, ports):
    scan_port(target, port)

def scan_port(ipaddress, port):
  try:
    sock = socket.socket() # Initiate the socket instance
    sock.connect((ipaddress, port)) # Connect to our target
    print("[+] Port Opened " + str(port))
    sock.close()
  except:
    print("[-] Port Closed " + str(port))

targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
  print("[*] Scanning Multiple Targets")
  for ip_addr in targets.split(','):
    scan(ip_addr.strip(' '), ports)
else:
  scan(targets, ports)

  
