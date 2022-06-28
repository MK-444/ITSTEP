"""
sirka = input("Zadej sirsku obdelnika:")
sirka = int(sirka)

vyska = int(input("Zadej vyska obdelnika:"))

obsah = sirka * vyska
print("Obsah obdelnika je", obsah)
"""

cislo = int(input("Zadej trojciferne cislo:"))
cifra1 = cislo // 100
cifra3 = cislo % 10
cifra2 = (cislo - (cifra1 * 100)) // 10 
print("", cifra1, cifra2, cifra3,
    cifra1 + cifra2 + cifra3, sep="\n\t\t")