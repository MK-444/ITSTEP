slovnik = {
    "jmeno": "Pavel",
    "vek": 29,
    "sporty":['fotball', 'basketball', 'hokey'],
    "muz": False
}
slovnik["vyska"] = 176

hodnoty = slovnik.values()
print(hodnoty)

klice = slovnik.keys()
print(klice)

slovnik_items = slovnik.items()
print(slovnik.items())

for klic in slovnik.values():
    print(klic)
    
for klic in slovnik.keys():
    print(klic)
    
for klic, hodnota in slovnik.items():
    print(klic, hodnota)