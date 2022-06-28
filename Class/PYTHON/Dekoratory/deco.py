import functools 


def muj_dekorator(fce):
    @functools.wraps(fce)
    def wrapper(*args, **kwargs):
        print("Tohle se stane pred funkce - obal")
        vysledek = fce(*args, **kwargs)
        print("Tohla se stane po funkci - obal")
        return vysledek 
    return wrapper
    
@muj_dekorator
def pozdrav(jmeno, prijmeni, vek):
    """tohle je funkce, ktera umi pozdravit"""
    print(f"ahoj {jmeno}{prijmeni}, jak se mas, dnes ti je {vek} let")
    return 42
    
#pozdrav = muj_dekorator(pozdrav)

cislo = pozdrav("Honza", "Novotny", vek=29)
print(cislo)

for i in range(3):
    print()

def udelej_dvakrat(fce):
    @functools.wraps(fce)
    def dvakrat_wrapper(*args, **kwargs):
        fce(*args, **kwargs)
        vysledek = fce(*args, **kwargs)
        return vysledek
    return dvakrat_wrapper

@udelej_dvakrat
def stekej():
    print("haf haf haf haf")
    print("konce stekani")
    print()
    
#stekej = udelej_dvakrat(stekej)
stekej()


"""
priklady na dekoratory, co jsme uz brali:

@login_required
@staticmethod
@classmethod

"""