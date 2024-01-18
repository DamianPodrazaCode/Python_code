import torch
from torch import nn

# definicja urządzenia obliczającego
device = 'cuda'
#device = 'cpu'

# ------------------------------------------------------------------------------------------------------------------
# tworzenie klasy sieci nn liniowej (nn.Linear -> y = ax + b)
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        
        # warstwy sieci neuronowej, takich warstw może być wiele, ogranicza to tylko prędkość sprzętu i pamięć
        self.layer_1 = nn.Linear(in_features=1, out_features=16) # jedno wejście do sieci, 16 wyjść do neuronów (wejść do sieci może być wiele w zależności odanych wejściowych)
        self.layer_2 = nn.Linear(in_features=16, out_features=16) # 16 wejść do neuronów, 16 wyjść do kolejnych neuronów (neuronów w sieciach ukrytych, może być wiele, przyspiesza to obliczenia kosztem wykozystania sprzętu, zaleca się potęgę 2)
        self.layer_3 = nn.Linear(in_features=16, out_features=1) # 16 wejść do neuronów, 1 wyjście z sieci 
        
    # funkcja układająca kolejność działania w sieci
    def forward(self, x):
        return self.layer_3(self.layer_2(self.layer_1(x)))
    # x -> layer_1 -> layer_2 -> layer_3 -> out
# tworzenie instancji i przesłanie jej do urządzenie obliczającego
model0 = LinearModel().to(device)

# tworzenie instancji za pomocą sekwencji
model1 = nn.Sequential(
    nn.Linear(in_features=1, out_features=16),      # x -> layer_1 ->
    nn.Linear(in_features=16, out_features=16),     # layer_1 -> layer_2 ->
    nn.Linear(in_features=16, out_features=1)       # layer_2 -> out
).to(device)
# tworzona jest odrazu instancja sieci wraz z kolejnością jej działania, czyli ten zapis całkowicie zastępuje poprzedni, nie trzeba tworzyć klasy

# ------------------------------------------------------------------------------------------------------------------
# tworzenie klasy sieci nn nie liniowej
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        
        # warstwy sieci neuronowej, takich warstw może być wiele, ogranicza to tylko prędkość sprzętu i pamięć
        self.layer_1 = nn.Linear(in_features=1, out_features=16) # jedno wejście do sieci, 16 wyjść do neuronów (wejść do sieci może być wiele w zależności odanych wejściowych)
        self.layer_2 = nn.Linear(in_features=16, out_features=16) # 16 wejść do neuronów, 16 wyjść do kolejnych neuronów (neuronów w sieciach ukrytych, może być wiele, przyspiesza to obliczenia kosztem wykozystania sprzętu, zaleca się potęgę 2)
        self.layer_3 = nn.Linear(in_features=16, out_features=1) # 16 wejść do neuronów, 1 wyjście z sieci 
        self.relu = nn.ReLU() # nie liniowa funkcja aktywacji
        
    # funkcja układająca kolejność działania w sieci
    def forward(self, x):
        return self.layer_3(self.relu(self.layer_2(self.relu(self.layer_1(x)))))
    # x -> layer_1 -> relu -> layer_2 -> relu -> layer_3 -> out
# tworzenie instancji i przesłanie jej do urządzenie obliczającego
model2 = LinearModel().to(device)

# tworzenie instancji za pomocą sekwencji
model3 = nn.Sequential(
    nn.Linear(in_features=1, out_features=16),      # x -> layer_1 ->
    nn.ReLU(),                                           
    nn.Linear(in_features=16, out_features=16),     # layer_1 -> layer_2 ->
    nn.ReLU(),
    nn.Linear(in_features=16, out_features=1)       # layer_2 -> out
).to(device)
# tworzona jest odrazu instancja sieci wraz z kolejnością jej działania, czyli ten zapis całkowicie zastępuje poprzedni, nie trzeba tworzyć klasy

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
