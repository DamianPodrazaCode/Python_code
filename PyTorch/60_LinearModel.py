import torch
from torch import nn
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.model_selection import train_test_split
from helper_functions import accuracy_fn

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
# utworzenie lini prostej y = ax + b
weight, bias = 0.7, 0.3
start, end, step  = 0, 1, 0.02
# ------------------------------------------------------------- # 2. Przygotować w odpowiednim formacie (dane wejściowe pogrupowane, dane wyjściowe).
X = torch.arange(start, end, step).unsqueeze(dim = 1) 
y = weight * X + bias 

# ------------------------------------------------------------- # 3. Podzielić na dane uczenia i dane do testu.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=None) 

# ------------------------------------------------------------- # 4. Przekonwertować do tensorów.
X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device)

# ------------------------------------------------------------- # 5. Stworzyć klase, instancje modelu sieci nn.
class LinearModel(nn.Module):
    def __init__(self) :
        super().__init__()
        
        # model jedno warstwowy
        # self.layer1 = nn.Linear(in_features=1, out_features=1) 
        
        # model weilowarstwowy
        self.layer1 = nn.Linear(in_features=1, out_features=8)
        self.layer2 = nn.Linear(in_features=8, out_features=1)
                
    def forward(self, x: torch.Tensor) -> torch.Tensor:
       #return self.layer1(x) 
       return self.layer2(self.layer1(x))

modelNN = LinearModel().to(device)  

# tworzenie instancji za pomocą sekwencji
# modelNN = nn.Sequential(
#     nn.Linear(in_features=1, out_features=32),      # x -> layer_1 ->
#     nn.Linear(in_features=32, out_features=1),     # layer_1 -> out
# ).to(device)

# ------------------------------------------------------------- # 6. Skonfigurować funkcje strat i optymalizacji.
# loss_fn = nn.L1Loss() 
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(params=modelNN.parameters(), lr=0.01) 

# ------------------------------------------------------------- # 7. Pętla nauki i testów.
# sprawdzenie sieci przed uczeniem
modelNN.eval()  
with torch.inference_mode(): 
    y_before = modelNN(X_test) 
plt.subplot(2, 3, 1)
plt.scatter(X_train.cpu(), y_train.cpu(), c='b', s=2, label="Dane do uczenia.")  
plt.scatter(X_test.cpu(), y_test.cpu(), c='y', s=2, label="Dane do testu.")  
plt.scatter(X_test.cpu(), y_before.cpu(), c='r', s=2, label="Sieć nn przed uczeniem.")  
plt.legend()

# listy do wizualizacji
epoch_count = []
loss_values = []
test_loss_values = []
acc_values = []

# pętla uczenia i testowania
epochs = 600
for epoch in range(epochs):
    
    # uczenie
    modelNN.train()
    y_pred = modelNN(X_train)
    loss = loss_fn(y_pred, y_train)
    optimizer.zero_grad()
    loss.backward() 
    optimizer.step()

    # test
    modelNN.eval() 
    with torch.inference_mode(): 
        test_pred = modelNN(X_test) 
        test_loss = loss_fn(test_pred, y_test) 

    # uzupełnianie list
    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)

# ------------------------------------------------------------- # 8. Wizualiza i wnioski.

plt.subplot(2, 3, 2)
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie.")  
plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test.")  
plt.legend()

# sprawdzenie sieci po uczeniu
modelNN.eval()  
with torch.inference_mode(): 
    y_after = modelNN(X_test) 
plt.subplot(2, 3, 3)
plt.scatter(X_train.cpu(), y_train.cpu(), c='b', s=2, label="Dane do uczenia.")  
plt.scatter(X_test.cpu(), y_test.cpu(), c='y', s=2, label="Dane do test.")  
plt.scatter(X_test.cpu(), y_after.cpu(), c='r', s=2, label="Sieć nn po uczeniu.")  
plt.legend()

plt.show()
