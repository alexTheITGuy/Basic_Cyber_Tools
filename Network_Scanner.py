from scapy.all import ARP, Ether, srp

print('Please enter a valid IP address with subnet. Example: 192.168.0.1/24')

#Destination IP 
target_ip = input()

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


