import torch
from torch import nn # torch.nn zawiera wszystko do budowania sieci neuronowych
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# Ustawienie urządzenia którego będzie używał PyTorch ('cpu', 'cuda')
device = "cuda" if torch.cuda.is_available() else "cpu"
print('Używam urządzenia:', device)
# Model treningowy całkowicie liniowy, wszystkie dane leżą na lini:
# 1. Stworzenie tensorów które mają wartości idealne, znane są również parametry(wagi). Rozdzielenie danych na uczenia i testowe.
# 2. Definicja klasy modelu uczenia LinearRegressionModel.
# 3. Tworzenie objekt modelu.
# 4. Prognozowanie - predicton model.
# 5. Konfiguracja minimalizacji błędu (loss, optimize).
# 6. Uczenie i testowanie.
# 7. Prognozowanie - po uczeniu.

print('1 ....................... Stworzenie tensorów (uczenia i testowych)')
weight, bias = 0.7, 0.3
start, end, step  = 0, 1, 0.02
X = torch.arange(start, end, step).unsqueeze(dim = 1) 
y = weight * X + bias 
train_split = int(0.8 * len(X)) 
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

print('2 ....................... Definicja klasy modelu uczenia LinearRegressionModel')
# użycie Linear Layers wbudowanej https://pytorch.org/docs/stable/generated/torch.nn.Linear.html#torch.nn.Linear
# o wiele lepsze efekty, nie trzeba generować parametrów startowych
class LinearRegressionModel(nn.Module):
    def __init__(self) :
        super().__init__()
        self.linear_layer = nn.Linear(in_features=1, out_features=1) 
    def forward(self, x: torch.Tensor) -> torch.Tensor:
       return self.linear_layer(x)       

print('3 ....................... Tworzenie objekt modelu')        
torch.manual_seed(42)  
model_1 = LinearRegressionModel()  
#print(model_1.state_dict()) 
# sprawdzenie jakiego urzadzenia używam do modelu
#print(next(model_1.parameters()).device)
model_1.to(device) # ustawienie urządzenia do obliczeń 
#print(next(model_1.parameters()).device)

print('4 ....................... Prognozowanie - predicton model')        
with torch.inference_mode(): 
    y_preds = model_1(X_test) 
# wizualizacja
plt.figure('Prognozowanie przed uczeniem, parametry random.')
plt.scatter(X_train, y_train, c='b', s=2, label="uczenie")  
plt.scatter(X_test, y_test, c='y', s=2, label="test")  
plt.scatter(X_test, y_preds, c='r', s=2, label="prognoza")  
plt.legend()
plt.show(block=False)
#plt.show(block=True)

print('5 ....................... Konfiguracja minimalizacji błędu (loss, optimize)')
# wskazanie jakie metody będą używane dla obliczeń strat i optymalizacji
# loss function - pomiar pomiędzy prognozowaniem a danymi testowymi, czym mniejszy błąd tym lepiej
# algorytmy oblicznia strat https://pytorch.org/docs/stable/nn.html#loss-functions
loss_fn = nn.L1Loss() 
# optimizer - bierze dane obliczone z loss function i reguluje parametry modelu
optimizer = torch.optim.SGD(params=model_1.parameters(), lr=0.01) 
# lr = lerning rate, jest uzależnione od tego jaką dokładność uczenia chcemy uzyskać, 
# jeżeli paramerty mają być z dokładnością 0.001 to tak trzeba ustawić lr
# algorytmy optymalizacji - https://pytorch.org/docs/stable/optim.html#algorithms
# loss function i optimazer będą używane w pętli treningu i tam dopiero dadzą efekt, teraz są tylko wybierane
      
print('6 ....................... Uczenie i testowanie') 
# Pętla w której uczymy i testujemy model, objekt automatycznie oblicza straty i optymalizuje parametry(wagi).
epochs = 200 # ilość przebiegów pętli nauki i testowania, jest to hyperparameter i ustalamy go sami, 
# wstępnie wartość tego parametru przy regresji liniowej ustalam wg wzoru epochs = (1/lr) * 2 gdzie lr jest wartością ustalaną w optymizerze

# listy do wizualizacji strat, uzupełniane w trakcie uczenia i testowania
epoch_count = []
loss_values = []
test_loss_values = []

for epoch in range(epochs):
    
    model_1.train() # włączenie uczenia
    #1. Forward() z obiektu model_1, dane przechodzą przez model i są aktualizowane zgodnie z parametrami(wagami), wynikiem są dane coraz bliższe do rzeczywistych
    y_pred = model_1(X_train)
    #2. Obliczenie strat (loss function) czyli błędu (różnicy między danymi testowymi a danymi obliczonymi wg aktualnych parametrów)
    loss = loss_fn(y_pred, y_train)
    #3. Prezejście wstecz gradientu
    optimizer.zero_grad()
    #4. Backpropagation, obliczanie strat do tyłu w sieci żeby obliczyć gradient każdego parametru, żeby zbliżyć się do strat na poziomie zero
    loss.backward() 
    #5. Optymalizacja parametrów modelu, wyregulowanie ich (gradient descent)
    optimizer.step()

    model_1.eval() # włączenie testowania, wyłącza różne ustawienia w modelu które nie są potrzebne do testowania, przyspiesza to testowanie
    with torch.inference_mode(): # wyłącza np: obliczanie gradientu, przyspiesza testowanie
        test_pred = model_1(X_test) # forward()
        test_loss = loss_fn(test_pred, y_test) # straty

    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)

# wizualizacja
plt.figure('Krzywe strat uczenia i testu.')
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")  # wymagany casting tensor->numpy
plt.plot(epoch_count, test_loss_values, label="Starty test")  
plt.ylabel("Starty")
plt.legend()
plt.show(block=False)
#plt.show(block=True)

print('7 ....................... Prognozowanie - po uczeniu.')  
with torch.inference_mode(): 
    y_preds = model_1(X_test)
# wizualizacja
plt.figure('Prognozowanie po uczeniu.')
plt.scatter(X_train, y_train, c='b', s=2, label="uczenie")  
plt.scatter(X_test, y_test, c='y', s=2, label="test")  
plt.scatter(X_test, y_preds, c='r', s=2, label="prognoza")  
plt.legend()
#plt.show(block=False)
plt.show(block=True)

