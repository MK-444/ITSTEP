anglictina = {
    "jablko": "apple",
    "dum": "house",
    "stul": "table".
    "kniha": "book",
    "dvere": "door"
}
print(anglictina["dum"])
anglictina["stul"] = "elephant"
anglictina["zidle"] = chair
preklad = input("jak slovicko chces prelozit")
print(anglictiva(preklad))
print(anglictina["j" + "a"])
print(anglictina["velbloud"])
if "velbloud" in anglictina:
print(anglictina["velbloud"])
else:
print("neni v slovniku")
print(anglictina.get("velbloud", "neni ve slovniku"))

print(anglictina.setdefault("velbloud" ,"camel"))
#kdyz to neni tak to vytvor

print(anglictina"[velbloud"])
for dvojce in anglictina.items():
print(dvojce)

for dvojce ing anglictina.items():
PRINT(index, value)



#tuple
seznam = ["Alik", "Rex", "Bert"]
ntice = ("Micka", "Liza", "Cubaka")
seznam[0]
ntice[0]
seznam[0] = "zly vlcek"
ntice[0] = "hodna koocicka"

#Listy lze zmenit - pridavat prvky, menit prvky, mazat, prvky - jsou tzv. Matable
# tu[menit nelze - nelze pridavat prvky, mazat ani prepisovat - jspi tzv. imutable]

#clice museji byt nemeni imutavle a hashable
seznam = {
    2: "dvojka",
    "s": "pismeno s",
    True: "boolean",
    (1,2,3): "seznam tei cisel",
    (1,2,3[4,5],7): "chyba"
}

muj_set = {1,234,5,235,35,35,35,3,533663}
#set nema dublikaty

muj_set.intersection(muj_set)
muj_set.union(muj_set)
muj_set.add()
muj_set.remove()
4 in muj_set
muj_set & muj_set3
ntice = (3,1,4)
ntice += (3,1,5)