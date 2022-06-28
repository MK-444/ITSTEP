"""
from time import sleep 
seconds = 0
while True:
    try:
        seconds += 1
        print(f"Uz to bylo {seconds} sekund.")
        sleep(1)
    except KeyboardInterrupt:
        #reaguje Ctrl + C
        print("ha ha ha ha ha - tenhle program nejde ukoncit!!")

try:
    delenec = int(input("Zadej prvni cislo: "))
    delitel = int(input("Zadej druhe cislo: ")) 
    vysledek = delenec / delitel
    print(f"Vysledek je {vysledek}") 
except ZeroDivisionError:
    print("Nelze delit nulou")
except ValueError:
    print("Nelze prevest na cislo")
except:
    print("Vznikla neznama chyba")
print("Program uspesne skolncil")


seznam = [1,5,6,8,1,2,3,9,4,5,6]
try:
    print(seznam[50])
except IndexError as promenna:
    print(f"Vznikla chyba, popis chyby zde: {promenna}")
    
"""



cislo = 5 * 6
cislo += 10
cislo *= 2
assert cislo == 80
try:
    assert cislo == 70
except AssertionError:
    print("Cislo neni stejne jako 70")
print("Vse v poradku")



