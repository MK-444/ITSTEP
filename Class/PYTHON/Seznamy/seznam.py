psi = ["Alik", "Rex", "Teyla", "Hugp", "Patrik"]

for index in range(len(psi)):
    print(index)
    print(psi[index])
    
for index, pes in enumerate(psi):
    print("Na indexu" + str(index) + "je ulozen pes" + pes)
    
pes1, pes2, pes3, pes4, pes5 = psi


seznam = ["Škoda", 2005, 1.3, "Fabia"]
typ, rok, objem, model = seznam

auta = [
        ["Škoda", 2005, 1.3, "Fabia"],
        ["Volkswagen", 2015, 1.9, "Passat"],
        ["Mercedes", 2010, 2.2, "S"],
        ["Ferrari", 2012, 4.0, "Formule"]
        ]
for auto in auta:
    typ, rok, objem, model = auto
    print(objem)
    print(typ, model, objem, rok)
    print(auto)
    
psi.append("Žeryk")
psi.append("Jerry")
psi.append("Vincent")
psi.remove("Hugo")
del psi[3]
psi.insert(4, "Hugo2")
psi.index("Rex")

