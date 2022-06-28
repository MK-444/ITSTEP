


class DomaciZvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        
    def __str__(self):
        return f"Jmeno je {self.jmeno}"
    
    def vydej_zvuk(self):
        pass
    
    
class Pes(DomaciZvire):
    def __init__(self, jmeno, rasa):
        super().__init__(jmeno)
        self.rasa = rasa 
        
    def vydej_zvuk(self):
        print("haf haf haf")
        
    def prinesi_mic(self):
        print("prinesu mic")
        
        
class Kocka(DomaciZvire):
    def __init__(self, jmeno, oblibene_jidlo):
        super().__init__(jmeno)
        self.oblibene_jidlo = oblibene_jidlo 
        
    def vydej_zvuk(self):
        print("mijau mijau")
        
    def skrabej (self):
        print("neskrabej!")
        



class Slepice(DomaciZvire):
    def __init__(self, jmeno, barva):
        super().__init__(jmeno)
        self.barva = barva 
        
    def vydej_zvuk(self):
        print("hu hu hu")
        
    def ji_banany(self):
        print("dej mi banan")
        
        
nika = Pes("Nika", "francouzsky buldocek")
matroskin = Kocka("Matroskin", "ryba")
maja = Slepice("Maja", "hneda")


seznam = [nika, matroskin, maja]

for zvire in seznam:
    zvire.vydej_zvuk()
    
nika.prinesi_mic()
matroskin.skrabej()
maja.ji_banany()

