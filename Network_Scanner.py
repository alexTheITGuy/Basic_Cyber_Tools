from scapy.all import ARP, Ether, srp
import sys
import subprocess
import os
import ipaddress

print('Exit:                                                    0')
print('Network scanner (match MAC to IPv4 address):             1')
print('Get a list of all possible IPs based on network address: 2')
print('Ping an IPv4 address on the network:                     3')
print('===========================================================')

def Network_Scan():
    #Destination IP 
    target_ip = input('Enter a valid IP address with subnet in CIDR notation. Example: 192.168.16.0/24 ==> ')

    #Check to verify that IP address is valid
    if target_ip.count('.') != 3 or target_ip.count('/') != 1:
        print('IP not valid')
        Network_Scan()
    
    #Create arp packet 
    arp = ARP(pdst=target_ip)
    #Create broadcast MAC address packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    #stack them 
    packet = ether/arp

    #srp works at the data link lay (layer 2)
    result = srp(packet, timeout = 3)[0]

    # a list of clients, we will fill this in the upcoming loop
    clients = []

    for sent, received in result: 
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    #Print Clients
    print('Here are the devices in this network')
    print('IP' + " " * 18 + 'MAC')
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))

#This function gets a list of all IP's on a network based on the network address
def Get_IP_List():
    network_address = input("Enter your current IPv4 network address in CIDR notation (Example: 192.168.16.0/24) ==> ")
    all_ipv4 = ipaddress.ip_network(network_address)

    for host in all_ipv4.hosts():
        if not host.is_private:
            continue
        print(host)

#Used to ping IP address on the conected network
def Network_Ping():
    #Gets the current OS that the script is running on
    current_os = os.name
    ip_address = input('What IP address would you like to ping? ==> ')

    #If the current OS is Windows 
    if current_os == 'nt':
        output = subprocess.run(['ping', '-n', '4', ip_address])
    #If the current OS is Linux based
    else:
        output = subprocess.run(['ping', '-c', '4', ip_address])

action = int(input('Select an operation ==> '))

match action:
    case 0: 
        sys.exit()
    case 1: 
        Network_Scan()
    case 2:
        Get_IP_List()
    case 3:
        Network_Ping()
