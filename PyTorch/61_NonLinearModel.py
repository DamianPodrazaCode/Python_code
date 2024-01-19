import torch
from torch import nn
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
from helper_functions import accuracy_fn, plot_decision_boundary

# Sieć ma się nauczyć rozpoznawać do których obszarów należą punkty na poszczególnych okręgach

# start randomów, ustawia ziarno do generowania liczb losowych.
torch.manual_seed(42) 
torch.cuda.manual_seed(42)
# wstyępna konfiguracja wykresów
plt.figure('Wizualizacja', figsize=(12, 8)) # tytuł i rozmiar plota
plt.subplots_adjust(left=0.05, bottom=0.05, top=0.95, right=0.95) # dociągnięcie do ramek wykresów

# ------------------------------------------------------------- 0. Ustalenie urządzenia obliczającego ('cpu', 'cuda', 'ROCm')
device = "cuda" if torch.cuda.is_available() else "cpu"
#device = "cpu" # wymuszenie działania na procesorze

# ------------------------------------------------------------- # 1. Stworzyć lub wczytać dane do nauki i testu (generator lub z dysku).
# wygenerowanie danych dwóch okręgów w postaci punktów
n_samples = 1000
X, y = make_circles(n_samples, noise=0.03, random_state=42) 

# ------------------------------------------------------------- # 2. Przygotować w odpowiednim formacie (dane wejściowe pogrupowane, dane wyjściowe).
# dane okręgów na tensor
X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float)

# ------------------------------------------------------------- # 3. Podzielić na dane uczenia i dane do testu.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=None) 

# ------------------------------------------------------------- # 4. Przekonwertować do tensorów.
X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device)

# ------------------------------------------------------------- # 5. Stworzyć klase, instancje modelu sieci nn.
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
modelNN = CircleModelV0().to(device)  

# tworzenie instancji za pomocą sekwencji
# model_0 = nn.Sequential(
#     nn.Linear(in_features=2, out_features=32),
#     nn.ReLU(),
#     nn.Linear(in_features=32, out_features=32),
#     nn.ReLU(),
#     nn.Linear(in_features=32, out_features=1)
# ).to(device)

# ------------------------------------------------------------- # 6. Skonfigurować funkcje strat i optymalizacji.
loss_fn = nn.BCEWithLogitsLoss() # sigmoid activation function build-in, 
optimizer = torch.optim.SGD(params=modelNN.parameters(), lr=0.1)

# ------------------------------------------------------------- # 7. Pętla nauki i testów.
# sprawdzenie sieci przed uczeniem
modelNN.eval()  
with torch.inference_mode(): 
    test_logits = modelNN(X_test).squeeze()
    test_pred = torch.round(torch.sigmoid(test_logits))
    train_logits = modelNN(X_train).squeeze()
    train_pred = torch.round(torch.sigmoid(train_logits))
plt.subplot(2, 3, 1)
plt.title("Przed uczeniem.")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().numpy(), s=4, cmap=plt.cm.RdYlBu)
plt.scatter(x=X_train[:, 0].cpu(), y=X_train[:, 1].cpu(), c=train_pred.cpu().numpy(), s=4, cmap=plt.cm.RdYlBu)

# podział obszarów w nn
plt.subplot(2, 3, 2)
plt.title("Podział obszarów.")
plot_decision_boundary(modelNN, X_test, y_test)
modelNN.to(device)

# listy do wizualizacji
epoch_count = []
loss_values = []
test_loss_values = []
acc_values = []

# pętla uczenia i testowania
epochs = 1000
for epoch in range(epochs):
    
    # uczenie
    modelNN.train()
    # BCEWithLogitsLoss -> ten model wymaga y_logits
    # X_train -> y_logits -> y_pred
    y_logits = modelNN(X_train).squeeze() # tu wyjściem są liczby rzeczywiste
    y_pred = torch.round(torch.sigmoid(y_logits)) # tu wyjściem jest 1 albo 0 po sigmoidzie
    loss = loss_fn(y_logits, y_train) # a tu trzeba podać liczby rzeczywiste żeby model mógł się uczyć
    acc = accuracy_fn(y_true=y_train, y_pred=y_pred) 
    optimizer.zero_grad()
    loss.backward() 
    optimizer.step()
    
    # test
    modelNN.eval() 
    with torch.inference_mode(): 
        test_logits = modelNN(X_test).squeeze()
        test_pred = torch.round(torch.sigmoid(test_logits))
        test_loss = loss_fn(test_logits, y_test) 
        test_acc = accuracy_fn(y_true=y_test, y_pred=test_pred)

    # uzupełnianie list       
    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)
    acc_values.append(test_acc)

# ------------------------------------------------------------- # 8. Wizualiza i wnioski.

#wizualizacja strat
plt.subplot(2, 3, 3)
plt.title("Krzywe strat uczenia i testu.")
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")  
plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test")  
plt.legend()

# wizualizacja procenu uczenia
plt.subplot(2, 3, 4)
plt.title("Procent przewidywania")
plt.plot(epoch_count, np.array(torch.tensor(acc_values).numpy()))  

# sprawdzenie sieci po uczeniu
modelNN.eval()  
with torch.inference_mode(): 
    test_logits = modelNN(X_test).squeeze()
    test_pred = torch.round(torch.sigmoid(test_logits))
    train_logits = modelNN(X_train).squeeze()
    train_pred = torch.round(torch.sigmoid(train_logits))
plt.subplot(2, 3, 5)
plt.title("Po uczeniu.")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().numpy(), s=4, cmap=plt.cm.RdYlBu)
plt.scatter(x=X_train[:, 0].cpu(), y=X_train[:, 1].cpu(), c=train_pred.cpu().numpy(), s=4, cmap=plt.cm.RdYlBu)

# podział obszarów w nn
plt.subplot(2, 3, 6)
plt.title("Podział obszarów.")
plot_decision_boundary(modelNN, X_test, y_test)
plot_decision_boundary(modelNN, X_train, y_train)
modelNN.to(device)

plt.show()
