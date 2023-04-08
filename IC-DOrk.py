print("""
 _   _ _____ _     _____ ____   ____ ____      _    ____ _____ _____ ____  
| \ | | ____| |   | ____|  _ \ / ___|  _ \    / \  / ___|_   _| ____|  _ \ 
|  \| |  _| | |   |  _| | |_) | |   | |_) |  / _ \| |     | | |  _| | |_) |
| |\  | |___| |___| |___|  __/| |___|  _ <  / ___ \ |___  | | | |___|  _ < 
|_| \_|_____|_____|_____|_|    \____|_| \_\/_/   \_\____| |_| |_____|_| \_\ 
                                                                             
""")
import requests
from bs4 import BeautifulSoup

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a')
    urls = []
    for link in links:
        try:
            url = link['href']
            if url.startswith('/url?q='):
                urls.append(url[7:url.index('&sa=U&')])
        except:
            continue
    return urls

query = input("Enter your search query: ")
results = search_google(query)
print("Search Results:\n")
for url in results:
    print(url)
