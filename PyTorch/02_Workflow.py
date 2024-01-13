import torch
from torch import nn # torch.nn zawiera wszystko do budowania sieci neuronowych
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

#print(torch.__version__)
# 2.1.2+cu121

print('\n-------------------------------------------------------------------------------')
print('....................... stworzenie danych wszystkich (uczenia i testowych)')

# te parametry teraz są dane tylko do stworzenia przykładu, normalnie są to poszukiwane wagi, i cały model będzie dążył do ty parametrów
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
    if train_labels is not None :
        plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")
    if test_label is not None :
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
        # self.weights = nn.Parameter(torch.tensor(0.0))
        # self.bias = nn.Parameter(torch.tensor(0.0))
    # forward (override) funkcja definiująca zachowanie obliczania, konieczna jeżeli dziedziczy się po nn.Module
    # funkcja która oblicza wszystko w modelu, przez nią w każdym etapie modelowania oraz testu przechodząś dane
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias # y = ax + b -> a = dy / dx, b miejsce przecięcia osi y
        
print('....................... tworzenie objektu modelu')        
torch.manual_seed(42)  # parametr startowy random, po to żeby liczby startowe random były takie same przy każdym uruchomieniu, 
# 42 to liczba którą możan znienić dowolnie, potrzebne do nauki o ML żeby porównywać dane, bo tak wygodniej
model_0 = LinearRegressionModel()  # wewnętrzna inicjalizacja modelu, utworzenie instancji, subklasa nn.Module

# sprawdzenie co jest w parametrach modelu
print(list(model_0.parameters())) # lista parametrów, tych z klasy
# [Parameter containing: tensor([0.3367], requires_grad=True), 
#  Parameter containing: tensor([0.1288], requires_grad=True)]
print(model_0.state_dict()) # mapa parametrów z wartościami i nazwami
# OrderedDict([('weights', tensor([0.3367])), ('bias', tensor([0.1288]))])

print('....................... prognozowanie - predicton model')        
with torch.inference_mode(): # uruchomienie przetwarzania danych w modelu bez reszty modelu, zostaną tylko przetworzone dane wejściowe
    y_preds = model_0(X_test) # przy pomocy danych testowych oraz wygenerowanych (random) parametrów, tworzony jest tensor wyjściowy
    # jeżeli, przechodzą dane przez model (model_0(X_test)) tak naprawde jest uruchamiana funkcja forward()
print(y_test, '\n', y_preds) # dane y_test to dane jakie powinny być, a y_preds jakie są przewidywane
plot_predictons(predictions=y_preds) # porównanie zielonych kropek y_test(prawidłowych) a czerwonych kropek(prognozowanych)

# starsza metoda, ale prawie taka sama, w tym przypadku będzie taki sam skutek, ta pierwsza jest zalecana przez PyTorch
# with torch.no_grad():    
#     y_preds = model_0(X_test)
# print(y_test, '\n', y_preds)
# plot_predictons(predictions=y_preds)

print('....................... minimalizacja błędu modelu przewidywania')
# wskazanie jakie metody będą używane dla obliczeń strat i optymalizacji
# loss function - pomiar jaki jest błąd między prognozowaniem a wyjściem z danymi prawidłowymi, czym mniejszy błąd tym lepiej
loss_fn = nn.L1Loss() # algorytmy oblicznia strat https://pytorch.org/docs/stable/nn.html#loss-functions
# optimizer - gradient descent - bierze dane obliczone z loss function reguluje parametry modelu
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.01) # lr = lerning rate, należy go uzależnić w zależności od dokładności danych wejściowych
# lr jest uzależnione od tego jaką dokładność uczenia chcemy uzyskać, jeżeli paramerty mają być z dokładnością 0.001 to tak trzeba ustawić lr
# algorytmy optymalizacji - https://pytorch.org/docs/stable/optim.html#algorithms
# loss function i optimazer będą używane w pętli treningu i tam dopiero dadzą efekt, teraz są tylko inicjalizowane
            
print('....................... uczenie i testowanie') 
# epoch - jeden przebieg pętli z danymi
epochs = 200 # ilość przebiegów pętli nauki, jest to hyperparameter, ustalamy go sami, przy tych ustawieniach moje spostrzeżenie to (1/lr) * 2

# dane które śledzimy
epoch_count = []
loss_values = []
test_loss_values = []

for epoch in range(epochs):
    # uczenie    
    model_0.train()
    #1. Forward() z obiektu model_0, dane przechodzą przez model i są aktualizowane zgodnie z parametrami, które się aktualizują niżej w pętli
    y_pred = model_0(X_train) # wynikiem są dane coraz bliższe do rzeczywistych
    #2. obliczenie strat (loss function) czyli błędu (różnicy między orginałem)
    loss = loss_fn(y_pred, y_train)
    #3. Przywrócenie ustawień optymilizataora na default, że by później obliczyć nową optymalizacje
    optimizer.zero_grad()
    #4. Backpropagation, obliczanie strat do tyłu w sieci żeby obliczyć gradient każdego parametru, żeby zbliżyć się do strat na poziomie zero
    loss.backward() 
    #5. Optymalizacja parametrów modelu, wyregulowanie ich (gradient descent)
    optimizer.step()

    # testy
    # testing wyłącza różne ustawienia w modelu które nie są potrzebne do testowania, pprzyspiesza to testowanie
    model_0.eval()
    with torch.inference_mode(): # wyłacza np, obliczanie gradientu, przyspiesza testowanie
        # 1. obliczenia forward()
        test_pred = model_0(X_test)
        # 2. straty
        test_loss = loss_fn(test_pred, y_test)

    if epoch % 10 == 0:
        epoch_count.append(epoch)
        loss_values.append(loss)
        test_loss_values.append(test_loss)
        # print(epoch, loss, test_loss)
        # print(model_0.state_dict())

# krzywe strat
plt.figure(1)
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Train loss")  
plt.plot(epoch_count, test_loss_values, label="Test loss")  
plt.title("Training and test loss curves")
plt.ylabel("Loss")
plt.xlabel("Epochs")
plt.legend()
plt.show(block=False)

# prognozy po nauce    
print(model_0.state_dict()) # obliczone parametry
with torch.inference_mode(): 
    y_preds = model_0(X_test)
plot_predictons(predictions=y_preds)    
