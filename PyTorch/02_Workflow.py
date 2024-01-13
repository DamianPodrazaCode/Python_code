import torch
from torch import nn # torch.nn zawiera wszystko do budowania sieci neuronowych
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

#print(torch.__version__)
# 2.1.2+cu121

print('\n-------------------------------------------------------------------------------')
print('....................... stworzenie danych wszystkich (uczenia i testowych)')

# te wartości teraz są dane tylko do stworzenia przykładu, normalnie są to poszukiwane wagi
weight = 0.7
bias = 0.3

# wartości startowe genertatora danych dop przykładu
start  = 0
end = 1
step = 0.02

# stworzenie tensorów danych i poszerzenie wymiaru o 1, i obliczenie danych wyjściowych (dane treningowe i testowe X,y)
X = torch.arange(start, end, step).unsqueeze(dim = 1) 
y = weight * X + bias 

# print(X[:10]) wyświetl pierwsze 10 elementów
# print(X[10:]) wyświetl ostatnie 10 elementów

# wszystkie dane 
print(X[:10], X.shape, len(X), '\n', 
      y[:10], y.shape, len(y), '\n')

print('....................... rozdzielenie danych do uczenia i danych do testowania')
train_split = int(0.8 * len(X)) # obliczenie 80% z długości tensora X (tensor uczenia)
print(train_split)
# 40 - ilość danych uczenia
X_train, y_train = X[:train_split], y[:train_split] # stworzenie tensorów do nauki
X_test, y_test = X[train_split:], y[train_split:] # stworzenie tensorów do testu

#print('....................... wizualizacja danych')
def plot_predictons(train_data = X_train, train_labels = y_train, test_data = X_test, test_label = y_test, predictions = None) :
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")
    plt.scatter(test_data, test_label, c="g", s=4, label="Testing data")
    if predictions is not None :
        plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")
    plt.legend(prop={"size": 14})
    plt.show()            

print(X_train, y_train) # domyślne dane wejściowe do plot_predictons()
print(X_test, y_test)
#plot_predictons()

print('....................... zbudowanie klasy modelu uczenia LinearRegressionModel')
class LinearRegressionModel(nn.Module): # <- nn.Module - klasa bazowa PyTorch dla sieci neuronowych
    def __init__(self) :
        super().__init__()
        # inicjalizacja parametrów modelu, inicjalizacja random-ami ,te wagi będą się ustalać w trakcie uczenia, mają dążyć do zmiennych weights i bias z początku kodu
        self.weights = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
        self.bias = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
    # forward (override) funkcja definiująca zachowanie obliczania, konieczna jeżeli dziedziczy się po nn.Module
    # funkcja która oblicza wszystko w modelu
    def forward(self, x: torch.Tensor) -> torch.Tensor :
        return self.weights * x + self.bias # y = ax + b -> a = dy/dx, b miejsce przecięcia osi y
        
print('....................... tworzenie objektu modelu')        
torch.manual_seed(42)  # parametr startowy random, po to żeby liczby startowe random były takie same przy każdym uruchomieniu, 
# 42 to liczba którą możan znienić dowolnie, potrzebne do nauki o ML żeby porównywać dane, bo tak wygodniej
model_0 = LinearRegressionModel()  # wewnętrzna inicjalizacja modelu, utworzenie instancji, subklasa nn.Module

# sprawdzenie co jest w parametrach modelu
print(list(model_0.parameters())) # lista parametrów, tych z klasy
# [Parameter containing: tensor([0.3367], requires_grad=True), 
#  Parameter containing: tensor([0.1288], requires_grad=True)]
print(model_0.state_dict()) # mapa parametrów z wartościami i nazwami, 
# OrderedDict([('weights', tensor([0.3367])), ('bias', tensor([0.1288]))])

print('....................... prognozowanie - predicton model')        
with torch.inference_mode():
    y_preds = model_0(X_test) # przy pomocy danych testowych oraz wygenerowanych (random) parametrów, tworzony jest tensor wyjściowy
    # jeżeli, przechodzą dane przez model (model_0(X_test)) tak naprawde jest uruchamiana funkcja forward()
print(y_test, '\n', y_preds)
#plot_predictons(predictions=y_preds)

print('.......................  minimalizacja błędu modelu przewidywania')
# loss fonction 
loss_fn = nn.L1Loss() # backpropagation
# optimizer - gradient descent
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.01) # lr = lerning parameter, należy go uzależnić o dokładności parametrów

print('....................... train loop') 
# epoch - jeden przebieg pętli z danymi, jest to hyperparameter bo ustalamy go sami
epochs = 10

for epoch in range(epochs):
    model_0.train()
    #1. Forward pass
    y_pred = model_0(X_train)
    #2. Calculate loss
    loss = loss_fn(y_pred, y_train)
    #3. Optimizer zero grad
    optimizer.zero_grad()
    #4. Backpropagation
    loss.backward()
    #5. Optimizer
    optimizer.step()
    
    # testing
    model_0.eval()
