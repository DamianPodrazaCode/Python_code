import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1,2,3,4,5]
y = [11,22,33,44,55]

# -----------------------------------------------------------------------------
# fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(10,10))

ax.plot(x, y)
ax.plot(x, [1,2,3,4,5])

ax.set(title="Simple Plot", xlabel='x-axis', ylabel='y-axis')

fig.savefig("Python_\sample-plt.png")
# -----------------------------------------------------------------------------
# print(type(fig), type(ax))
# <class 'matplotlib.figure.Figure'> <class 'matplotlib.axes._axes.Axes'>
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

plt.show()