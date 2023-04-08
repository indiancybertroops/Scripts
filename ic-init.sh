#!/bin/bash

clear
echo ""
figlet  "IC-Domain"

echo ""
echo "Enter the domain name:"
read domain

echo ""
echo "Searching for information on $domain..."

# Get WHOIS information
echo ""
echo "WHOIS information:"
whois $domain | grep -E 'Registrant:|Registrar:|Name Server:|DNSSEC:|Updated Date:|Creation Date:|Expiration Date:'

# Get DNS information
echo ""
echo "DNS information:"
nslookup -type=NS $domain | grep -E 'nameserver'

# Get IP address information
echo ""
echo "IP address information:"
ping -c 1 $domain | head -n1 | cut -d' ' -f3 | tr -d '()'
