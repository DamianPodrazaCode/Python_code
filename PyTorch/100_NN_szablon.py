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

# ------------------------------------------------------------- Ziarnistość random
torch.manual_seed(RANDOM_SEED)  
torch.cuda.manual_seed(RANDOM_SEED)

# ------------------------------------------------------------- Wybór urządzenia do obliczeń
device = "cuda" if torch.cuda.is_available() else "cpu"
#device = "cpu" # wymuszenie działania na procesorze

# ------------------------------------------------------------- Stworzenie lub wczytanie danych, oraz podzielenie ich na: do uczenia, do testu
# X - wejścia do sieci, y - wyjcie z sieci

# rozdzielenie na dane uczenia i testu (test_size=0.3 to 30% testu i 70% uczenia)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_SEED) 

# ------------------------------------------------------------- Ustawienie danych na urządzenie
X_train, y_train = X_train.to(device), y_train.to(device)
X_test, y_test = X_test.to(device), y_test.to(device)

# ------------------------------------------------------------- Zdefiniowanie i stworzenie instancji modeluNN
modelNN = nn.Sequential(
    nn.Linear(in_features=2, out_features=128),
    nn.ReLU(),
    nn.Linear(in_features=128, out_features=128),
    nn.ReLU(),
    nn.Linear(in_features=128, out_features=1)
).to(device)

# ------------------------------------------------------------- Konfiguracja funkcji strat i optymalizacji
loss_fn = 
optimizer = torch.optim.SGD(params=modelNN.parameters(), lr=LEARNING_RATE)

# ------------------------------------------------------------- Wizualizacja przed uczeniem
modelNN.eval()
with torch.inference_mode():
    test_out = modelNN(X_test)
    test_pred = 
        
plt.figure('Wizualizacja', figsize=(12, 12))
plt.subplots_adjust(left=0.05, bottom=0.05, top=0.95, right=0.95) # dociągnięcie wykresó do ramek okna
mngr = plt.get_current_fig_manager()
mngr.window.geometry("+0+0") 

plt.subplot(3, 3, 1)
plt.title("Dane wejściowe.")
plt.scatter(x=X[:, 0].cpu(), y=X[:, 1].cpu(), c=y.cpu().detach().numpy(), s=4, cmap=plt.cm.RdYlBu)

plt.subplot(3, 3, 2)
plt.title("Model przed uczeniem, train.")
plt.scatter(x=X_train[:, 0].cpu(), y=X_train[:, 1].cpu(), c=y_train.cpu().detach().numpy(), s=4)#, cmap=plt.cm.RdYlBu)

plt.subplot(3, 3, 3)
plt.title("Model przed uczeniem, test.")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().detach().numpy(), s=4)#, cmap=plt.cm.RdYlBu)


# ------------------------------------------------------------- Pętla uczenia i testu
epoch_count = []
loss_values = []
test_loss_values = []

for epoch in range(EPOCHS):
    
    # uczenie
    modelNN.train()
    y_out = modelNN(X_train)
    loss = loss_fn(y_out, y_train) 
    optimizer.zero_grad()
    loss.backward() 
    optimizer.step()

    y_pred = 

    
    # test
    modelNN.eval()
    with torch.inference_mode():
        test_out = modelNN(X_test) 
        test_loss = loss_fn(test_out, y_test) 
        test_pred = 
    
    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)
    
# ------------------------------------------------------------- Wizualizacja po uczeniu

plt.subplot(3, 3, 4)
plt.title("Model po uczeniu, train.")
plt.scatter(x=X_train[:, 0].cpu(), y=X_train[:, 1].cpu(), c=y_pred.cpu().detach().numpy(), s=4)#, cmap=plt.cm.RdYlBu)

plt.subplot(3, 3, 5)
plt.title("Model po uczeniu, test.")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().detach().numpy(), s=4)#, cmap=plt.cm.RdYlBu)

plt.subplot(3, 3, 6)
plt.title("Straty.")
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")
plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test") 
plt.legend()

plt.subplot(3, 3, 7)
plt.title("Obszary train")
plot_decision_boundary(modelNN, X_train, y_train)

plt.subplot(3, 3, 8)
plt.title("Obszary test")
plot_decision_boundary(modelNN, X_test, y_test)

plt.show()