import torch
from torch import nn
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from helper_functions import plot_decision_boundary

# ------------------------------------------------------------- Hiperparametry
RANDOM_SEED = 42
LEARNING_RATE = 0.1
EPOCHS = 100

START_WINDOW = 0 # start okna
STEP = 100 # ilość wierszy z tabeli do okna
# ------------------------------------------------------------- Ziarnistość random
torch.manual_seed(RANDOM_SEED)  
torch.cuda.manual_seed(RANDOM_SEED)

# ------------------------------------------------------------- Wybór urządzenia do obliczeń
device = "cuda" if torch.cuda.is_available() else "cpu"
#device = "cpu" # wymuszenie działania na procesorze

# ------------------------------------------------------------- Stworzenie lub wczytanie danych, oraz podzielenie ich na: do uczenia, do testu
# X - wejścia do sieci, y - wyjcie z sieci

tab = np.genfromtxt('dl.csv', delimiter=',')

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

# print(X, X.shape)
# print(y, y.shape)

X_train = torch.from_numpy(X).type(torch.float)
y_train = torch.from_numpy(y).type(torch.float)

# ------------------------------------------------------------- Ustawienie danych na urządzenie
X_train, y_train = X_train.to(device), y_train.to(device)

print(X_train, X_train.shape)
print(y_train, y_train.shape)

# ------------------------------------------------------------- Zdefiniowanie i stworzenie instancji modeluNN
modelNN = nn.Sequential(
    nn.Linear(in_features=STEP*6, out_features=1024),
    nn.ReLU(),
    nn.Linear(in_features=1024, out_features=1024),
    nn.ReLU(),
    nn.Linear(in_features=1024, out_features=6)
).to(device)

# ------------------------------------------------------------- Konfiguracja funkcji strat i optymalizacji
loss_fn = nn.CrossEntropyLoss()
#optimizer = torch.optim.SGD(params=modelNN.parameters(), lr=LEARNING_RATE)
optimizer = torch.optim.Adam(params=modelNN.parameters(), lr=LEARNING_RATE)

# ------------------------------------------------------------- Pętla uczenia i testu
epoch_count = []
loss_values = []

for epoch in range(EPOCHS):
    
    # uczenie
    modelNN.train()
    y_out = modelNN(X_train).squeeze()
    loss = loss_fn(y_out, y_train) 
    optimizer.zero_grad()
    loss.backward() 
    optimizer.step()

    y_pred = torch.softmax(y_out, dim=1) # (y_out, dim=1) oznacza weź z tablicy cały wymiar pierwszy
    y_pred_max = torch.argmax(y_pred, dim=1)
    
    epoch_count.append(epoch)
    loss_values.append(loss)
    
    print(EPOCHS - epoch)
    
# ------------------------------------------------------------- Wizualizacja po uczeniu
print(y_out[:5], '\n')
print(y_pred[:5], '\n')
print(y_pred_max, '\n')

plt.figure('Wizualizacja')
mngr = plt.get_current_fig_manager()
mngr.window.geometry("+0+0") 

plt.title("Straty.")
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")
plt.legend()

plt.show()
