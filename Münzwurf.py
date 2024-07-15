import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate_coin_flips(n):
    return np.random.choice(['Kopf', 'Zahl'], size=n)

def calculate_probabilities(flips):
    counts = {'Kopf': 0, 'Zahl': 0}
    probabilities = []
    for i, flip in enumerate(flips):
        counts[flip] += 1
        probabilities.append(counts['Kopf'] / (i + 1))
    return probabilities

def update(num, flips, line):
    probabilities = calculate_probabilities(flips[:num + 1])
    line.set_data(range(num + 1), probabilities)
    return line,

# Anzahl der Münzwürfe
n = 2000

# Münzwürfe simulieren
flips = simulate_coin_flips(n)

# Initialisierung der Plot-Daten
fig, ax = plt.subplots()
ax.set_xlim(0, n)
ax.set_ylim(0, 1)
ax.set_xlabel('Anzahl der Würfe')
ax.set_ylabel('Relative Häufigkeit von "Kopf"')
line, = ax.plot([], [], lw=2)

# Hinzufügen der theoretischen Wahrscheinlichkeit
ax.axhline(0.5, color='red', linestyle='--', label='Theoretische Wahrscheinlichkeit')
ax.legend()

# Animation
ani = animation.FuncAnimation(fig, update, frames=n, fargs=[flips, line], blit=True, interval=10, repeat=False)

# Animation speichern
# Als GIF speichern
from matplotlib.animation import PillowWriter
# Save the animation as an animated GIF
ani.save("animation1.gif", dpi=100,
         writer=PillowWriter(fps=50))

plt.show()
