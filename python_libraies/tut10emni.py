import numpy as np
import matplotlib.pyplot as plt

# Parameter t (angle)
t = np.linspace(0, 2 * np.pi, 1000)

# Parametric equations for a heart
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Plot
plt.figure(figsize=(6,6))
plt.plot(x, y, color="red")
plt.fill(x, y, color="red", alpha=0.6)  # fill inside
plt.title("❤️ Love Sign Graph")
plt.axis("equal")   # keep aspect ratio square
plt.show()

