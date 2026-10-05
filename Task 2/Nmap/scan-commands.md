# ICMP Connectivity Test
ping -c 4 192.168.56.102

# Host Discovery / Ping Sweep
sudo nmap -sn 192.168.56.0/24

# TCP SYN Scan
sudo nmap -sS 192.168.56.102 -oN nmap-tcp-scan.txt

# TCP SYN + Service Version + OS Detection
sudo nmap -sS -sV -O 192.168.56.102 -oN nmap-comprehensive.txt

# UDP Top 100 Ports
sudo nmap -sU --top-ports 100 192.168.56.102 -oN nmap-udp-scan.txt

# Banner Grabbing
sudo nmap -sV --script banner -p 21,22,23,25,53,80,2121,3306,5432,6667,8180 192.168.56.102 -oN banner-grabbing.txt
