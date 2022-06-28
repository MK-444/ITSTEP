numbers = [1, -3, 5, 2, -5, -4, 4, 3, 7, 9, 6, -8, ]
zaporne_cisla = 0
cetnoje_cislo = 0
necetnoje_cislo = 0

for i in numbers:
    if i < 0:
        zaporne_cisla += i
    elif i % 2 == 0:
        cetnoje_cislo += i
    elif i % 2 != 0 :
        necetnoje_cislo += i
print(" Suma Zaporne cisla: " + str(zaporne_cisla)   + "\n Suma Cetnych cisel: " + str(cetnoje_cislo) + "\n Suma Necitnych cisel: " + str(necetnoje_cislo))


jevseznamu = 0
seznam = []
cislo = input("Napis cisla: ")
hledane_cislo = int(input("Napis hledane cislo: "))
seznam.append(cislo)
for i in seznam:
    if i == hledane_cislo:
        jevseznamu += int(i)
        print(jevseznamu)
    else:
        print("Error")




variable = []
num_list = int(input("Write numbers: "))
variable.append(num_list)
variable.reverse()
print(variable)


