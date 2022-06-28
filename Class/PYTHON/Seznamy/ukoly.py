import numbers



seznam = [1,2,3,4,5,6]


druhe_mocniny = (
    cislo **2 
    for cislo in seznam
)
print(druhe_mocniny)
suma = sum(druhe_mocniny)
#suma2 = sum(druhe_mocniny)

print(f"Suma je {suma}")
#print(f"Suma je {suma2}")
suma = sum((
    cislo ** 2
    for cislo in seznam
))
#generator expression
#vedle list compresion mame jeste 
#jsou dobre v tom, ze setri pamet
print(f"Suma je {suma}")
#seznam_stringu = []
#for cislo in seznam:
    #seznam_stringu = [str(cislo) for cislo in seznam]
    #seznam_stringu.append(str(cislo))
#novy_seznam = ",".join(seznam_stringu)
#print(novy_seznam)

print(f"Suma je {suma}")


retezec = "10 abc 20 de44 30 55fg 40"
def secti_cisla(ret):
    #soucet = 0
    #for neco in retezec.split():
        #if neco.isdigit():
            #soucet += int(neco)
    return sum([
                int(neco)
                for neco in ret.split()
                if neco.isdigit()
                ])

print(secti_cisla(retezec))

secti_cisla(retezec)


cislo = "dddd"
def funkce(i):
    for i in cislo:
        print(i+"a")

funkce(cislo)

# def funkce2(data, data2, data3):
#     #data = "dffs"
#     data2 = "fdsafs"
#     data3 = "adfdfda"
#     print("ahoj")
#     print("slon")
#     print(data+4)
# funkce(cislo, 5,7)

#5 minutovka
seznam = [2, 7, 25, 9,10]
slovnik = {
    cislo:cislo ** 2
    for cislo in seznam
}
print(slovnik)


slovnik = {
    "jablko": "apple",
    "dvere": "door",
    "stul": "table",
    "slon": "elephant"
}

def otoc_slovnik(slv):
    return {
        hodnota: klic
        for klic, hodnota in slv.items()
    }
print(otoc_slovnik(slovnik))

slozity_seznam = [[1,2], [3,4,5]]
novy_seznam = []

for jednoduchy_seznam in slozity_seznam:
    for cislo in jednoduchy_seznam:
        novy_seznam.append(cislo)
print(novy_seznam)

def plochy_seznam(szn):
    return[
        cislo
        for jednoduchy_seznam in slozity_seznam
        for cislo in jednoduchy_seznam
    ]
slozity_seznam = [[1,2,5,6], [3,4,5,6]]
print(plochy_seznam(slozity_seznam))


    
    
seznam = [5,6,3,223,34,53,21]
seznam_stringu = []
for cislo in seznam:
    seznam_stringu.append(str(cislo))
novy_seznam = ",".join(seznam_stringu)
print(novy_seznam)


x,y = 10, 20
x, y = y,x

a = "Geegforgeeks"
print("Reverse is", a [::-1])

a = ["Geeks", "For", "Geeks"]
print(" ".join(a))

n = 10
result= 1 < n < 20
print(result)
result= 1> n <= 9


import os
import socket

def x():
    return 1,2,3,4
a,b,c,d = x()
print(a,b,c,d)

test = [1,2,3,4,1,2,3,4, 5,4,4]
print(max(set(test), key = test.count))

import sys
x = 1
print(sys.getsizeof(x))

from collections  import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


print(is_anagram('geek', 'eekg'))
print(is_anagram('geek', 'peek'))




