# Python3
import requests
import json
import pyfiglet

# ASCII banner text
ascii_banner = pyfiglet.figlet_format("IC-Cript")
print(ascii_banner)

# API endpoint
api_url = 'https://api.wappalyzer.com/analyze/v1/'

# User input
url = input("Enter the URL to analyze: ")

# API request headers and payload
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-api-key': 'YOUR_API_KEY' # Replace with your Wappalyzer API key
}

payload = {
    'url': url,
    'html': '',
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
}

# Send API request and retrieve response
response = requests.post(api_url, headers=headers, data=json.dumps(payload))

# Process response
if response.ok:
    results = json.loads(response.text)
    print("Results for URL:", url)
    print("------------------------------------")
    for app in results['applications']:
        print(app['name'], "-", app['version'])
else:
    print("Error occurred while analyzing the URL:", response.text)
    
    #You can use alternative code to define api for easy use  change code @ api area:
    # Set the Wappalyzer API URL and API key
#api_url = "https://api.wappalyzer.com/analyze/v1/"
#api_key = "<your API key here>"
# Set the headers for the API request
#headers = {
    #"Content-Type": "application/json",
    #"X-Api-Key": api_key
#}

