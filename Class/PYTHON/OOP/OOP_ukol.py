"""
1.)
Nadefinujte třídu Motor. Motor má typ a výkon. 
Nadefinujte třídu Auto. Auto má značku a motor.
Jako motor se používá instance třídy motor.
Motor i auto se umí hezky vypisovat.
Vytvořte několik instancí třídy auto a několik instancí třídy motor.
Nějaké motory uložte do proměnných, nějaké vytvořte přímo při vytváření aut.
Zkuste změnit typ motoru tak, že si na něj sáhnete ne přímo, ale přes auto, 
které ho používá.

2.)
Vytvořte třídu Kniha.
Kniha má jméno, autora a rok vydání.
Vytvořte třídu PoliceNaKnihy. Do police se vejde neomezené množství knih.
Vytvořte ve třídě metodu na přidávání knih (ať je nemusíte přidávat přímo.)
Zařiďte, ať se Kniha i PoliceNaKnihy hezky vypisuje.
Vytvořte několik instancí knih, aspoň jednu instanci PoliceNaKnihy a 
několik knih do ní uložte.
"""
print()
#1)

class Motor:
    def __init__(self, type:str, power:int):
        self.type = type
        self.power = power
        
    def __str__(self):
        return f"{self.type}{self.power}"
    
benzin = Motor("Benzin", 100)
diesel = Motor("Diesel", 200)


class Car:
    def __init__(self, mark:str, model:str, motor:Motor):
        self.mark = mark
        self.model = model
        self.motor = motor
        
    def __str__(self):
        return f"Znacka auta {self.mark} model auta {self.model} motor ma {self.motor.type} a vykon {self.motor.power}"
    
mercedes = Car("Mercedes","C-class", benzin)
skoda = Car("Skoda","Fabia", diesel)

print(mercedes)
print(skoda)
mercedes = Car("hunday","nevim", Motor("diesel", 50))
print(mercedes)
mercedes.motor.type = "elektro"
print(mercedes)

#2)*******************************************
print()
class Book:
    def __init__(self, name:str, author:str, year:int):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"Autor je {self.author}. Nazev knihy je {self.name}. Vydana v roce {self.year}"

first_book = Book("prvni_jmeno","prvni_nazev",2005)
second_book = Book("druhy_jmeno","druhy_nazev",2009)
third_book = Book("treti_jmeno","treti_nazev",1997)

class PoliceNaKnihy:
    def __init__(self):
        self.books = []

    def insert_books(self, book):
        self.books.append(book)

    def __str__(self):
        str_with_text = ""
        if len(self.books) == 0:
            return None
        for text in self.books:
            str_with_text += str(text)
            str_with_text += ".\n"
        return str_with_text
        


my_book = PoliceNaKnihy()

my_book.insert_books(first_book)
my_book.insert_books(second_book)
my_book.insert_books(third_book)

print(my_book)



"""
1.) Vytvořte třídu člověk. Člověk má jméno a věk. 
Třída člověk si pamatuje (pomocí třídní proměnné), kolik lidí už bylo vytvořeno.

2.) Vytvořte několik lidí a vypište (pomocí třídní proměnné), kolik lidí už bylo vytvořeno.

3.) Vypisovat třídní proměnnou sice umíte a jde to, ale nemusí to být v každém případě
úplně ideální postup. Vypište počet vytvořených lidí pomocí metody přímo ve třídě člověk.
Zkuste použít běžnou instanční metodu (ta se na to příliš nehodí, ale stejně si to zkuste), 
dále zkuste statickou metodu a třídní metodu. Jaké jsou mezi nimi rozdíly?

4.) Otázky z TEORIE:
a) Jak se liší statická a třídní metoda, vzhledem k počtu parametrů?
b) K čemu je dobrý parametr "cls" ve třídní metodě?
c) Na co se odkazuji pomocí "self.__class__"?

Příště budeme brát: DĚDIČNOST

Přehled (to neřešte, to je pro mě):
OOP 1 - úvod - metody __init__, __str__, rozdíl mezi třídou a instancí, rozdíl mezi atributem a
proměnnou, metodou a funkcí
OOP 2 - kompozice objektů
OOP 3 - statika (třídní proměnné, @staticmethod, @classmethod)
OOP 4 - dědičnost
OOP 5 - velký úkol
"""

print()
class Human:
    peoples = 0
    def __init__(self, name:str, year:int):
        self.name = name
        self.year = year
        self.__class__.peoples +=1
    
    def __str__(self):
        return f"Jmenuju se {self.name}, je {self.year} let."

    @classmethod 
    def count_peoples(group):
            print(f"Skupina ze {group.peoples} lidi")
    
    @staticmethod 
    def count_peoples_2():
        print(f"Skupina ze {__class__.peoples} lidi")

first_human = Human("Maria", 17)
second_human = Human("Max", 24)
third_human = Human("Nika", 5)


Human.count_peoples()
Human.count_peoples_2()
print(first_human, second_human, third_human, sep="\n")


"""
4.) Otázky z TEORIE:
a) Jak se liší statická a třídní metoda, vzhledem k počtu parametrů?
Ze staticka metoda neprijima zadny parametr a tridni ma aspon jeden parametr "cls"
b) K čemu je dobrý parametr "cls" ve třídní metodě?
Ze ukazuje primo na class - cls. Nezalezi jak se jmenuje trida primo na nej ukazuje 
c) Na co se odkazuji pomocí "self.__class__"?
Okdazuje se primo na tridu ve ktere se nachazi eventualnim odkaz.
napr:
class Human:
    pocet = 0
        def__init__(self,neco_neco):
        self.neco = neco_neco
        pocet +=1
class vypis:
    def _neco:
        return f"{__class__.self.pocet}"
    jestli zmenime jmeno class tak styjne vytiskne to co potrebuje , at kterekoliv bude jmeno
"""

