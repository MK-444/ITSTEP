"""Začněte posledním úkolem z minulé hodiny. 

1.) Prohlédněte si APíčko o psech na adrese https://thedogapi.com/.
Zkuste do něj poslat dotaz na všechna plemena psů. Získaná data zpracujte.

Pro další krok si (kvůli přehlednosti) můžete nechat jen prvních deset
položek listu (tj. prvních deset plemen).

2.) Vytvořte nový list a pro každé plemeno tam uložte jen jeho jméno, temperament
a výšku a váhu v metrických jednotkách.

3.) List můžete nějak hezky vytisknout.

4.) Na adrese https://github.com/public-apis/public-apis si najděte 
nějaké apíčko na téma, které vás zajímá. Pošlete si do něj requesty,
zpracujte je a data hezky vytiskněte.

5.) Něco z teorie - Jak se jmenuje HTTP metoda, co odpovídá operaci CREATE?
Jak se jmenuje metoda, která odpovídá operace DELETE? A metoda, která odpovídá
operaci UPDATE? Jaká je poslední metoda a jaké odpovídá operaci?

6.) Jaký status kód má číslo 301? Do jaké patří skupiny?
A jaké číslo má status kód "Unsupported Media Type"? A dp jaké patří skupiny?"""


from textwrap import indent
import requests
import json
import csv 
import json


base_url = "https://api.thedogapi.com/"
endpoint = "v1/breeds"

url = base_url + endpoint
response = requests.get(url)

result = response.json()
for breed in result:
    print("Plemeno: ", end="")
    print(breed["name"])
    print("Vyska: ", end="")
    print(breed["height"])
    if "width" in breed:
        print("Sirka: ", end="")
        wbreed = breed.json()
        print(wbreed["width"])




"""
5)
create = POST 
delete = DELETE
update = PUT, PATCH
read = GET
CRUD = create, read, update, delete

6)
301 Moved Permanently Trvale přesunuto se používá pro trvalé přesměrování, což znamená, že odkazy nebo záznamy vracející tuto odpověď by měly být aktualizovány.
HTTP 415 
"""








