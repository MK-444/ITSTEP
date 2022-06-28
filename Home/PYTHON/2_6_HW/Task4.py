cislo = input("Zadej cislo, odstranim trojku a sestku: ")
# for cislice in cislo:
#     if cislice != "3" and cislice != "6":
#         nove_cislo = nove_cislo + cislice
#     print(cislice)

for i in cislo:
    if i == "3" or i == "6":
        continue
    print(i, end="")