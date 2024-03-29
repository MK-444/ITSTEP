"""
Dnes je to spíš inspirace na úkoly:

CSV:
1.) Vytvořte si csv soubor (nebo si nějaký někde vygooglete) a přečtěte z něj data pomocí modulu CSV. Můžete použít obě možnosti, které jsme probírali.

2.) Data pak můžete zapsat do jiného souboru. Můžete zkusit jiný oddělovač (třeba | místo čárky).

3.) Co znamenají parametry quotechar, escapechar a quoting používané v csv? Jaký význam mají konstanty csv.QUOTE_ALL, csv.QUOTE_MINIMAL,
csv.QUOTE_NONNUMERIC a csv.QUOTE_NONE a jak se používají?

JSON:
1.) Vytvořte slovník, ktrý má různé typy dat. Zapište ho jako json do souboru a také do stringu. Jaké dvě metody použijete? Jak se liší? Co znamená parametr indent?
Co znamená parametr separators? A co sort_keys?

2.) Přečtěte json uložený v souboru z minulého bodu. Přečtěte json uložený ve stringu z minulého bodu. Změnila se nějaká data? Jaká a jak se změnila?

API:
1.) Prohlédněte si SWAPI na adrese https://swapi.dev/. Zkuste do něj poslat dotaz na třetí planetu vyskytující se ve filmech a pak dotaz na první postavu.
Získaná data nějak zpracujte a prohlédněte si je. Vypište, jaké má třetí planeta podnebí a terén. Vypište, jaké kosmické lodě první postava používá.

Odkazy:
https://realpython.com/python-csv/
https://realpython.com/python-json/
https://realpython.com/python-requests/

Obecně o API:
https://realpython.com/api-integration-in-python/
https://www.itnetwork.cz/javascript/nodejs/rest-api-soap-graph-a-json

"""


import requests
import csv
import json
from pprint import pprint 



link = (f"https://swapi.dev/api/")
planets_path = "planets/3"
people_path = "people/1"

planets_url = link + planets_path
people_url = link + people_path

response_planets= requests.get(planets_url)
response_people = requests.get(people_url)

planets_json = response_planets.json()
people_json = response_people.json()

pprint(f"Planety jsou:\n{planets_json}")
print()
pprint(f"Lide jsou:\n{people_json}")



# with open("ukol.json", "w", newline="") as file:
#     json.dump(response.text, file, indent=4)