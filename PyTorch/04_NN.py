import sklearn
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
import torch
from torch import nn 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
# import requests
from helper_functions import plot_predictions, plot_decision_boundary

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

# print(X.shape, y.shape)
# print(X[0, 0])

# dane do tensora
# print(type(X), X.dtype)
X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float)
# print(X, '\n', y)

# rozdzielenie danych w sposób random na uczenie i testy (from sklearn.model_selection import train_test_split)
X_train, X_test, y_train, y_test = train_test_split(X,  
                                                    y, 
                                                    test_size=0.2, # 0.2 - będzie 20% danych do testu, 80% do nauki
                                                    random_state=42) 

# wizualizacja
# plt.figure('Dane uczenia')
# plt.scatter(x=X_train[:, 0], y=X_train[:, 1], c=y_train, cmap=plt.cm.RdYlBu)
# plt.show(block=False)
#plt.show(block=True)
# plt.figure('Dane testowe')
# plt.scatter(x=X_test[:, 0], y=X_test[:, 1], c=y_test, cmap=plt.cm.RdYlBu)
# plt.show(block=False)
#plt.show(block=True)

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
    
model_0 = CircleModelV0().to(device)
# print(model_0)
#print(model_0.state_dict())

# print(next(model_0.parameters()).device) # info z jakiego urządzenia korzysta instancja

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# stworzenie instancji modelu w najprostrzy sposób, to jest to samo co klasa wyżej, 
# tylko w ten sposób dostaje się z automatu funkcje forward i nie można nic w niej zmienić
# model_0 = nn.Sequential(
#     nn.Linear(in_features=2, out_features=128),
#     # nn.ReLU(),
#     nn.Linear(in_features=128, out_features=1)
# ).to(device)
# print(model_0)
# print(model_0.state_dict())
# OrderedDict([
#             ('0.weight', tensor([                      # wagi dziesięciu połączeń niędzy dwoma wejściami a pierwszą warstwą pięciu neuronów
#                                 [ 0.0541,  0.0947],
#                                 [ 0.3760,  0.1158],
#                                 [ 0.3373, -0.3898],
#                                 [ 0.7012,  0.6934],
#                                 [-0.1694, -0.3135]], device='cuda:0')), 
#             ('0.bias', tensor(                        # wzmocnienie 5 neuronów pierwszej warstwy
#                                 [-0.0392,  0.5870,  0.5644,  0.2388, -0.1709], device='cuda:0')), 
#             ('1.weight', tensor([                     # wagi połączeniń między 5 neuronami pierwszej warstwy a jednym wyjściem
#                                 [-0.2709, -0.1017, -0.2575,  0.1395,  0.2672]], device='cuda:0')), 
#             ('1.bias', tensor(                        # wzmocnienie wyjścia
#                                 [0.0847], device='cuda:0'))])
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Predictions - przed treningiem
# model_0.eval()  
# with torch.inference_mode():
#     untrained_preds = model_0(X_test.to(device))
# print(torch.round(untrained_preds))  
# print(y_test)  

# wizualizacja
# plt.figure('Predictions - przed treningiem')
# plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=torch.round(untrained_preds).cpu(), cmap=plt.cm.RdYlBu)
# plt.show(block=False)
#plt.show(block=True)  

# setup loss function and optimizer
# los function mierzy jak bardzo się myli Predictions model
# optimizer - próbuje skorygować błąd zmierzony przez los function

loss_fn = nn.BCEWithLogitsLoss() # sigmoid activation function build-in
optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.1)
# optimizer = torch.optim.Adam(params=model_0.parameters(), lr=0.1)

# Obliczanie dokładności - jaka jest poprawność modelu dla 100 próbek
def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item()
    acc = (correct/len(y_pred)) * 100
    return acc

# dane do urządzenia
X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device)

# model uczenia
torch.manual_seed(42)  
epochs = 100

epoch_count = []
loss_values = []
test_loss_values = []

for epoch in range(epochs):
    
    model_0.train()

    y_logits = model_0(X_train).squeeze()
    y_pred = torch.round(torch.sigmoid(y_logits))
    
    # BCEWithLogitsLoss -> ten model wymaga y_logits
    loss = loss_fn(y_logits, y_train) 
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
        # print(test_acc)
           
    epoch_count.append(epoch)
    loss_values.append(loss)
    test_loss_values.append(test_loss)
    
# wizualizacja
plt.figure('Krzywe strat uczenia i testu.')
plt.plot(epoch_count, np.array(torch.tensor(loss_values).numpy()), label="Starty uczenie")  # wymagany casting tensor->numpy
plt.plot(epoch_count, np.array(torch.tensor(test_loss_values).numpy()), label="Starty test")  
plt.ylabel("Starty")
plt.legend()
plt.show(block=False)
#plt.show(block=True)

# wizualizacja
# plt.figure('Predictions - po treningiem')
# plt.scatter(x=X_test[:, 0].cpu(), y=X_test[:, 1].cpu(), c=test_pred.cpu(), cmap=plt.cm.RdYlBu)
# plt.show(block=False)
#plt.show(block=True) 

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("trian")
plot_decision_boundary(model_0, X_train, y_train)
plt.subplot(1, 2, 2)
plt.title("test")
plot_decision_boundary(model_0, X_test, y_test)
plt.show()
