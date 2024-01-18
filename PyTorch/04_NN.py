import sklearn
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
import torch
from torch import nn 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from helper_functions import plot_predictions, plot_decision_boundary, accuracy_fn

# Ustawienie urządzenia którego będzie używał PyTorch ('cpu', 'cuda')
device = "cuda" if torch.cuda.is_available() else "cpu"
# device = "cpu" # wymuszenie działania na procesorze
# print('Urządzenie którego będę używał:', device)

# Cele:
# 1. Wygenerowanie dwóch okręgów w punktów.
# 2. Wyznaczenie granicy między okręgami.

# wygenerowanie danych dwóch okręgów w postaci punktów
n_samples = 1000
X, y = make_circles(n_samples, noise=0.03, random_state=42) 

# wizualizacja w postaci tabeli
# circles = pd.DataFrame({"X1": X[:, 0], "X2": X[:, 1], "label": y})
# print(circles.head(10))

# wizualizacja
# plt.figure('Wszystkie dane')
# plt.scatter(x=X[:, 0], y=X[:, 1], c=y, cmap=plt.cm.RdYlBu)
# plt.show(block=False)
# plt.show(block=True)

# dane okręgów na tensor
X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float)

# rozdzielenie danych w sposób random na uczenie i testy (from sklearn.model_selection import train_test_split)
X_train, X_test, y_train, y_test = train_test_split(X,  
                                                    y, 
                                                    test_size=0.2, # 0.2 - będzie 20% danych do testu, 80% do nauki
                                                    random_state=42) 

# start randomów od 42, przed utworzeniem instancji torch
torch.manual_seed(42) 
torch.cuda.manual_seed(42)

#stworzenie klasy modelu NN
class CircleModelV0(nn.Module):
    def __init__(self):
        super().__init__()
        
        # tworzenie warstw sieci neuronowej 
        self.layer_1 = nn.Linear(in_features=2, out_features=32) 
        self.layer_2 = nn.Linear(in_features=32, out_features=32)
        self.layer_3 = nn.Linear(in_features=32, out_features=1) 
        self.relu = nn.ReLU() # nie liniowa funkcja aktywacji
    
    # metoda kalkulacji sieci neuronowej        
    def forward(self, x):
        # return self.layer_2(self.layer_1(x)) # x wchodzi do warstwy 1, a warstwa 1 wchodzi do warstwy 2, z której wychodzą odpowiedzi
        return self.layer_3(self.relu(self.layer_2(self.relu(self.layer_1(x)))))

# sworzenie instancji modelu i przesunięcie go do GPU    
model_0 = CircleModelV0().to(device) 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# uprzoszczony sposób tworzenia instancji modelu, to jest prawie to samo co instancja klasy wyżej, 
# tylko w ten sposób dostaje się z automatu funkcje forward i inne ustawienia
# tutaj napisanie modelu wyżej stworzonego, jak ten jest aktywny to ten wyżej można zakomentować i odwrotnie
# model_0 = nn.Sequential(
#     nn.Linear(in_features=2, out_features=128),
#     nn.ReLU(),
#     nn.Linear(in_features=128, out_features=128),
#     nn.ReLU(),
#     nn.Linear(in_features=128, out_features=1)
# ).to(device)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# dane treningu i testu przesunięcie do urządzenia
X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device)

# loss function mierzy błąd uczenia
loss_fn = nn.BCEWithLogitsLoss() # sigmoid activation function build-in, 

# optimizer - próbuje skorygować błąd zmierzony przez los function
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.1)

# model prognozy przed uczeniem
model_0.eval() 
with torch.inference_mode(): 
    test_logits = model_0(X_test).squeeze()
    test_pred = torch.round(torch.sigmoid(test_logits))
# wizualizacja prognozy przed uczeniem       
plt.figure('OUT', figsize=(12, 8))
plt.subplots_adjust(left=0.05, bottom=0.05, top=0.95, right=0.95)

plt.subplot(2, 3, 1)
plt.title("Prognoza przed uczeniem, dane testu")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().numpy(), s=4, cmap=plt.cm.RdYlBu)
 
# listy do wizualizacji
epoch_count = []
loss_values = []
test_loss_values = []
acc_values = []

# ilość pętli uczenia
epochs = 1000 

# pętla uczenia i testów
for epoch in range(epochs):
    
    # uczenie
    model_0.train()
    # BCEWithLogitsLoss -> ten model wymaga y_logits
    # X_train -> y_logits -> y_pred
    y_logits = model_0(X_train).squeeze() # tu wyjściem są liczby rzeczywiste
    y_pred = torch.round(torch.sigmoid(y_logits)) # tu wyjściem jest 1 albo 0 po sigmoidzie
    loss = loss_fn(y_logits, y_train) # a tu trzeba podać liczby rzeczywiste żeby model mógł się uczyć
    acc = accuracy_fn(y_true=y_train, y_pred=y_pred) 
    optimizer.zero_grad()
    loss.backward() 
    optimizer.step()

    # testowanie
    model_0.eval() 
    with torch.inference_mode(): 
        test_logits = model_0(X_test).squeeze()
        test_pred = torch.round(torch.sigmoid(test_logits))
        test_loss = loss_fn(test_logits, y_test) 
        test_acc = accuracy_fn(y_true=y_test, y_pred=test_pred)
      
    # uzupełnianie danych do wizualizacji       
    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)
    acc_values.append(test_acc)
    
# wizualizacja strat
plt.subplot(2, 3, 2)
plt.title("Krzywe strat uczenia i testu.")
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")  # wymagany casting tensor->numpy
plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test")  
plt.ylabel("Starty")
plt.legend()

# wizualizacja procenu uczenia
plt.subplot(2, 3, 3)
plt.title("Procent przewidywania")
plt.plot(epoch_count, np.array(torch.tensor(acc_values).numpy()))  

# model prognozy po uczeniu
model_0.eval() 
with torch.inference_mode(): 
    test_logits = model_0(X_test).squeeze()
    test_pred = torch.round(torch.sigmoid(test_logits))
# wizualizacja    
plt.subplot(2, 3, 4)
plt.title("Prognoza po uczeniu, dane testu")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().numpy(), s=4, cmap=plt.cm.RdYlBu)

# wizualizacja model uczenia - dane uczenia
plt.subplot(2, 3, 5)
plt.title("Po uczeniu, dane uczenia")
plot_decision_boundary(model_0, X_train, y_train)

# wizualizacja model uczenia - dane testu
plt.subplot(2, 3, 6)
plt.title("Po uczeniu, dane testu")
plot_decision_boundary(model_0, X_test, y_test)
plt.show()


