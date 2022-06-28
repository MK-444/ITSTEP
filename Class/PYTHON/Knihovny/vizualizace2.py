import matplotlib.pyplot as plt
from prochazka import np



fig, ax = plt.subplots(figsize=(15,8))
ax.scatter(np.kroky_X, np.kroky_Y, s=100, c=list(range(len(np.kroky_Y))), cmap="viridis")
ax.plot(np.kroky_X, np.kroky_Y, ls="--", c="k")
ax.scatter(np.kroky_X[0], np.kroky_Y[0], s=800, c="red", label="start", edgecolors="k")
ax.scatter(np.kroky_X[-1], np.kroky_Y[-1], s=800, c="orange", label="konec", edgecolors="k")

ax.set_title("Nahodna prochazka", fontsize=50)
ax.legend()


plt.show()