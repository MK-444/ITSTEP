def func():
    return "“Don’t let the noise of others’ opinions drown out your own inner voice.” Steve Jobs"
func()



def line(length, direction, symbol):
    if direction == 'vertical':
        for n in range(length):
            print(symbol)
    elif direction == 'horizontal':
        for n in range(length):
            print(symbol, end='')
    else:
        print("error")



length = int(input("write number: "))
direction = input("write direction: ")
symbol = input("write symbol: ")
line(length, direction, symbol)





# Program to check if a number is prime or not

num = int(input("number: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num // i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    
    #lucky or not
def getSum(n):
    
    sum = 0
    for digit in str(n)[:3]: 
        sum += int(digit)
    sum2 = 0
    for digit2 in str(n)[3:]: 
        sum2 += int(digit2)
    if sum == sum2:
        print("lucky")
    else:
        print("not lucky")
    
n = 123422
print(getSum(n))



#faktorial
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
n=int(input("čislo : "))
print(faktorial(n))

