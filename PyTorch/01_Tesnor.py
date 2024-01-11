import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import time

# tensor - czyli dane, w postaci skalara, wektora i tablic wielowymiarowych

print('.......................tensor scalar')
Tensor = torch.tensor(7)
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape)  
# tensor(7) , ilość wymiarów:  0 , kształt wymiarów:  torch.Size([])

print('.......................tensor vector')
Tensor = torch.tensor([1, 3])
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape)  
# tensor([1, 3]) , ilość wymiarów:  1 , kształt wymiarów:  torch.Size([2])

print('.......................tensor matrix, dwu wymiarowy')
Tensor = torch.tensor([[1, 2],
                       [3, 4]])
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape)  
# tensor([[1, 2],
#         [3, 4]]) , ilość wymiarów:  2 , kształt wymiarów:  torch.Size([2, 2])

print('....................... trój wymiarowy')
Tensor = torch.tensor([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]])
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape)  
# tensor([[[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]]) , ilość wymiarów:  3 , kształt wymiarów:  torch.Size([1, 3, 3])

print('....................... dostęp do danych przez indexing')
print(Tensor[0], Tensor[0].shape)
# tensor([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]) torch.Size([3, 3]) - wynikiem jest pierwsza tablica dwuwymiarowa

print(Tensor[0][0], Tensor[0][0].shape) # lub print(Tensor[0, 0])
# tensor([1, 2, 3]) torch.Size([3]) - wynikiem jest pierwsza tablica jednomwymiarowa z pierwszej tablicy dwuwymiarowej

print(Tensor[0][0][0], Tensor[0][0][0].shape) # lub print(Tensor[0, 0, 0])
# tensor(1) torch.Size([]) - wynikiem nie jest tablica tylko element

# Można urzyć ":" żeby mieć dostęp do całego wymiaru
print(Tensor.shape)
# torch.Size([1, 3, 3])
print(Tensor[:, :, 0]) # z całego wymiaru trzeciego, z całego wymiaru x, z lini 0 y
# tensor([[1, 4, 7]])
print(Tensor[:, 0]) # z całego wymiaru trzeciego, z lini 0 x
# tensor([[1, 2, 3]])
print(Tensor[:, 1, 1]) # z całego wymiaru trzeciego, z wiersza x = 1, z lini y = 1, tensor w postaci jednowymiarowej a nie elementu
# tensor([5])
print(Tensor[0, 0, :]) # z całego wymiaru trzeciego, z lini 0 x
# tensor([1, 2, 3])

print('\n-------------------------------------------------------------------------------')
print('....................... random tensors float32')
Tensor = torch.rand(3, 4) # tu podajemy wymiary tensora
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape, 'typ danych', Tensor.dtype)  
# tensor([[0.9781, 0.4199, 0.5948, 0.1169],
#         [0.1806, 0.2670, 0.8709, 0.2166],
#         [0.4721, 0.1201, 0.9758, 0.1681]]) , ilość wymiarów:  2 , kształt wymiarów:  torch.Size([3, 4]) typ danych torch.float32

# Tensor = torch.rand(size = (224, 224, 3)) 
# print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape, 'typ danych', Tensor.dtype)  

print('....................... tensor wypełniony zerami')
Tensor = torch.zeros(size = (5, 5))
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape, 'typ danych', Tensor.dtype)  
# tensor([[0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.]]), ilość wymiarów:  2 , kształt wymiarów:  torch.Size([5, 5]) typ danych torch.float32

print('....................... tensor wypełniony jedynkami')
Tensor = torch.ones(size=(5, 5))
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape, 'typ danych', Tensor.dtype)
# tensor([[1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.]]), ilość wymiarów:  2 , kształt wymiarów:  torch.Size([5, 5]) typ danych torch.float32

print('.......................arange - tensor w zakresie')
Tensor = torch.arange(0, 10) # int 
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape, 'typ danych', Tensor.dtype)
# tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) , ilość wymiarów:  1 , kształt wymiarów:  torch.Size([10]) typ danych torch.int64

Tensor = torch.arange(0., 10.) # float
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape, 'typ danych', Tensor.dtype)
# tensor([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]) , ilość wymiarów:  1 , kształt wymiarów:  torch.Size([10]) typ danych torch.float32

Tensor = torch.arange(0, 10, 2) # int ze skokiem co 2
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape, 'typ danych', Tensor.dtype)
# tensor([0, 2, 4, 6, 8]) , ilość wymiarów:  1 , kształt wymiarów:  torch.Size([5]) typ danych torch.int64

print('.......................tensor o takim samym kształcie jak wejściowy, wypełnony zerami')
Tensor_tmp = torch.zeros_like(input = Tensor)
print(Tensor_tmp, ', ilość wymiarów: ', Tensor_tmp.ndim, ', kształt wymiarów: ', Tensor_tmp.shape, 'typ danych', Tensor_tmp.dtype)
# tensor([0, 0, 0, 0, 0]) , ilość wymiarów:  1 , kształt wymiarów:  torch.Size([5]) typ danych torch.int64

