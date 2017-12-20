"""
ejemplo de llamadas
"""
from urllib import request

def load_url(url):
    req = request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    with request.urlopen(req) as response:
        return response.read()
    

url = load_url ('https://google.com')
print(url)

"""
req = request.Request(url)
with request.urlopen(req) as response:
    web = response.read()
    print(web)
"""