import torch
from torch import nn
# import torchmetrics
# from torchmetrics import Accuracy
import matplotlib.pyplot as plt 
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from helper_functions import plot_decision_boundary
import numpy as np

torch.manual_seed(42)  # ziarnistość random
torch.cuda.manual_seed(42) # to samo tylko dla cuda

device = "cuda" if torch.cuda.is_available() else "cpu" # wybranie urządzenia liczącego

# dwie tablie, jedna pozycje x,y, druga grupy 0,1,2,3 do tamtych pozycji
NUM_CLASSES = 4 # ilość grup
NUM_FEATURES = 2 # ilość wymiarów (x,y)
RANDOM_SEED = 42
X_blob, y_blob = make_blobs(n_samples=1000, n_features=NUM_FEATURES, centers=NUM_CLASSES, cluster_std=1.5, random_state=RANDOM_SEED)

# konwersja do tensorów
X_blob = torch.from_numpy(X_blob).type(torch.float)
y_blob = torch.from_numpy(y_blob).type(torch.LongTensor)

# rozdzielenie na dane uczenia i testu
X_train, X_test, y_train, y_test = train_test_split(X_blob, y_blob, test_size=0.3, random_state=RANDOM_SEED) 

# tensory do właściwego urządzenia
X_train, y_train = X_train.to(device), y_train.to(device)
X_test, y_test = X_test.to(device), y_test.to(device)

# klasa sieci
class MultiModel(nn.Module):
    def __init__(self, input_features, output_features, hidden_layers=8):
        super().__init__()
        self.linear_layer_stack = nn.Sequential(
            nn.Linear(in_features=input_features, out_features=hidden_layers),
            nn.ReLU(), 
            nn.Linear(in_features=hidden_layers, out_features=hidden_layers),
            nn.ReLU(),  
            nn.Linear(in_features=hidden_layers, out_features=output_features)
        )
        
    def forward(self, x):
        return self.linear_layer_stack(x)

# instancja sieci nn
modelNN = MultiModel(input_features=2, output_features=4, hidden_layers=8).to(device)

# ustawienie funkcji strat i optymalizacji
loss_fn = nn.CrossEntropyLoss() # uwaga w funkcji loss_fn muszą być typy torch.LongTensor
optimizer = torch.optim.SGD(params=modelNN.parameters(), lr=0.1)

epoch_count = []
loss_values = []
test_loss_values = []

# pętla uczenia
epochs = 500
for epoch in range(epochs):
    
    # uczenie
    modelNN.train()
    y_out = modelNN(X_train) # model zwraca typ torch.LongTensor
    loss = loss_fn(y_out, y_train) # tu y_train musi być torch.LongTensor
    optimizer.zero_grad()
    loss.backward() 
    optimizer.step()

    # y_out         -> wiersz [ -2.9356,  -9.7943,  -6.3436,   5.5677]
    # po soft max   -> wiersz [  0.3371,   0.1372,   0.1950,   0.3307] - suma równa sie 1.0
    # po torch.argmax zwracany jest index najwyższej wartości liczony od 0 i od lewej strony w tym przypadku będzie to index 0
    # w ostatnim y_pred tablica straci jeden wymiar, bo z czterech wartości w wierszu zrobi się jeden
    y_pred = torch.softmax(y_out, dim=1) # (y_out, dim=1) oznacza weź z tablicy cały wymiar pierwszy
    y_pred = torch.argmax(y_pred, dim=1)
    
    # test
    modelNN.eval()
    with torch.inference_mode():
        test_out = modelNN(X_test) 
        test_loss = loss_fn(test_out, y_test) 
        test_pred = torch.softmax(test_out, dim=1)
        test_pred = torch.argmax(test_pred, dim=1)    
    
    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)
    
#wizualizacja
plt.figure('Wizualizacja', figsize=(12, 8)) # tytuł i rozmiar plota
plt.subplots_adjust(left=0.05, bottom=0.05, top=0.95, right=0.95) # dociągnięcie do ramek wykresów

plt.subplot(2, 3, 1)
plt.title("Dane wejściowe.")
plt.scatter(x=X_blob[:, 0].cpu(), y=X_blob[:, 1].cpu(), c=y_blob.cpu().detach().numpy(), s=4, cmap=plt.cm.RdYlBu)

plt.subplot(2, 3, 2)
plt.title("Dane po uczeniu, train.")
plt.scatter(x=X_train[:, 0].cpu(), y=X_train[:, 1].cpu(), c=y_pred.cpu().detach().numpy(), s=4)#, cmap=plt.cm.RdYlBu)

plt.subplot(2, 3, 3)
plt.title("Dane po uczeniu, test.")
plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu().detach().numpy(), s=4)#, cmap=plt.cm.RdYlBu)

plt.subplot(2, 3, 4)
plt.title("Straty.")
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")
plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test") 
plt.legend()

plt.subplot(2, 3, 5)
plt.title("Obszary train")
plot_decision_boundary(modelNN, X_train, y_train)

plt.subplot(2, 3, 6)
plt.title("Obszary test")
plot_decision_boundary(modelNN, X_test, y_test)

plt.show()
