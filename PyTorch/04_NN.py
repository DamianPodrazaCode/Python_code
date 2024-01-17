import sklearn
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
import torch
from torch import nn 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# Ustawienie urządzenia którego będzie używał PyTorch ('cpu', 'cuda')
device = "cuda" if torch.cuda.is_available() else "cpu"
# device = "cpu" # wymuszenie działania na procesorze
# print('Urządzenie którego będę używał:', device)

# zadaniem jest rozdzielenie dwóch okręgów zrobionych z punktów wymieszanych w jednej tablicy

# wygenerowanie danych dwóch okręgów w postaci punktów
n_samples = 1000
X, y = make_circles(n_samples, noise=0.03, random_state=42) 
# print(X, '\n', y)

# wizualizacja w postaci tabeli
# circles = pd.DataFrame({"X1": X[:, 0], "X2": X[:, 1], "label": y})
# print(circles.head(10))

#wizualizacja
plt.figure('Wszystkie dane')
plt.scatter(x=X[:, 0], y=X[:, 1], c=y, cmap=plt.cm.RdYlBu)
plt.show(block=False)
#plt.show(block=True)

# print(X.shape, y.shape)
# print(X[0, 0])

# dane do tensora
# print(type(X), X.dtype)
X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float)
# print(X, '\n', y)

# rozdzielenie danych w sposób random na uczenie i testy (from sklearn.model_selection import train_test_split)
X_train, X_test, y_train, y_test = train_test_split(X,  
                                                    y, 
                                                    test_size=0.2, # 0.2 - będzie 20% danych do testu, 80% do nauki
                                                    random_state=42) 

# wizualizacja
plt.figure('Dane uczenia')
plt.scatter(x=X_train[:, 0], y=X_train[:, 1], c=y_train, cmap=plt.cm.RdYlBu)
plt.show(block=False)
#plt.show(block=True)
plt.figure('Dane testowe')
plt.scatter(x=X_test[:, 0], y=X_test[:, 1], c=y_test, cmap=plt.cm.RdYlBu)
plt.show(block=False)
#plt.show(block=True)

#stworzenie klasy modelu i konfiguracja loss i optimizer
class CircleModelV0(nn.Module):
    def __init__(self):
        super().__init__()
        # tworzenie warstw sieci neuronowej 
        self.layer_1 = nn.Linear(in_features=2, out_features=5) # in_features=2 - wejście do sieci -> dwie dane wejściowe z X, out_features=5 ukryte dwie sieci
        self.layer_2 = nn.Linear(in_features=5, out_features=1) # in_features=5 - wejście z sieci ukrytej z poprzedniej warstwy, out_features=1 wyjście z odpowiedziami
    
    # metoda kalkulacji sieci neuronowej        
    def forward(self, x):
        return self.layer_2(self.layer_1(x)) # x wchodzi do warstwy 1, a warstwa 1 wchodzi do warstwy 2, z której wychodzą odpowiedzi
    
model_0 = CircleModelV0().to(device)

print(model_0)
# print(next(model_0.parameters()).device) # info z jakiego urządzenia korzysta instancja

# stworzenie instancji modelu w najprostrzy sposób, to jest to samo co klasa wyżej, 
# tylko w ten sposób dostaje się z automatu funkcje forward i nie można nic w niej zmienić
model_0 = nn.Sequential(
    nn.Linear(in_features=2, out_features=5),
    nn.Linear(in_features=5, out_features=1)
).to(device)

print(model_0)
