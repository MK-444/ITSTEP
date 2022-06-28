napoj = input("Co rad pijes") 
penezenka = 10
if vek >= 18:
    print ("Slvele, pojd tovnitr")
    print("vitame te tu")
    if not napoj == "pivo:
        print("Ty nepijes pivo? Fakt???")
    if napoj == "pivo":
        print("Mame to tu druhy piva")
        print("Kosyel, Radegast a Plzen")
        print("Ktere pivo si das")
        if pivo == "Kozel":
            print("Pochutnej si na Kozlovi")
            penezenka = penezenka - 5
        elif pivo == "Redegast":
            penezenka = penezenka - 6
        elif pivo == "Plzen":
                penezenka = penezenka - 8
    else:
        print("Co jineho si das? Vino, rum?")
elif vek >= 15:
    print("Pojd dovnitr, mame tu tri druhy limonady")
elif vek >= 10:
        print("Pojd dovnitr, mame tu skvele ovocny dzus")
else: 
    print("bohuyel to pro tebe nic nemame")

if ((vek >= 20) and (vek <= 25)) or ((vek >= 40) and (vek <= 45)):
    print("Mam pro tebe specialni nabidku")
if vek >= 60 or vek <= 10:
    print("Mame tu neco pro deti a starsi lidi")
print("Konec programu")