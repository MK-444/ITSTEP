def pozdrav(jmeno):
    print("Ahoj.", jmeno)
    print(jmeno + ", Odloz si, satni je vlevo.")
    print("Pokracuj rovne, v hale je obcerstveni.")
    
# pozdrav("Pavle")
# pozdrav("Monika")
# pozdrav("Honzo")

def scitej(a, b):
    print("Scitam cisla", a, "a", b) 
    soucet = a + b
    return("Soucet je "+ str( soucet))
    
prvni_vysledek = scitej(56, 3)
print(scitej(5, 3))
print(scitej(5, 8))

def pozdrav(jmeno: str, jmeno2: int):
    print("ahoj")
    print(jmeno)
    print("pojd dal")
    print("odloz si, satna je vpravo")
    print(jmeno2)
    print("obcerstveni je za rohem vlevo ")
#funkci volam pomoci zavorek!!!
pozdrav("asfd", 56)
print("ahoj","afdfs", "dfd", sep="*", end="konec",)
#dva typy argumentu
#positional arguments = args
#keyword arguments = kwargs

def scitej(a,b,c):
    return a + b + c

def scitej(a,b,c):
    soucet = a + b + c
    if soucet == 5:
        return soucet
    print("chachacha")

vysledek = scitej(7,8,9)

novy_vysledek = scitej(vysledek, vysledek, vysledek)


def diskriminant(a, b, c):
    d = (b ** 2) - (4 * a * c)
    return d 
print(diskriminant(1,3,2))
    