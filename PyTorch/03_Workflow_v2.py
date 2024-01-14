import torch
from torch import nn # torch.nn zawiera wszystko do budowania sieci neuronowych
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# Ustawienie urządzenia którego będzie używał PyTorch ('cpu', 'cuda')
device = "cuda" if torch.cuda.is_available() else "cpu"
#device = "cpu" # wymuszenie działania na procesorze
print('Urządzenie którego będę używał:', device)

torch.manual_seed(42)  

print('1 ....................... Stworzenie danych (uczenia i testowych)')
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

print('3 ....................... Stworzenie objekt modelu, konfiguracja strat i optymalizacji')        
model_1 = LinearRegressionModel()  
#print(next(model_1.parameters()).device) # sprawdzenie jakiego urzadzenia używam do modelu
model_1.to(device) # ustawienie urządzenia do obliczeń 
#print(next(model_1.parameters()).device) # sprawdzenie jakiego urzadzenia używam do modelu
X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device)
loss_fn = nn.L1Loss() 
optimizer = torch.optim.SGD(params=model_1.parameters(), lr=0.01) 
print('Parametry modelu przed uczeniem, idealne to (0.7, 0.3)', model_1.state_dict()) # sprawdzenie parametrów modelu

print('4 ....................... Wizualizacja przed uczeniem')      
model_1.eval()  
with torch.inference_mode(): 
    y_preds = model_1(X_test) 
# wizualizacja
plt.figure('Prognozowanie przed uczeniem.')
plt.scatter(X_train.cpu(), y_train.cpu(), c='b', s=2, label="uczenie")  
plt.scatter(X_test.cpu(), y_test.cpu(), c='y', s=2, label="test")  
plt.scatter(X_test.cpu(), y_preds.cpu(), c='r', s=2, label="prognoza")  
plt.legend()
plt.show(block=False)
#plt.show(block=True)

print('5 ....................... Uczenie i testowanie') 
epochs = 200 
epoch_count = []
loss_values = []
test_loss_values = []

for epoch in range(epochs):
    
    model_1.train()
    y_pred = model_1(X_train)
    loss = loss_fn(y_pred, y_train)
    optimizer.zero_grad()
    loss.backward() 
    optimizer.step()

    model_1.eval() 
    with torch.inference_mode(): 
        test_pred = model_1(X_test) 
        test_loss = loss_fn(test_pred, y_test) 

    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)

print('Parametry modelu po uczeniu, idealne to (0.7, 0.3)', model_1.state_dict()) # sprawdzenie parametrów modelu

# wizualizacja
plt.figure('Krzywe strat uczenia i testu.')
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")  # wymagany casting tensor->numpy
plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test")  
plt.ylabel("Starty")
plt.legend()
plt.show(block=False)
#plt.show(block=True)

print('6 ....................... Prognozowanie - po uczeniu.')  
model_1.eval()  
with torch.inference_mode(): 
    y_preds = model_1(X_test) 
# wizualizacja
plt.figure('Prognozowanie po uczeniu.')
plt.scatter(X_train.cpu(), y_train.cpu(), c='b', s=2, label="uczenie")  
plt.scatter(X_test.cpu(), y_test.cpu(), c='y', s=2, label="test")  
plt.scatter(X_test.cpu(), y_preds.cpu(), c='r', s=2, label="prognoza")  
plt.legend()
#plt.show(block=False)
plt.show(block=True)
