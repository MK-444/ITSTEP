menu = {
    "olivje": 100,
    "borsh": 40,
    "pureshka": 20,
    "kotleta": 12,
    "odbevnaja": 24,
    "pelmeni": 125,
    "manka": 46
}
menu["kasa"] = 20
menu["sok"] = 15
menu["moloko"] = 5


del menu["sok"]


menu["manka"] = 30



def foods(menu):
    food = menu.keys()
    print (food)
foods(menu)

def foods_and_price(menu):
    list_menu = menu.items()
    print(list_menu)
foods_and_price(menu)

ucet = 0
def objednavka(menu):
    global ucet
    objednaci_jidlo = input("Co chcete objednat? ")
    if objednaci_jidlo in menu:
        for jidlo, cena in menu.items():
            if jidlo == objednaci_jidlo:
                print("Vase objednavka: ", jidlo, "stoji", cena, "Kč")
                ucet += cena
                print("Vase ucet je ", ucet)
                objednavka(menu)
    elif objednaci_jidlo not in menu:
        print("Omlouvame se, tohle jidlo nemame")
    else:
        exit()

objednavka(menu)




weather = {}
output = 0
def weatherGenerator():
    global output
    inputMesto = input("Mesto: ")
    inputdest = input("Dest: " )
    if inputMesto != '':
        for mesto, dest in weather.items():
                if inputMesto == mesto:
                    dest += inputdest
                    print(weather)
        weather[inputMesto] = inputdest
        
        weatherGenerator()
    else:
        print(weather.items())
weatherGenerator()

muj_oblibeny_list = [(1,2), (3,7), (9, 5),(5,6)]
soucet = 0
for a, b in muj_oblibeny_list:
    soucet += a * b
print(soucet)


