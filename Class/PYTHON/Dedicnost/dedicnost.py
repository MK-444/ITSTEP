class Clovek:
    """
    tohle je trida pro vytvareny lidi, budu ji pouzivat pro dedeni
    tohle je docstring, tedy dokumentacni retezec
    """
    def __init__(self, jmeno, vek):
        """init metoda, python ji vola sam"""
        self.jmeno = jmeno
        self.vek = vek 
        
    def __str__(self):
        return f"ja jsem {self.jmeno}"
    
    def pozdrav(self):
        """postavicka potka jinou postavicku a pozdravi ji"""
        print("Dobry den!")
        
    def spi(self):
        """postavicka vydava zvukz typicke pri spanku"""
        print("Chrrrrr")
        



class Programator(Clovek):
    
    def __init__(self, jmeno, vek=40, jazyk="Python"):
        jmeno = "Superman " + jmeno
        super().__init__(jmeno, vek + 5)
        self.jazyk = jazyk
    
    def pij_kafe(self):
        print("Mame u nas ve firme moc dore kafe")
        
    def pozdrav(self):
        super().pozdrav()
        print("Ahoj")
        
    def spi(self):
        print("Spim a zda se mi o objektech... OOP sny jsou super!")
        
    def __str__(self):
        return f"Jsem programator {self.jmeno} a nejradeji programuji v jazyku {self.jazyk}."
    
    
class Manazer(Clovek):
    def spi(self):
        print("Spim a zda se mi, ze rano vyhodim pulku zamestnancu.")
        
class Sportovec(Clovek):
    pass

    
        
erik = Programator("Erik", 35, "JavaScript")
pepa = Clovek("Josef", 18)
robert = Programator("Robert")
hugo = Manazer("Hugo", 50)
kyle = Sportovec("Kyle", 20)

seznam = [pepa, erik, robert, hugo, kyle]

for osoba in seznam:
    osoba.spi()




















# pepa.spi()
# pepa.pozdrav()
# print(pepa)

# erik.spi()
# erik.pozdrav()
# erik.pij_kafe()
# print(erik)
# print(erik.jmeno)
# print(erik.jazyk)

# print(robert.vek)
# print(robert)


#inheritance 
