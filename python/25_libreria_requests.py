"""
la libreia request simplifica mucho el
y respuestas http
"""

import requests

response = requests.get('https://httpbin.org/ip')
ip = response.json()['origin']
print('Tu IP es', ip)

response = requests.get('https://swapi.co/api/people/')
people = response.json()['results']

for person in people:
    print(person['name'])