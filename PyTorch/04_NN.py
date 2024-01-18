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

# zadaniem jest rozdzielenie dwóch okręgów zrobionych z punktów wymieszanych w jednej tablicy (X_train i X_test)

# wygenerowanie danych dwóch okręgów w postaci punktów
n_samples = 1000
X, y = make_circles(n_samples, noise=0.03, random_state=42) 
# print(X, '\n', y)

# wizualizacja w postaci tabeli
# circles = pd.DataFrame({"X1": X[:, 0], "X2": X[:, 1], "label": y})
# print(circles.head(10))

#wizualizacja
# plt.figure('Wszystkie dane')
# plt.scatter(x=X[:, 0], y=X[:, 1], c=y, cmap=plt.cm.RdYlBu)
# plt.show(block=False)
#plt.show(block=True)

# dane do tensora
X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float)

# rozdzielenie danych w sposób random na uczenie i testy (from sklearn.model_selection import train_test_split)
X_train, X_test, y_train, y_test = train_test_split(X,  
                                                    y, 
                                                    test_size=0.2, # 0.2 - będzie 20% danych do testu, 80% do nauki
                                                    random_state=42) 

#stworzenie klasy modelu i konfiguracja loss i optimizer
class CircleModelV0(nn.Module):
    def __init__(self):
        super().__init__()
        
        # tworzenie warstw sieci neuronowej 
        self.layer_1 = nn.Linear(in_features=2, out_features=128) # in_features=2 - wejście do sieci -> dwie dane wejściowe z X, out_features=5 ukryte dwie sieci
        self.layer_1_2 = nn.ReLU()
        self.layer_2 = nn.Linear(in_features=128, out_features=1) # in_features=5 - wejście z sieci ukrytej z poprzedniej warstwy, out_features=1 wyjście z odpowiedziami
    
    # metoda kalkulacji sieci neuronowej        
    def forward(self, x):
        # return self.layer_2(self.layer_1(x)) # x wchodzi do warstwy 1, a warstwa 1 wchodzi do warstwy 2, z której wychodzą odpowiedzi
        return self.layer_2(self.layer_1_2(self.layer_1(x))) 

# start randomów od 412, przed utworzeniem instancji torch
torch.manual_seed(412) 
    
model_0 = CircleModelV0().to(device) # sworzenie instancji


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# uprzoszczony sposób tworzenia instancji modelu, to jest prawie to samo co instancja klasy wyżej, 
# tylko w ten sposób dostaje się z automatu funkcje forward i inne ustawienia
model_0 = nn.Sequential(
    nn.Linear(in_features=2, out_features=128),
    nn.ReLU(),
    nn.Linear(in_features=128, out_features=128),
    nn.ReLU(),
    nn.Linear(in_features=128, out_features=1)
).to(device)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# dane do urządzenia
X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device)

model_0.eval() 
with torch.inference_mode(): 
    test_logits = model_0(X_test).squeeze()
    test_pred = torch.round(torch.sigmoid(test_logits))
        
plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 1)
plt.title("Przed uczeniem, dane testu")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().numpy(), s=4, cmap=plt.cm.RdYlBu)

# inicjalizacja loss function i optimizer
# los function mierzy błąd uczenia
# optimizer - próbuje skorygować błąd zmierzony przez los function

loss_fn = nn.BCEWithLogitsLoss() # sigmoid activation function build-in, 
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.1)
# optimizer = torch.optim.Adam(params=model_0.parameters(), lr=0.1)
 
# listy do wizualizacji
epoch_count = []
loss_values = []
test_loss_values = []

# ilość pętli uczenia
epochs = 300 

# pętla uczenia i testów
for epoch in range(epochs):
    
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

    model_0.eval() 
    with torch.inference_mode(): 
        test_logits = model_0(X_test).squeeze()
        test_pred = torch.round(torch.sigmoid(test_logits))
        test_loss = loss_fn(test_logits, y_test) 
        test_acc = accuracy_fn(y_true=y_test, y_pred=test_pred)
        print(test_acc)
           
    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)
    
# wizualizacja
# plt.figure('Krzywe strat uczenia i testu.')
# plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")  # wymagany casting tensor->numpy
# plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test")  
# plt.ylabel("Starty")
# plt.legend()
# plt.show(block=False)
#plt.show(block=True)

plt.subplot(2, 3, 2)
plt.title("Krzywe strat uczenia i testu.")
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")  # wymagany casting tensor->numpy
plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test")  
plt.ylabel("Starty")
plt.legend()

model_0.eval() 
with torch.inference_mode(): 
    test_logits = model_0(X_test).squeeze()
    test_pred = torch.round(torch.sigmoid(test_logits))
plt.subplot(2, 3, 3)
plt.title("Po uczeniu, dane testu")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().numpy(), s=4, cmap=plt.cm.RdYlBu)

plt.subplot(2, 3, 4)
plt.title("Po uczeniu, dane uczenia")
plot_decision_boundary(model_0, X_train, y_train)

plt.subplot(2, 3, 5)
plt.title("Po uczeniu, dane testu")
plot_decision_boundary(model_0, X_test, y_test)
plt.show()
