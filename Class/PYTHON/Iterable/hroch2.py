class Hroch:
    def __init__(self, jmeno, delka_ocasu):
        self.jmeno = jmeno 
        self.delka_ocasu = delka_ocasu
        
    def __len__(self):
        return self.delka_ocasu
    
    def __add__(self, other):
        print("Nekdo scita hrochy")
        return self
    
    def __mul__(self, other):
        self.delka_ocasu += 5
        other.delka_ocasu -= 10
        return self.delka_ocasu * other.delka_ocasu 
    
    def __iter__(self):
        self.vlastnosti = list(self.__dict__.keys())
        self.index = -1
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.vlastnosti):
            raise StopIteration
        return self.vlastnosti[self.index]
    
        
    def __str__(self):
        return f"Jsem {self.jmeno} a {self.delka_ocasu} cm dlouhy ocas."
    
adam = Hroch("Adam", 20)
borek = Hroch("Borek", 15)
cyril = Hroch("Cyril", 34)



print(len(adam))

print(adam + borek + cyril)

vysledek = adam * borek 

print(adam)

print(borek)

print(vysledek)

for x in adam:
    print(x)