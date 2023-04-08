#!/bin/bash

# ASCII banner text
echo -e "\033[33m
 _____ _   _ _____ _____     _____ _____ ____  
|   __| | | |   __|   __|___|   __|_   _|    \ 
|   __| |_| |   __|__   |___|__   | | | |  |  |
|__|  |_____|_____|_____|   |_____| |_| |____/ 
\033[0m"

# Check if URL input is provided
if [ $# -eq 0 ]; then
    echo "No URL input provided. Please enter a valid URL."
    exit 1
fi

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    echo "curl could not be found. Please install curl to use this script."
    exit 1
fi

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "jq could not be found. Please install jq to use this script."
    exit 1
fi

# Check for SSRF vulnerability using curl and jq
echo "Scanning for SSRF vulnerability in $1 ..."
curl -s -o /dev/null -w "%{http_code}\n" "$1" \
    -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" \
    -H "Referer: $1" \
    -H "X-Forwarded-For: 127.0.0.1" | jq -e '. as $raw | try (input | fromjson) catch empty | select(.ip == $raw)' > /dev/null

if [ $? -eq 0 ]; then
    echo "SSRF vulnerability detected in $1"
else
    echo "No SSRF vulnerability detected in $1"
fi
