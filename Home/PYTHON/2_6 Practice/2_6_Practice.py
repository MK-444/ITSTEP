#1 First task:
# Print the multiplication table for the user-defined number.
# If the user typed in 7, the output should be as follows:
#7 * 1 = 7
#7 * 2 = 14
#7 * 3 = 21 :


print("Hello this a programm is as a multiplication table")
a = int(input("Enter the number of a table:"))

for i in range (1,10):
    i*=a
    print(i)


#2 Second task:
# Write a currency converter program. Implement a dialog
# with the user through a menu:
"""
print("Hello this is the currency converter.")

numb = int(input("Please enter a value:"))
print("You have your value in:",
        "Dollars == $",
        "Euro == EURO",
        "Funt == FUNT",
        "UA == UA",
        "Rub == RUB",
        "Kc == KC", sep="\n")
currency = input("You have a:").upper()
#print("You have:", str(numb) +" "+ currency)
print("We can change your value in:",
        "Dollars == $",
        "Euro == EURO",
        "Funt == FUNT",
        "UA == UA",
        "Rub == RUB",
        "Kc == KC", sep="\n")
conv = input("Enter in which currency you want to convent:").upper()

if conv == "$":
    if currency == "EURO":
        print("Convert in: $")
        numb *= 1.13
        print(numb)
    elif currency == "FUNT":
        print("Convert in: $")
        numb *=1.33
        print(numb)
    elif currency == "UA":
        print("Convert in: $")
        numb*=0.04
        print(numb)
    elif currency == "RUB":
        print("Convert in: $")
        numb*=0.01
        print(numb)
    elif currency == "KC":
        print("Convert in: $")
        numb*=0.04
        print(numb)
elif conv == "EURO":
    if currency == "$":
        print("Convert in: EURO")
        numb*=0.88
        print(numb)
    elif currency == "FUNT":
        print("Convert in: EURO")
        numb*=1.19
        print(numb)
    elif currency == "UA":
        print("Convert in: EURO")
        numb*=0.03
        print(numb)
    elif currency == "RUB":
        print("Convert in: EURO")
        numb*=0.01
        print(numb)
    elif currency == "KC":
        print("Convert in: EURO")
        numb*=0.04
        print(numb)
elif conv == "FUNT":
    if currency == "EURO":
        print("Convert in: FUNT")
        numb*=0.84
        print(numb)
    elif currency == "$":
        print("Convert in: FUNT")
        numb*=0.74
        print(numb)
    elif currency == "UA":
        print("Convert in: FUNT")
        numb*=0.03
        print(numb)
    elif currency == "RUB":
        print("Convert in: FUNT")
        numb*=0.01
        print(numb)
    elif currency == "KC":
        print("Convert in: FUNT")
        numb*=0.03
        print(numb)
elif conv == "UA":
    if currency == "EURO":
        print("Convert in: UA")
        numb*=30.84
        print(numb)
    elif currency == "FUNT":
        print("Convert in: UA")
        numb*=36.62
        print(numb)
    elif currency == "$":
        print("Convert in: UA")
        numb*=27.27
        print(numb)
    elif currency == "RUB":
        print("Convert in: UA")
        numb*=0.37
        print(numb)
    elif currency == "KC":
        print("Convert in: UA")
        numb*=1.23
        print(numb)
elif conv == "RUB":
    if currency == "EURO":
        print("Convert in: RUB")
        numb*=83.16
        print(numb)
    elif currency == "FUNT":
        print("Convert in: RUB")
        numb*=98.73
        print(numb)
    elif currency == "UA":
        print("Convert in: RUB")
        numb*=2.7
        print(numb)
    elif currency == "$":
        print("Convert in: RUB")
        numb*=73.54
        print(numb)
    elif currency == "KC":
        print("Convert in: RUB")
        numb*=3.32
        print(numb)
elif conv == "KC":
    if currency == "EURO":
        print("Convert in: KC")
        numb*=25.08
        print(numb)
    elif currency == "FUNT":
        print("Convert in: KC")
        numb*=29.77
        print(numb)
    elif currency == "UA":
        print("Convert in: KC")
        numb*=0.81
        print(numb)
    elif currency == "RUB":
        print("Convert in: KC")
        numb*=0.3
        print(numb)
    elif currency == "$":
        print("Convert in: KC")
        numb*=22.17
        print(numb)
else:
    print("Please write correct value")

print("End of programm")

"""

Amount = float(input("Amount: "))
currency = {
"1": "USD",
"2": "EUR",
"3": "CZK"}
From = int(input("From:\n 1: USD\n 2: EUR - Euro\n 3: CZK - Czech Koruna\n Please, write number: "))
To = int(input("To:\n 1: USD - US Dollar\n 2: EUR - Euro\n 3: CZK - Czech Koruna\n Please, write number: "))
one_from_USD_to_EUR = 0.88323372
one_from_USD_to_CZK = 22.180505
one_from_EUR_to_USD = 1.132094
one_from_EUR_to_CZK = 25.108611
one_from_CZK_to_USD = 0.045080582
one_from_CZK_to_EUR = 0.039825225
if From == 1 and To == 2:
    answer = Amount * one_from_USD_to_EUR
    print(str(Amount)+" "+currency["1"]+" = "+str(answer)+" "+currency["2"])
elif From == 1 and To == 3:
    answer = Amount * one_from_USD_to_CZK
    print(str(Amount)+" "+currency["1"]+" = "+str(answer)+" "+currency["3"])
elif From == 2 and To == 1:
    answer = Amount * one_from_EUR_to_USD
    print(str(Amount)+" "+currency["2"]+ " = " +str(answer)+" "+currency["1"])
elif From == 2 and To == 3:
    answer = Amount * one_from_EUR_to_CZK
    print(str(Amount)+ " " +currency["2"]+" = "+str(answer)+ " " +currency["3"])
elif From == 3 and To == 1:
    answer = Amount * one_from_CZK_to_USD
    print(str(Amount)+ " " +currency["3"]+ " = " +str(answer)+ " " +currency["1"])
elif From == 3 and To == 2:
    answer = Amount * one_from_CZK_to_EUR
    print(str(Amount)+ " " +currency["3"]+ " = " +str(answer)+ " " +currency["2"])
    
    
    

import random
cislo = random.randint(1, 50)
while True:
    tip = int(input("Hadej jake si myslim cislo: "))
    if tip == 0:
        print("Cislo je", cislo)
        print("Konec programu")
        break
    elif tip == cislo:
        print("uhodl jsi!!!")
        break
    elif tip < cislo:
        print("Hledane cislo je vetsi")
    else:
        assert tip > cislo
        print("Hledame cislo je mensi")
    