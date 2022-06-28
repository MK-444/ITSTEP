"""
Úkol na NumPy a matplotlib:

1.) Vytvořte šest polí čísel.Všechny čísla od jedné do dvaceti, 
pak ta samá čísla, ale o jedna větší, pak o dva větší, pak o tři větší,
o čtyři větší a o pět větší.
(Pokud nechcete pracovat s NumPy, můžou to být i pytonovské listy.)

2.) Vytvořte graf v matplotlibu. Ukažte na něm všech šest polí čísel pod sebou.
Odlište je barvou, stylem čáry, vyzkoušejte různou šířku čáry. 
Nastavte grafu titulek, popis osy X a Y. Titulku a popiskům nastavte
velikost fontu a barvu. Nasvtavte velikost popisků na osách.
Nastavte jednotlivým čarám popisky a zobrazte legendu.

3.) Najděte si (třeba na w3schools), jak nastavovat nějaké z věcí 
z předchozího bodu. Např. styl čáry se dá nastavit celým slovem i zkratkou
a i jeho hodnoty mají celá slova nebo zkratky. 
Najděte si pár zkratek a vyzkoušejte je.

4.) (Volitelné, spíše pro zábavu.) 
Projděte si barevné mapy v dokumentaci matplotlibu a některé z nich použijte
v kódu, co jsme dělali na hodině.
"""

import matplotlib.pyplot as plt
import numpy as np 


pole1 = np.array(1)
pole2 = np.arange(1,4)
pole3 = np.arange(1,7)
pole4 = np.arange(1,11)
pole5 = np.arange(1,16)
pole6 = np.arange(1,22)

print(pole1)
print(pole2)
print(pole3)
print(pole4)
print(pole5)
print(pole6)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 4),facecolor='#1CC4AF')

ax.plot(pole1, color='tab:blue')
ax.plot(pole2, color='tab:orange')
ax.plot(pole3,)
ax.plot(pole4)
ax.plot(pole5)
ax.plot(pole6)
ax.set_title("Graf", fontsize=30)

ax.set_ylabel("Vysledek", fontsize=25)
ax.set_xlabel("Cislo", fontsize=25)

plt.show()
