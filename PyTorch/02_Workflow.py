import torch
from torch import nn # torch.nn zawiera wszystko do budowania sieci neuronowych
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

print(torch.__version__)
# 2.1.2+cu121

print('\n-------------------------------------------------------------------------------')
print('.......................  stworzenie danych wszystkich')
weight = 0.7
bias = 0.3
start  = 0
end = 1
step = 0.02

X = torch.arange(start, end, step).unsqueeze(dim = 1) # stworzenie tablicy danych i poszerzenie wymiaru o 1
y = weight * X + bias # obliczenie danych wyjściowych

# print(X[:10]) wyświetl pierwsze 10 elementów
print(X[:10], X.shape, len(X), '\n', 
      y[:10], y.shape, len(y), '\n')

print('....................... rozdzielenie danych do uczenia i danych do testowania')
train_split = int(0.8 * len(X)) # obliczenie 80% z długości tensora X
print(train_split)
# 40
X_train, y_train = X[:train_split], y[:train_split] # stworzenie tensorów do nauki
#print(X_train, y_train)
X_test, y_test = X[train_split:], y[train_split:] # stworzenie tensorów do testu
#print(X_test, y_test)
