input("input number 1")
input("input number 2")
input("input number 3")
x = input("+ it 1 or - it 2")
if "+":
    x == 1
else "-":
    x == 2
#=============================

num = input("input metr")
choose = {1: "mily", 2:"dujmy", 3:"jrd"}
mily = 0.0006213711922373 
dujmy = 39.37007874016
jrd = 1.093613298338
if choose == 1:
    num *= mily
elif choose == 2:
    num *= dujmy
else choose == 3:
    num *= jrd
print(num)
#=============================

def mult(num):
    y = 0
    while y <= 10:
        ans = num * y
        print(str(num) + " * " + str(y) + " = " + str(ans))
        y += 1
    mult(num = int(input("number is")))
#=============================

Amount = float(input("Amount: "))
currency = {"1": "USD",
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
    print(str(Amount)+" "+currency["2"]+" = "+str(answer)+" "+currency["1"])
elif From == 2 and To == 3:
    answer = Amount * one_from_EUR_to_CZK
    print(str(Amount)+" "+currency["2"]+" = "+str(answer)+" "+currency["3"])
elif From == 3 and To == 1:
    answer = Amount * one_from_CZK_to_USD
    print(str(Amount)+" "+currency["3"]+" = "+str(answer)+" "+currency["1"])
elif From == 3 and To == 2:
    answer = Amount * one_from_CZK_to_EUR
    print(str(Amount)+" "+currency["3"]+" = "+str(answer)+" "+currency["2"])
#=============================

x = int(input("number: ")) 
y = int(input("number: ")) 
result = 1 
while y:
    result *= x 
    y -= 1 
print(result) 
#=============================

input("input number 1")
input("input number 2")
input("input number 3")
x = input("+ it 1 or - it 2")
if "+":
    x == 1
else "-":
    x == 2
num = input("input metr")
choose = {1: "mily", 2:"dujmy", 3:"jrd"}
mily = 0.0006213711922373 
dujmy = 39.37007874016
jrd = 1.093613298338
if choose == 1:
    num *= mily
elif choose == 2:
    num *= dujmy
else choose == 3:
    num *= jrd
print(num)
#=============================

def mult(num):
    y = 0
    while y <= 10:
        ans = num * y
        print(str(num) + " * " + str(y) + " = " + str(ans))
        y += 1
    mult(num = int(input("number is")))
#=============================  

Amount = float(input("Amount: "))
currency = {"1": "USD",
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
    print(str(Amount)+" "+currency["2"]+" = "+str(answer)+" "+currency["1"])
elif From == 2 and To == 3:
    answer = Amount * one_from_EUR_to_CZK
    print(str(Amount)+" "+currency["2"]+" = "+str(answer)+" "+currency["3"])
elif From == 3 and To == 1:
    answer = Amount * one_from_CZK_to_USD
    print(str(Amount)+" "+currency["3"]+" = "+str(answer)+" "+currency["1"])
elif From == 3 and To == 2:
    answer = Amount * one_from_CZK_to_EUR
    print(str(Amount)+" "+currency["3"]+" = "+str(answer)+" "+currency["2"])
#=============================  

x = int(input("number: ")) 
y = int(input("number: ")) 
result = 1 
while y:
    result *= x 
    y -= 1 
print(result) 

#module 3 practic 1
number1 = input("number is: ")
for i in number1:
    print(i) 
#=============================  

number1 = input("number is: ")
for i in (number1):
    print(i)
print(number1[-1] + number1[0])