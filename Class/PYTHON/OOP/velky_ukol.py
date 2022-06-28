"""
Velký úkol na OOP:
Vytvořte třídu zvíře.
Zvíře má počet nohou, barvu a metodu vydej_zvuk
(metoda nebude nic dělat, obecné zvíře zvuk nevydává).
Vytvořte několik tříd na konkrétní zvířata.
Např. třída pes, kočka, nebo taky žirafa a slon.
Zajímavá je třída had - ten má 0 nohou.
Každá nová třída bude mít něco navíc (atribut nebo metodu), 
např. pes může mít atribut rasu nebo metodu hlidej_barak.
(Dohromady vytvořte aspoň jednu metodu a aspoň jeden atribut.)
Každý potomek zvířete zároveň přepíše (přetíží) metodu vydej_zvuk po svém 
(např. pes zaštěká).
Vytvořte několik instancí různých zvířat.
Vytvořte si seznam (list) a uložte do něj několik instancí různých zvířat.
Pak seznam projděte cyklem a nechte každé zvíře dát o sobě nahlas vědět 
(tedy vždy zavolejte metodu vydej_zvuk).
Dodělejte ke zvířatům metodu __str__ nebo __repr__, aby se hezky vypisovala.
Zamyslete se, jestli se hodí víc k předkovi Zvire nebo k potomkům.
Vytvořte třídu Klec.
Do klece se vejde několik zvířat.
Vytvořte metodu pridej_zvire na přidání zvířete do klece.
(Vsuvka pro velmi pokročilé - tohle jsme nedělali, ale můžete si to zkusit vygooglit:
Metoda pridej_zvire může mít víc parametrů (více různých zvířat) a přidá je všechny.)
Zařiďte, aby se hezky vypisovala včetně zvířat vevnitř (budeme to potřebovat později).
Můžete vytvořit několik instancí klecí a umístit do nich některé z už vytvořených zvířat.
Vytvořte třídu Zoo.
Do zoo se vejde několik klecí.
Vytvořte metodu pridej_klec na přidání klece do zoo.
(Vsuvka pro pokročilé: metoda pridej_klec umí přidat několik klecí najednou.)
Třída Zoo se umí hezky vypisovat (vypíše klece i zvířata v nich).
Vytvořte metodu vypis_podle_barvy, která projde celé zoo (všechny klece a zvířata v nich) a vypíše jen zvířata s určitou barvou (barvu dostane jako parametr).
Vytvořte metodu vypis_podle_nohou, která projde celé zoo (všechny klece a zvířata v nich) a vypíše jen zvířata s určitým počtem nohou (ten dostane jako parametr).
Do zoo přijel sponzor.
Chce všem zvířatům koupit ponožky.
Vytvořte metodu spocitej_nohy, která projde všechny klece a zvířata v nich a spočítá počet nohou v celé zoo.
Vytvořte instanci třídy Zoo a užijte si ji. 
Vytvořte instance zvířat (pokud je už nemáte), 
do klecí dejte zvířata a klece dejte do zoo.
Vypište si zvířata podle barev, podle počtu nohou a nezapomeňte spočítat počet ponožek pro sponzora!
"""



class Zvire:
    def __init__(self, jmeno, nohy, barva):
        self.jmeno = jmeno
        self.nohy = nohy
        self.barva = barva
        
    def __str__(self):
        return f"Jmenu je se {self.jmeno}, ma {self.nohy} nohy a {self.barva} barvu"
        
    def vydej_zvuk(self):
        raise Exception("Nevyda zvuk")
    


class Pes(Zvire):
    def __init__(self, jmeno, nohy, barva, rasa):
        super().__init__(jmeno, nohy, barva)
        self.rasa = rasa
        
    def vydej_zvuk(self):
        print("haf haf haf")

    def hlidej_barak(self):
        return f"Hlidam tvuj barak"
    
    def __str__(self):
        return f"Pes je {self.rasa} "
    
nika = Pes("Nika", 4, "cerna", "francuzsky buldocek")
volt = Pes("Volt", 4, "bilo-cerny", "staford")

print(nika)
print(volt.hlidej_barak())



class Kocka(Zvire):
    def __init__(self, jmeno,  nohy, barva, oblibene_jidlo):
        super().__init__(jmeno, nohy, barva)
        self.oblibene_jidlo = oblibene_jidlo

    def vydej_zvuk(self):
        return f"mijau mijau"
    
    def skrabej(self):
        print("neskrabej!")

    def __str__(self):
        return f"Kocka ma rada {self.oblibene_jidlo}"

matroskin = Kocka("Matroskin", 4,"cerno-bily","mleko")
murka = Kocka("Murka", 4, "zrzava", "maso")

print(matroskin)
print(murka)



class Zirafa(Zvire):
    def __init__(self, jmeno, nohy, barva, vyska):
        super().__init__(jmeno, nohy, barva)
        self.vyska = vyska

    def vydej_zvuk(self):
        return f"jsem zticha"
    
    def tanci(self):
        return f"Umim tancit breakdance"

    def __str__(self):
        return f"Zirafa je vysoka {self.vyska}"

tiffany = Zirafa("Tiffany", 4, "svetlo hneda",  "4m")
naomi = Zirafa("Naomi", 4, "tmavo hneda", "5m")


class Klec():
    def __init__(self):
        self.zvirata_v_klece = []

    def pridej_zvire(self, *args):
        for zvire in args:
            self.zvirata_v_klece.append(zvire)

    def __str__(self):
        return (', '.join(self.zvirata_v_klece))
        

klec_pro_psy = Klec()
klec_pro_kocky = Klec()
klec_pro_zirafy = Klec()

klec_pro_psy.pridej_zvire(nika.jmeno)
klec_pro_psy.pridej_zvire(volt.jmeno)
klec_pro_kocky.pridej_zvire(matroskin.jmeno)
klec_pro_kocky.pridej_zvire(murka.jmeno)
klec_pro_zirafy.pridej_zvire(tiffany.jmeno)
klec_pro_zirafy.pridej_zvire(naomi.jmeno)

print(f"Jsem klec pro psy a jsou ve me tito psy: {klec_pro_psy}.")
print(f"Jsem klec pro kocky a jsou ve me tito kocky: {klec_pro_kocky}.")
print(f"Jsem klec pro zirafy a jsou ve me tito zirafy: {klec_pro_zirafy}.")


class Zoo:
    def __init__(self):
        self.klece_v_zoo = [] 
        
    def pridej_klec(self, klec):
        self.klece_v_zoo.append(klec)        
        
    def zvire_podle_barvy(self, barva):
        neexistuje = True
        for klec in self.klece_v_zoo:
            for zvire in klec.zvirata:
                if zvire.barva == barva:
                    print(zvire)
                    neexistuje = False 
        if neexistuje:
            print("Neni takove zvire")



zvirata = [klec_pro_psy, klec_pro_kocky, klec_pro_zirafy]
muj_zoo = Zoo()
print(muj_zoo.pridej_klec(klecy))
print(muj_zoo)

# positional arguments = args
# keyword arguments = kwargs

