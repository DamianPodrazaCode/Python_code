import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generator	Class implementing all of the random number distributions https://en.wikipedia.org/wiki/Normal_distribution
np.random.seed(42)
x = np.random.randn(1000)


fig, ax = plt.subplots()
ax.hist(x)


plt.show()