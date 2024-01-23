import torch
from torch import nn 

import numpy as np

tab = np.genfromtxt('dl.csv', delimiter=',')

START_WINDOW = 0 # start okna
STEP = 10 # ilość wierszy z tabeli do okna

window = np.array(tab[START_WINDOW:START_WINDOW+STEP])
window = window.reshape(1, STEP * 6)
X = window
# print(X, X.shape, '\n')
out = np.array(tab[START_WINDOW+STEP])
y = out.reshape(1, 6)
# print(y, y.shape, '\n')

while START_WINDOW < (tab.shape[0]-STEP-1):
    START_WINDOW = START_WINDOW + 1
    window = np.array(tab[START_WINDOW:START_WINDOW+STEP])
    window = window.reshape(1, STEP * 6)
    X = np.append(X, window, axis=0)
    out = np.array(tab[START_WINDOW+STEP])
    out = out.reshape(1, 6)
    y = np.append(y, out, axis=0)
    print(tab.shape[0] - START_WINDOW - STEP)

print(X, X.shape)
print(y, y.shape)
