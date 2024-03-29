import matplotlib.pyplot as plt 
import numpy as np

druhe_mocniny = [1, 4, 9, 16, 25]
treti_mocniny = [1, 8, 27, 64, 125]
cisla = np.arange(1,6) #numpy pole
cisla2 = [1,2,3,4,5] #list se stejnum obsahem jako numpy pole

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(cisla, druhe_mocniny, linewidth=5, linestyle="dashed", color="orange", label="druha mocnina")
ax.plot(cisla, treti_mocniny, lw=6, c="b", ls=":", label="treti mocnina")
ax.set_title("Graf druhych a tretich mocnin", fontsize=25)

ax.set_ylabel("Vysledek", fontsize=20)
ax.set_xlabel("Cislo", fontsize=20)
ax.legend(loc='upper right')

ax.tick_params(axis="both", which="major", labelsize=20)
plt.show()
