import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.random.randn(1000)
nut_butter_prices = {'Almond butter': 10,
                     'Penaut butter': 8,
                     'Cashew butter': 12}

# ------------------------------------------------------------------------------------
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

ax1.plot(x, x/2)
ax2.scatter(np.random.random(10), np.random.random(10))
ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax4.hist(x)

# ------------------------------------------------------------------------------------
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

ax[0, 0].plot(x, x/2)
ax[0, 1].scatter(np.random.random(10), np.random.random(10))
ax[1, 0].bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax[1, 1].hist(x)

plt.show()