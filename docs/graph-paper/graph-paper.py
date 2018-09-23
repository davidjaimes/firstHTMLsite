# Author: David Jaimes
# Email: astro@davidjaimes.run
# Web: https://davidjaimes.run
# Date: 2017 Novermber 30
# Developed with Python 3.6.3 :: Anaconda custom (64-bit)
# Questions about the code? Feel free to contact me

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


plt.figure(figsize=(8.5, 11))
matplotlib.rc('axes', edgecolor='C7')

# default xmax=30 ymax=50; play with these numbers to get different spacing.
xmax = 30
ymax = 50

# numeric major ticks, list is used to leave out numbers
plt.xticks(np.arange(0, xmax + 1, 5), [], color='C7')
plt.yticks(np.arange(0, ymax + 1, 5), [], color='C7')
plt.tick_params(which='major', length=10, color='C7')
plt.grid(which="major", lw=1.5, ls="dashed")

# minor ticks marks
plt.gca().set_xticks(np.arange(0, xmax, 1), minor=True)
plt.gca().set_yticks(np.arange(0, ymax, 1), minor=True)
plt.tick_params(which='minor', length=5, color='C7')
plt.grid(which="minor", lw=0.5, ls="dashed")

# Final layout and saving figure made
plt.gca().xaxis.set_ticks_position("both")
plt.gca().yaxis.set_ticks_position("both")
plt.xlim(0, xmax)
plt.ylim(0, ymax)
plt.tight_layout()
plt.savefig("graph-paper.png", transparent=True, dpi=300)
