#FIRST CLASS CITIZEN

def pozdrav(jmeno):
    print(f"Ahoj {jmeno}, jak se mas?")
    
hroch = pozdrav 

hroch()


def pozdrav_slusne(prijmeni):
    print(f"Dobry den pane/pani {prijmeni}, jak se mate?")
    
pozdravy = [pozdrav, pozdrav_slusne]

def funkce_co_zdravi(f, jmeno):
    return f(jmeno)
    
def pocasi(kod):
    def slunecno():
        print("Dnes je slunicko")
    
    def destivo():
        print("Dnes prsi")
        
    print("skoncila funkce pocasi")
    if kod == 1:
        return slunecno 
    else:
        return destivo
    
predpoved = pocasi(1)

predpoved()

