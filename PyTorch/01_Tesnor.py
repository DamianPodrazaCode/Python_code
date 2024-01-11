import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import time

# tensor - czyli dane, w postaci skalara, wektora i tablic wielowymiarowych

print('.......................tensor scalar')
Tensor = torch.tensor(7)
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape)  
# tensor(7)

print('.......................tensor vector')
Tensor = torch.tensor([1, 3])
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape)  
# tensor([1, 3])  -  1  -  torch.Size([2])

print('.......................tensor matrix')
Tensor = torch.tensor([[1,2],
                       [3,4]])
print(Tensor, ', ilość wymiarów: ', Tensor.ndim, ', kształt wymiarów: ', Tensor.shape)  
# tensor([[1, 2],
#         [3, 4]])  -  2  -  torch.Size([2, 2])

print('....................... dostęp do danych')
print(Tensor[0])
# tensor([1, 2])
print(Tensor[1])
# tensor([3, 4])
print(Tensor[0][0])
# lub
print(Tensor[0, 0])
# tensor(1)

'''
# tensor wielowymarowy
#dwu wymiarowy
dataTensor = torch.tensor([[1,2,3], 
                           [4,5,6],
                           [7,8,9]])
print(dataTensor, ' - ', dataTensor.ndim, ' - ', dataTensor.shape) 
# tensor([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]])  -  2  -  torch.Size([3, 3])
# trój wymiarowy
dataTensor = torch.tensor([[[1,2,3],
                            [4,5,6],
                            [7,8,9]]])
print(dataTensor, ' - ', dataTensor.ndim, ' - ', dataTensor.shape) 
# tensor([[[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]])  -  3  -  torch.Size([1, 3, 3])

# dostęp
print(dataTensor[0])
# tensor([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]) 
print(dataTensor[0][0])
# tensor([1, 2, 3])
print(dataTensor[0][0][0])
# tensor(1)

# random tensors
randTensorFloat = torch.rand(3, 4) # tu podajemy wymiary tensora
print(randTensorFloat)
# tensor([[0.9781, 0.4199, 0.5948, 0.1169],
#         [0.1806, 0.2670, 0.8709, 0.2166],
#         [0.4721, 0.1201, 0.9758, 0.1681]])

randRTensorIMG = torch.rand(size = (224, 224, 3)) 
print(randRTensorIMG, ' - ', randRTensorIMG.ndim, ' - ', randRTensorIMG.shape) 

# tensor wypełniony zerami 
zeroTensor = torch.zeros(size=(5, 5))
print(zeroTensor)
# tensor([[0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.]])

# tensor wypełniony jedynkami
oneTensor = torch.ones(size=(5, 5))
print(oneTensor)
# tensor([[1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.]])
print(oneTensor.dtype) # odczytanie typu danych w tensor

print('.......................range - tensor w zakresie')
print(torch.arange(0, 10)) # int 
# tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
data = torch.arange(0., 10.) # float
print(data)
# tensor([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
print(torch.arange(0, 10, 2)) # int ze skokiem co 2
# tensor([0, 2, 4, 6, 8])

print('.......................tensor o takim samym kształcie jak wejściowy, wypełnony zerami')
dataCopy = torch.zeros_like(input=data)
print(dataCopy)
# tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

print('.......................typy danych w tensor')
float32tensor = torch.tensor([3., 4., 5.], dtype=None) # mimo ustawienia typu na none, domyślnym typem danych tensora jest float32
print(float32tensor, float32tensor.dtype) 
# tensor([3., 4., 5.]) torch.float32
float16tensor = torch.tensor([1., 2., 3.], dtype=torch.float16) 
print(float16tensor, float16tensor.dtype) 
# tensor([1., 2., 3.], dtype=torch.float16) torch.float16

dataTensor = torch.tensor([3., 4., 5.], 
                          dtype=None,
                          device="cuda",
                          requires_grad=False)
print(dataTensor, dataTensor.dtype, dataTensor.shape, dataTensor.device, dataTensor.requires_grad) 
# tensor([3., 4., 5.], device='cuda:0') torch.float32 torch.Size([3]) cuda:0 False

print('.......................operacje na tensor (dodawanie, odejmowanie, mnożenie, dzielenie, mnożenie macierzy)')
tensor = torch.tensor([1, 2, 3])
print(tensor + 10)
# tensor([11, 12, 13])
print(tensor - 10)
# tensor([-9, -8, -7])
print(tensor * 10)
# tensor([10, 20, 30])
print(tensor / 10)
# tensor([0.1000, 0.2000, 0.3000])
print(tensor * tensor)
# tensor([1, 4, 9])

print('.......................operacje wbudowane w PyTorch')
print(torch.mul(tensor, 10))
# tensor([10, 20, 30])
print(torch.add(tensor, 10))
# tensor([11, 12, 13])
print(torch.sub(tensor, 10))
# tensor([-9, -8, -7])

print('.......................mnożenie macierzy')
mA = torch.tensor([[1.,2.,3.],
                   [4.,5.,6.]], device='cpu')
mB = torch.tensor([[7.,8.],
                   [9.,10.],
                   [11.,12.]], device='cpu')
startT = time.time_ns()
mOut = torch.matmul(mA, mB) # bardzo szybka metoda !!!!!!!!!!!!!!
print(time.time_ns() - startT, '[ns]')
print(mOut)
# tensor([[ 58.,  64.],
#         [139., 154.]], device='cuda:0')
# print(mA * mB) # będzie błąd bo nie widzi tego jako macierze

print('.......................zasady mnożenie macierzy')
# Dwie główne asady mnożenia macierzy
# 1. Zewnęterzne wymiary muszą pasować
# (3, 2) @ (3, 2) nie będzie pasować
# (3, 2) @ (2, 3) będzie pasować
# (2, 3) @ (3, 2) będzie pasować
mA = torch.randint(0,10,(2,3)) #parametry (nim, max, rozmiar(2x3))
print(mA)
mB = torch.randint(0,10,(3,2))
print(mB)
print(torch.matmul(mA, mB))
# 2. Macierz wyjściowa z mnożenia ma wymiar zawsze wielkości zewnętrznych
# (3, 2) @ (2, 3) będzie (3, 3)
# (2, 3) @ (3, 2) będzie (2, 2)

print('.......................manipulacje kształtu macierzy')
mB = torch.randint(0,10,(3,2))
print(mB)
# tensor([[3, 3],
#         [2, 0],
#         [5, 4]])
print(mB.T) # przewrócenie macierzy (Transpose)
# tensor([[3, 2, 5],
#         [3, 0, 4]])

print('.......................tensor aggregation -> min, max, mean, sum')
x = torch.randint(low=0,high=100,size=([10]))
print(x)
# tensor([20, 79, 81, 67, 98, 66, 14, 44,  8, 84])
print(torch.min(x), x.min()) # dwa wykonania tej samej funkcji
# tensor(8) tensor(8)
print(torch.max(x), x.max())
# tensor(98) tensor(98)
print(torch.mean(x.type(torch.float32))) # zapis 'x.type(torch.float32)' konwertuje x do danych float32, bo tego wymaga funkcja mean
print(x.type(torch.float32).mean()) # to wyżej
#tensor(56.1000)
print(torch.sum(x), x.sum())
#tensor(561) tensor(561)

# znalezienie pierwszej pozycji 
x = torch.randint(low=0,high=100,size=([10]))
print(x)
# tensor([85, 11, 66, 19, 23, 73, 32, 97, 13, 68])
print(x.argmin())  # pozycja min
# tensor(1)
print(x.argmax())  # max
# tensor(7)

print('.......................tensor zmiany kształtu')
x = torch.arange(1., 10.)
print(x, x.shape)
# tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.]) torch.Size([9])
# Zwraca tensor z tymi samymi danymi i liczbą elementów co dane wejściowe, ale o określonym kształcie. 
# Jeśli to możliwe, zwrócony tensor będzie widokiem danych wejściowych. 
# W przeciwnym razie będzie to kopia. Ciągłe dane wejściowe i dane wejściowe o zgodnych krokach 
# można przekształcać bez kopiowania, ale nie należy polegać na zachowaniu kopiowania i przeglądania.
y = x.reshape(1, 9) # z jednowymiarowej tablicy robi dwuwymiarową
print(y, y.shape) 
# tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.]]) torch.Size([1, 9])

y = x.reshape(3, 3)
print(y, y.shape)
# tensor([[1., 2., 3.],
#         [4., 5., 6.],
#         [7., 8., 9.]]) torch.Size([3, 3])

# Zwraca nowy tensor z tymi samymi danymi co własny tensor, ale o innym kształcie.
y = x.view(-1, 3) # he size -1 is inferred from other dimensions, czyli jest (3, 3)
print(y, y.shape) 
print(x, x.shape) 
# tensor([[1., 2., 3.],
#         [4., 5., 6.],
#         [7., 8., 9.]]) torch.Size([3, 3])
# tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.]) torch.Size([9])

# łączenie wielu tensorów, jażeli dim=0 to układa w wiersze, a jak dim-1 to w kolumny
z = torch.stack([x, x, x, x], dim=1)
print(z)
# dim=0
# tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.],
#         [1., 2., 3., 4., 5., 6., 7., 8., 9.],
#         [1., 2., 3., 4., 5., 6., 7., 8., 9.],
#         [1., 2., 3., 4., 5., 6., 7., 8., 9.]])
# dim=1
# tensor([[1., 1., 1., 1.],
#         [2., 2., 2., 2.],
#         [3., 3., 3., 3.],
#         [4., 4., 4., 4.],
#         [5., 5., 5., 5.],
#         [6., 6., 6., 6.],
#         [7., 7., 7., 7.],
#         [8., 8., 8., 8.],
#         [9., 9., 9., 9.]])

# torch.squezze() - ściskanie matrixów
x = x.reshape(1, 9)
print(x, x.shape)
# tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.]]) torch.Size([1, 9])

x = x.squeeze() # spowoduje że przestanie być tablicą dwu wymiarową taj jak wyżej, usuwa pojedyncze wymiary
print(x, x.shape)
# tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.]) torch.Size([9])

# dodanie extra wymiaru
x = x.unsqueeze(dim=0) # dim=0 wymiar na początku, dim=1 wymiar na końcu
print(x, x.shape)
#dla dim=0
#tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.]]) torch.Size([1, 9])
#dla dim=1
# tensor([[1.],
#         [2.],
#         [3.],
#         [4.],
#         [5.],
#         [6.],
#         [7.],
#         [8.],
#         [9.]]) torch.Size([9, 1])

# mieszanie wymiarami
img = torch.rand(size=(100,80,3))
print(img, img.shape)
imgp = img.permute(2,0,1) #przestawia w kształcie pole 2(3) nz pole 0, pole 0(100) na pole 1, pole 1(80) na pole 2, czyli (3,100,80)
print(imgp, imgp.shape)

# dostęp do danych przez indexing
x = torch.arange(1, 10).reshape(1, 3, 3)
print(x, x.shape)
# tensor([[[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]]) torch.Size([1, 3, 3])

print(x[0]) # pierwszy wymiar
# tensor([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]])

print(x[0][0]) # można też tak print(x[0, 0])
# tensor([1, 2, 3])

print(x[0][0][0])
# tensor(1)

# Można urzyć ":" żeby mieć dostęp do całego wymiaru
print(x[:, :, 0])
# tensor([[1, 4, 7]])
print(x[:, 0])
# tensor([[1, 2, 3]])
print(x[:, 1, 1])
# tensor([5])
print(x[0, 0, :])
# tensor([1, 2, 3])

# NumPy to tensor
array = np.arange(1., 8.)
tensor = torch.from_numpy(array) 
# tensor = torch.from_numpy(array).type(torch.float32) # konwersja do float32
print(array)
# [1. 2. 3. 4. 5. 6. 7.]
print(tensor)
# tensor([1., 2., 3., 4., 5., 6., 7.], dtype=torch.float64)

array = array + 1 # jak dodamy, to zmiana w array nie wpłynie na tensor
array[0] = 12
print(array)
print(tensor)

#tensor to NumPy
tensor = torch.ones(7)
numpy_from_tensor = tensor.numpy()
print(tensor, tensor.dtype)
# tensor([1., 1., 1., 1., 1., 1., 1.]) torch.float32
print(numpy_from_tensor, numpy_from_tensor.dtype)
# [1. 1. 1. 1. 1. 1. 1.] float32

'''