print('.......................typy danych w tensor')
Tensor = torch.tensor([3., 4., 5.], dtype = None) # mimo ustawienia typu na none, domyślnym typem danych tensora jest float32
print(Tensor, Tensor.dtype) 
# tensor([3., 4., 5.]) torch.float32
Tensor = torch.tensor([1., 2., 3.], dtype=torch.float16) 
print(Tensor, Tensor.dtype) 
# tensor([1., 2., 3.], dtype=torch.float16) torch.float16

print('.......................tensor dane w CUDA')
Tensor = torch.tensor([3., 4., 5.], 
                          dtype=None,
                          device="cuda",
                          requires_grad=False)
print(Tensor, Tensor.dtype, Tensor.shape, Tensor.device, Tensor.requires_grad) 
# tensor([3., 4., 5.], device='cuda:0') torch.float32 torch.Size([3]) cuda:0 False

print('\n-------------------------------------------------------------------------------')
print('.......................operacje na tensor (dodawanie, odejmowanie, mnożenie, dzielenie, mnożenie macierzy)')
Tensor = torch.tensor([1, 2, 3])
print(Tensor + 10)
# tensor([11, 12, 13])
print(Tensor - 10)
# tensor([-9, -8, -7])
print(Tensor * 10)
# tensor([10, 20, 30])
print(Tensor / 10)
# tensor([0.1000, 0.2000, 0.3000])
print(Tensor * Tensor)
# tensor([1, 4, 9])

print('.......................operacje wbudowane w PyTorch')
print(torch.mul(Tensor, 10))
# tensor([10, 20, 30])
print(torch.add(Tensor, 10))
# tensor([11, 12, 13])
print(torch.sub(Tensor, 10))
# tensor([-9, -8, -7])

print('.......................mnożenie macierzy')
mA = torch.tensor([[1., 2., 3.],
                   [4., 5., 6.]])
mB = torch.tensor([[7., 8.],
                   [9., 10.],
                   [11., 12.]])
print(torch.matmul(mA, mB))
# jw. torch.mm(mA, mB)
# tensor([[ 58.,  64.],
#         [139., 154.]])
# print(mA * mB) # będzie błąd bo nie widzi tego jako macierze

print('.......................zasady mnożenie macierzy')
# Dwie główne zasady mnożenia macierzy
# 1. Zewnęterzne wymiary muszą być takie same
# (3, 2) @ (3, 2) nie będzie pasować
# (3, 2) @ (2, 3) będzie pasować
# (2, 3) @ (3, 2) będzie pasować
mA = torch.randint(0, 10, size = (2, 3)) #parametry (nim, max, rozmiar(2x3))
print('macierz mA', mA)
mB = torch.randint(0, 10, size = (3, 2))
print('macierz mB', mB)
print('mA * mB', torch.matmul(mA, mB))
# 2. Macierz wyjściowa z mnożenia ma wymiar zawsze wielkości zewnętrznych
# (3, 2) @ (2, 3) będzie (3, 3)
# (2, 3) @ (3, 2) będzie (2, 2)


print('\n-------------------------------------------------------------------------------')
print('.......................przewrócenie macierzy - Transpose')
Tensor = torch.randint(0, 10, size = (3, 2))
print(Tensor)
# tensor([[3, 3],
#         [2, 0],
#         [5, 4]])
print(Tensor.T) # przewrócenie macierzy
# tensor([[3, 2, 5],
#         [3, 0, 4]])

print('.......................tensor aggregation -> min, max, mean, sum')
Tensor = torch.randint(low = 0, high = 100, size = ([10])) 
print(Tensor)
# tensor([20, 79, 81, 67, 98, 66, 14, 44,  8, 84])
print(torch.min(Tensor), Tensor.min()) # dwa wykonania tej samej funkcji
# tensor(8) tensor(8)
print(torch.max(Tensor), Tensor.max())
# tensor(98) tensor(98)
print(torch.mean(Tensor.type(torch.float32))) # zapis 'Tensor.type(torch.float32)' konwertuje Tensor do danych float32, bo tego wymaga funkcja mean
print(Tensor.type(torch.float32).mean()) # to co wyżej
#tensor(56.1000)
print(torch.sum(Tensor), Tensor.sum())
#tensor(561) tensor(561)

print('....................... znalezienie pierwszej pozycji: min, max')
Tensor = torch.randint(low = 0, high = 100, size = ([10]))
print(Tensor)
# tensor([85, 11, 66, 19, 23, 73, 32, 97, 13, 68])
print(Tensor.argmin())  # index min
# tensor(1)
print(Tensor.argmax())  # index max
# tensor(7)

