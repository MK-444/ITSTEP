"""
zvetseny_o_pet = []
for cislo in seznam:
    zvetseny_o_pet.append(cislo + 5)
    
print(zvetseny_o_pet)
zvetseny_o_pet_pomoc_comprehension = [cislo + 5 for cislo in seznam]
"""
seznam = [2,4,5,6,7]
druhe_mocniny = []
for cislo in seznam:
    if cislo % 2 == 0:
        druhe_mocniny.append(cislo ** 2)
print(druhe_mocniny)    


druhe_mocniny_pomoci_comprehension = [
    cislo ** 2
    for cislo in seznam
    if cislo % 2 == 0
]
print(druhe_mocniny_pomoci_comprehension)



seznam = ["ahoj", "ovoce", "zelenina", "brambory"]
sernam_pismen = []
for slovo in seznam2:
    for pismenko in slovo:
        seznam_pismen.append(pismenko)
print(seznam_pismen)

set_pismen_pomoci_compreshension = {
    pismeno 
    for slovo in seznam2 
    for pismeno in slovo
}
print(srt_pismen_pomoci_compreshension)
#set comprehension

#dict comprehension
slovnik_pomoci_comprehension = {
    cislo : cislo ** 2
    for cislo in seznam
}
print(slovnik_pomoci_comprehension)


