#DICTIONARY - slovnik

anglictina = {
    "apple": "jablko",
    "car": "auto",
    "book": "kniha",
    "table": "stul",
    "flower": "kvetina"
}

maruv_slovnik = {
    "jmeno":"Maria",
    "vek": 16,
    "oblibena barva": "zluta",
    "vyska": 160,
    "pije_rada_pivo": F
}

slovnik = {
    "klic": "hodnota"
}

pavluv_seznam = ["Pavel", 35, "zluta", 180, True]
pavluv_seznam[1]

maruv_slovnik["sport"] = "fotbal"
del pavlu_slovnik
maruv_slovnik["oblibena barva"] = 'cervena'
jidlo in pavluv_slovnik
"sport" not in pavluv_slovnik
jidlo not in pavluv_slovnik

"""
from pprint import pprint
import pprint(anglictina)"""

for klic in maruv_slovnik.keys():
    print(klic)


for hodnota in maruv_slovnik.values():
    print(hodnota)
    
klice = maruv_slovnik.keys()
hodnoty = maruv_slovnik.values()
dvojce = maruv_slovnik.items()

for klic in maruv_slovnik.keys():
    print(klic)

for hodnota in maruv_slovnik.values():
    print(hodnota)

for klic, hodnota = maruv_slovnik.items():
    print(klic, hodnota)

for index, items in enumerate(seznam):
    print(dvojce),
    print(inde, "---", item)
for dvojce  in maruv_slovnik.items():
    print(dvojce)
for klic, hodnota in pavluv_slovnik.items():
    print("klic" je, klic, "a hodnota je", hodnota)
    
slovnik = {}
seznam = []
retezec = ""