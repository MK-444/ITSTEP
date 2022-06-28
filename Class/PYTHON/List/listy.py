"""
seznam = [1, 7, 4, -5, 7, 1, -5, -9, -3, 8, 15] #globalni

print(seznam[5])
print(len(seznam))
print(max(seznam))


vysledek = 0
for cislo in seznam:
    if cislo > 0:
        vysledek += cislo

print(vysledek)



def vyber_pouze_kladna_cisla(seznam): #localni 
    novy_seznam = []
    for cislo in seznam:
        if cislo > 0:
            novy_seznam.append(cislo)
    return novy_seznam

def vyber_pouze_suda_cisla(seznam):
    novy_seznam = []
    for cislo in seznam:
        if cislo % 2 == 0:
            novy_seznam.append(cislo)
    return novy_seznam

print(vyber_pouze_kladna_cisla(seznam))
print(vyber_pouze_suda_cisla(seznam))
print(vyber_pouze_kladna_cisla(vyber_pouze_suda_cisla(seznam)))


def calculate(seznam):
    new_list = []
    twice_list = 0
    for i in seznam:
        if i > 0:
            new_list.append(i)
            twice_list += i
    return twice_list

print(calculate(seznam))

"""
num_list = [6,4,6,2,8,9]

def faktorial(num_list):
    list_faktorial = []
    for i in range(len(num_list)):
        if i <= 1:
            return 1
        else:
            vysledek = i * faktorial(i-1)
        list_faktorial.append(vysledek)
    return list_faktorial
print(faktorial(num_list))

'''
new_list = [ 0, 1, 5, 4, -3, ]

def search_num(new_list):
    for i in num_list:
        if i > 0:
            print(i)
print(search_num(new_list))
'''


def faktorial(cislo):
    if cislo <= 1:
        return 1
    return cislo * faktorial(cislo - 1)
print(faktorial(6))