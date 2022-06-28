import matplotlib.pyplot as plt 


druhe_mocniny = [1, 4, 9, 16, 25]
treti_mocniny = [1, 8, 27, 64, 125]

#STATEFUL

print(plt.style.available)
plt.style.use("dark_background")

plt.subplot(1, 2, 1)

plt.plot(druhe_mocniny)

plt.title("Graf druhych mocnin")

plt.subplot(1, 2, 2)

plt.plot(treti_mocniny)
plt.title("Graf tretich mocnin")

plt.show()