import requests 
import json
from pprint import pprint 


response = requests.get("https://swapi.dev/api/")

print(response.text)
#result = json.loads(response.text)
# print(result)
# print(type(result))

vysledek = response.json()

pprint(vysledek["planets"])

response2 = requests.get("https://swapi.dev/api/planets/")
vysledek2 = response2.json()
pprint(vysledek2)
print(response2.status_code)
