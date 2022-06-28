def say():
    print("Ahoj host")
    print("Host, Jak se mas")
say()
say()

def say(jmeno):
    print("Ahoj", jmeno)
    print(jmeno, "Jak se mas")
say("Host")
say("Maria")


def calculate(num1, num2):
    print( num1 * num2)
calculate(3,4)
calculate(5,5)


def calculate(num1, num2):
    return num1 * num2

ans = calculate(8,7)
ans2 = calculate(5,6)
print(ans * ans2)



def calculate(num1, num2, operaci):
        return num1, operaci, num2
calculate(1, 3, "+")
calculate(1, 3, "-")
calculate(1, 3, "*")



def calculate(num1, num2, operaci, kontinue):
    num1 = int(input("Prvni cislo: "))
    num2 = int(input("Druhe cislo: "))
    operaci = str(input("Napiste cislo 1-scitani, 2-odcitani, 3-nasobeni: "))
    if operaci == '1':
        print(num1 + num2)
    elif operaci == '2':
        print( num1 - num2)
    else:
        assert operaci == '3'
        print( num1 * num2)
    kontinue = int(input("Pokracovat? 1 - ano, 0 - ne: "))
    if kontinue == 0:
        return
    elif kontinue == 1:
        return num1, num2, operaci
    print(kontinue)
    
calculate(num1, num2, operaci, kontinue)



