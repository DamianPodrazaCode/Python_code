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
# Te zmienne (weight, bias) to tylko dane do stworzenia tensorów (uczenia i testowania), 
# normalnie są to poszukiwane wagi i w normalnym modelu są one nieznane, cały model będzie dążył do tych parametrów
weight = 0.7
bias = 0.3
# wartości graniczne genertatora danych dla przykładu
start, end, step  = 0, 1, 0.02
# stworzenie tensorów (uczenia i testowe), dane idealne, ilość 50
X = torch.arange(start, end, step).unsqueeze(dim = 1) # tensor z x-ami, konieczne poszerzenie o wymiar 
y = weight * X + bias # tensor z y-ami
# rozdzielenie danych do uczenia i danych do testowania
train_split = int(0.8 * len(X)) # obliczenie 80% z długości tensora X (tensor uczenia), uczenie 40 danych, test 10 danych
X_train, y_train = X[:train_split], y[:train_split] # stworzenie tensorów do uczenia od 0 do 39
X_test, y_test = X[train_split:], y[train_split:] # stworzenie tensorów do testu od 40 do 49
# wizualizacja
# plt.figure('Tensory wejściowe.')
# plt.scatter(X_train, y_train, c='b', s=2, label="uczenie")  
# plt.scatter(X_test, y_test, c='y', s=2, label="test")  
# plt.legend()
# plt.show(block=False)
#plt.show(block=True)

print('2 ....................... Definicja klasy modelu uczenia LinearRegressionModel')
class LinearRegressionModel(nn.Module): # <- nn.Module - klasa bazowa PyTorch dla sieci neuronowych
    def __init__(self) :
        super().__init__()
        # inicjalizacja parametrów modelu, inicjalizacja random-ami, te wagi będą się ustalać w trakcie uczenia, 
        # mają dążyć do zmiennych weights i bias z początku kodu, można je ustalic liczbami np 0. wtedy parametry szukane zaczną od tych wartości, 
        # ale w praktyce robi się to na randomach, teba pamiętać że przy ustawieniu 0 prawdopodobnie uczenie będzie trwało dłużej
        
        # parametry startujące od random
        # self.weights = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
        # self.bias = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
        
        # parametry startujące od zera - przy tym samym czasie uczenia najgorszy wynik
        # self.weights = nn.Parameter(torch.tensor(0.0), requires_grad=True)
        # self.bias = nn.Parameter(torch.tensor(0.0), requires_grad=True)
        
        # parametry startujące od średniej danych wejściowych uczenia X - najlepszy wynik w tym przypadku
        inData = float(X_train.type(torch.float32).mean())
        self.weights = nn.Parameter(torch.tensor(inData), requires_grad=True)
        self.bias = nn.Parameter(torch.tensor(inData), requires_grad=True)

        # parametry startujące od średniej danych wejściowych uczenia y
        # inData = float(y_train.type(torch.float32).mean())
        # self.weights = nn.Parameter(torch.tensor(inData), requires_grad=True)
        # self.bias = nn.Parameter(torch.tensor(inData), requires_grad=True)
        
    # forward (override) funkcja definiująca zachowanie obliczeń, konieczna jeżeli dziedziczy się po nn.Module
    # funkcja która oblicza model, przez nią w każdym etapie modelowania oraz testu przechodzą dane
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias # y = ax + b -> a = dy / dx, b miejsce przecięcia osi y

print('3 ....................... Tworzenie objekt modelu')        
torch.manual_seed(42)  # parametr startowy random, po to żeby random przy każdym uruchomieniu startował z tej samej liczby 
# w parametrach(wagach) objektu klasy LinearRegressionModel, 42 to liczba którą możan znienić dowolnie, 
# ten zabieg potrzebny jest do nauki o ML żeby porównywać dane, bo tak wygodniej
model_0 = LinearRegressionModel()  # inicjalizacja modelu, utworzenie instancji(objektu), subklasa nn.Module
# parametry modelu(wagi)
# print(list(model_0.parameters())) # lista parametrów z wartościami, 
# [Parameter containing: tensor([0.3367], requires_grad=True), 
#  Parameter containing: tensor([0.1288], requires_grad=True)]
# print(model_0.state_dict()) # mapa parametrów z nazwami i wartościami 
# OrderedDict([('weights', tensor([0.3367])), ('bias', tensor([0.1288]))])

print('4 ....................... Prognozowanie - predicton model')        
# prognozowanie ma na celu sprawdzenie danych testowych na podstrawie parametrów(wag), bez gradientu i innych ustawień, 
# jest to szybkie sprawdzenie danych, poprostu dane przechodzą przez model(funkcja forward())
with torch.inference_mode(): 
# with torch.no_grad(): # starsza metoda, prawie taka sama, wyłącza tylko gradient, ta pierwsza jest zalecana przez PyTorch   
    y_preds = model_0(X_test) 
# print(y_test, '\n', y_preds) # dane y_test to dane jakie powinny być, a y_preds jakie są przewidywane
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
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.01) 
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
    
    model_0.train() # włączenie uczenia
    #1. Forward() z obiektu model_0, dane przechodzą przez model i są aktualizowane zgodnie z parametrami(wagami), wynikiem są dane coraz bliższe do rzeczywistych
    y_pred = model_0(X_train)
    #2. Obliczenie strat (loss function) czyli błędu (różnicy między danymi testowymi a danymi obliczonymi wg aktualnych parametrów)
    loss = loss_fn(y_pred, y_train)
    #3. Prezejście wstecz gradientu
    optimizer.zero_grad()
    #4. Backpropagation, obliczanie strat do tyłu w sieci żeby obliczyć gradient każdego parametru, żeby zbliżyć się do strat na poziomie zero
    loss.backward() 
    #5. Optymalizacja parametrów modelu, wyregulowanie ich (gradient descent)
    optimizer.step()

    model_0.eval() # włączenie testowania, wyłącza różne ustawienia w modelu które nie są potrzebne do testowania, przyspiesza to testowanie
    with torch.inference_mode(): # wyłącza np: obliczanie gradientu, przyspiesza testowanie
        test_pred = model_0(X_test) # forward()
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
    y_preds = model_0(X_test)
# wizualizacja
plt.figure('Prognozowanie po uczeniu.')
plt.scatter(X_train, y_train, c='b', s=2, label="uczenie")  
plt.scatter(X_test, y_test, c='y', s=2, label="test")  
plt.scatter(X_test, y_preds, c='r', s=2, label="prognoza")  
plt.legend()
#plt.show(block=False)
plt.show(block=True)

