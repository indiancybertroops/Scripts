#!/bin/bash

# Function to print ASCII banner
print_banner() {
    echo " _____   _____  ____  ____  _____ "
    echo "/  ___| /  ___|/ ___|/ ___||  ___|"
    echo "\`--.  \| \`--. \\\___ \\\___ \| |_   "
    echo " \`--. \/ \`--. \/ ___) |__) |  _|  "
    echo "/\__/ /\__/ / |____/|____/|_|    "
    echo "\____/ \____/  IC-Crap Website Scraper"
}

# Call the print_banner function to display ASCII banner
print_banner

# Get the URL input from user
read -p "Enter the URL of the website you want to scrape: " url

# Use curl to retrieve the website HTML and pipe it to grep to extract the text
curl -s $url | grep -o '<p>[^<]*</p>' | sed 's/<[^>]*>//g'

# End of script
