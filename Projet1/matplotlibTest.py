# coding: utf-8

import matplotlib.pyplot as plt

plt.title("Danger de la vitesse")
plt.plot([50, 100, 150, 200], [1, 2, 3, 4])
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.axis([80, 180, 1, 10])
plt.show()
