# one 

# def odd_num(start, stop):
#     for i in range(start, stop):
#         if i % 2  == 1:
#             numbs = i
#     return numbs
        
# print(odd_num(5, 10))

def line(length, direction, symbol):
    s = length * symbol
    if direction == "vertical":
        for i in range(s):
            print(i)
        
length = int(input("Write number: "))
derection = input("Horizontal or vertical?: ")
symbol = input("Symbol: ")
print(line(length, direction, symbol))





def max_num(a, b, c, d):
    if (a >= b) and (a >= c) and (a >= d):
        largest = a
    elif (b >= a) and (b >= c) and (b >= d):
        largest = b
    elif (c >= a) and (c >= b) and (c >= d):
        largest = c
    else:
        largest = d
    return largest

a = int(input("prvni cislo: "))
b = int(input("druhe cislo: "))
c = int(input("treti cislo: "))
d = int(input("ctvrte cislo: "))
print(max_num(a, b, c, d))



