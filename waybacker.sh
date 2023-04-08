#!/bin/bash

# Install jq if not installed
if ! command -v jq &> /dev/null
then
    echo "jq not found. Installing..."
    sudo apt-get install jq -y
fi

# Install curl if not installed
if ! command -v curl &> /dev/null
then
    echo "curl not found. Installing..."
    sudo apt-get install curl -y
fi

# Install figlet if not installed
if ! command -v figlet &> /dev/null
then
    echo "figlet not found. Installing..."
    sudo apt-get install figlet -y
fi

# Display the banner
figlet Waybacker

# Get user input
read -p "Enter the URL to search on Wayback Machine: " url

# Format the URL
url="http://web.archive.org/cdx/search/cdx?url=${url}/*&output=json&collapse=urlkey"

# Get the URLs from Wayback Machine and save them to output.txt
curl -s "$url" | jq -r '.[] | .[2]' > output.txt

# Echo the result
echo "URLs saved to output.txt:"
cat output.txt