print('.......................tensor zmiany kształtu')
Tensor = torch.arange(1., 10.)
print(Tensor, Tensor.shape)
# tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.]) torch.Size([9])
# Zwraca tensor z tymi samymi danymi i liczbą elementów co dane wejściowe, ale o określonym kształcie. 
# Jeśli to możliwe, zwrócony tensor będzie widokiem danych wejściowych, bezie dotyczyć tej samej pamięci. 
# W przeciwnym razie będzie to kopia. Ciągłe dane wejściowe i dane wejściowe o zgodnych krokach 
# można przekształcać bez kopiowania, ale nie należy polegać na zachowaniu kopiowania i przeglądania.
Tensor = Tensor.reshape(1, 9) # z jednowymiarowej tablicy robi dwuwymiarową
print(Tensor, Tensor.shape) 
# tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.]]) torch.Size([1, 9])

Tensor = Tensor.reshape(3, 3)
print(Tensor, Tensor.shape)
# tensor([[1., 2., 3.],
#         [4., 5., 6.],
#         [7., 8., 9.]]) torch.Size([3, 3])

Tensor = Tensor.reshape(9) # zpowrotem na jednowymiarową
print(Tensor, Tensor.shape) 
# tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.]) torch.Size([9])

# Zwraca nowy tensor z tymi samymi danymi co własny tensor, ale o innym kształcie.
Tensor_tmp = Tensor.view(-1, 3) # size -1 oznacza że dopasuje kolumny, czyli jest (3, 3)
print(Tensor_tmp, Tensor_tmp.shape) 
print(Tensor, Tensor.shape) 
# tensor([[1., 2., 3.],
#         [4., 5., 6.],
#         [7., 8., 9.]]) torch.Size([3, 3])
# tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.]) torch.Size([9])

print('....................... łączenie wielu tensorów, jażeli dim = 0 to układa w wiersze, a jak dim = 1 to w kolumny')
z = torch.stack([Tensor, Tensor, Tensor, Tensor], dim = 1)
print(z)
# dim = 0
# tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.],
#         [1., 2., 3., 4., 5., 6., 7., 8., 9.],
#         [1., 2., 3., 4., 5., 6., 7., 8., 9.],
#         [1., 2., 3., 4., 5., 6., 7., 8., 9.]])
# dim = 1
# tensor([[1., 1., 1., 1.],
#         [2., 2., 2., 2.],
#         [3., 3., 3., 3.],
#         [4., 4., 4., 4.],
#         [5., 5., 5., 5.],
#         [6., 6., 6., 6.],
#         [7., 7., 7., 7.],
#         [8., 8., 8., 8.],
#         [9., 9., 9., 9.]])

print('....................... torch.squezze() - ściskanie matrixów, usuwanie pojedynczych wymiarów')
Tensor = Tensor.reshape(1, 9)
print(Tensor, Tensor.shape)
# tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.]]) torch.Size([1, 9])

Tensor = Tensor.squeeze() # spowoduje że przestanie być tablicą dwu wymiarową taj jak wyżej, usuwa pojedyncze wymiary
print(Tensor, Tensor.shape)
# tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.]) torch.Size([9])

print('.......................  dodanie extra wymiaru')
Tensor = Tensor.unsqueeze(dim = 1) # dim = 0 wymiar na początku, dim = 1 wymiar na końcu
print(Tensor, Tensor.shape)
#dla dim = 0
#tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.]]) torch.Size([1, 9])
#dla dim = 1
# tensor([[1.],
#         [2.],
#         [3.],
#         [4.],
#         [5.],
#         [6.],
#         [7.],
#         [8.],
#         [9.]]) torch.Size([9, 1])

print('.......................  mieszanie wymiarami')
Tensor = torch.rand(size=(3, 4, 2))
print(Tensor, Tensor.shape)
Tensor_tmp = Tensor.permute(2, 0, 1) #przestawia w kształcie pole 2(3) nz pole 0, pole 0(100) na pole 1, pole 1(80) na pole 2, czyli shape to(2, 3, 4)
print(Tensor_tmp, Tensor_tmp.shape)

print('\n-------------------------------------------------------------------------------')
print('....................... NumPy do tensor')
array = np.arange(1., 8.) # dekleracja w NumPy, typ danych w float64
Tensor = torch.from_numpy(array) # Tensor otrzymuje float64
# tensor = torch.from_numpy(array).type(torch.float32) # konwersja do float32
print(array)
# [1. 2. 3. 4. 5. 6. 7.]
print(Tensor)
# tensor([1., 2., 3., 4., 5., 6., 7.], dtype=torch.float64)

array = array + 1 # jak dodamy, to zmiana w array nie wpłynie na tensor,
array[0] = 12 # a to wpłynie na obydwie tablice jak niebędzie operacji wyżej ????????????
print(array)
print(Tensor)

print('....................... tensor do NumPy')
Tensor = torch.ones(7)
numpy_from_tensor = Tensor.numpy()
print(Tensor, Tensor.dtype)
# tensor([1., 1., 1., 1., 1., 1., 1.]) torch.float32
print(numpy_from_tensor, numpy_from_tensor.dtype)
# [1. 1. 1. 1. 1. 1. 1.] float32

