import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import time

# tensor - czyli dane IO

# scalar
scalar = torch.tensor(7)
print(scalar)  
# >>> tensor(7)

# vector
wektor = torch.tensor([1, 3])
print(wektor, ' - ', wektor.ndim, ' - ', wektor.shape)  
# >>> tensor([1, 3])  -  1  -  torch.Size([2])
# ndim - ilość wymiarów
# shape - kształt wymiarów

# matrix
macierz = torch.tensor([[1,2],
                        [3,4]])
print(macierz, ' - ', macierz.ndim, ' - ', macierz.shape) 
# >>> tensor([[1, 2],
#             [3, 4]])  -  2  -  torch.Size([2, 2])

# dostęp do danych
print(macierz[0])
# >>> tensor([1, 2])
print(macierz[1])
# >>> tensor([3, 4])

# tensor wielowymarowy
dataTensor = torch.tensor([[[1,2,3],
                            [4,5,6],
                            [7,8,9]]])
print(dataTensor, ' - ', dataTensor.ndim, ' - ', dataTensor.shape) 
# >>> tensor([[[1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9]]])  -  3  -  torch.Size([1, 3, 3])

# dostęp
print(dataTensor[0])
# >>> tensor([[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]])
print(dataTensor[0][0])
# >>> tensor([1, 2, 3])
print(dataTensor[0][0][0])
# >>> tensor(1)

# random tensors
randTensorFloat = torch.rand(3, 4) # tu podajemy wymiary tensora
print(randTensorFloat)
# >>> tensor([[0.9781, 0.4199, 0.5948, 0.1169],
#             [0.1806, 0.2670, 0.8709, 0.2166],
#             [0.4721, 0.1201, 0.9758, 0.1681]])

randRTensorIMG = torch.rand(size = (224, 224, 3)) 
print(randRTensorIMG, ' - ', randRTensorIMG.ndim, ' - ', randRTensorIMG.shape) 

# tensor wypełniony zerami 
zeroTensor = torch.zeros(size=(5, 5))
print(zeroTensor)
'''
tensor([[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]])
'''

# tensor wypełniony jedynkami
oneTensor = torch.ones(size=(5, 5))
print(oneTensor)
'''
tensor([[1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.],
        [1., 1., 1., 1., 1.]])
'''
print(oneTensor.dtype) # odczytanie typu danych w tensor

print('.......................range - tensor w zakresie')
print(torch.arange(0, 10)) # int 
# >>> tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
data = torch.arange(0., 10.) # float
print(data)
# >>> tensor([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
print(torch.arange(0, 10, 2)) # int ze skokiem co 2
# >>> tensor([0, 2, 4, 6, 8])

print('.......................tensor o takim samym kształcie jak wejściowy, wypełnony zerami')
dataCopy = torch.zeros_like(input=data)
print(dataCopy)
# >>> tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

print('.......................typy danych w tensor')
float32tensor = torch.tensor([3., 4., 5.], dtype=None) # mimo ustawienia typu na none, domyślnym typem danych tensora jest float32
print(float32tensor, float32tensor.dtype) 
# >>> tensor([3., 4., 5.]) torch.float32
float16tensor = torch.tensor([1., 2., 3.], dtype=torch.float16) 
print(float16tensor, float16tensor.dtype) 
# >>> tensor([1., 2., 3.], dtype=torch.float16) torch.float16

dataTensor = torch.tensor([3., 4., 5.], 
                          dtype=None,
                          device="cuda",
                          requires_grad=False)
print(dataTensor, dataTensor.dtype, dataTensor.shape, dataTensor.device, dataTensor.requires_grad) 
# >>> tensor([3., 4., 5.], device='cuda:0') torch.float32 torch.Size([3]) cuda:0 False

print('.......................operacje na tensor (dodawanie, odejmowanie, mnożenie, dzielenie, mnożenie macierzy)')
tensor = torch.tensor([1, 2, 3])
print(tensor + 10)
# >>> tensor([11, 12, 13])
print(tensor - 10)
# >>> tensor([-9, -8, -7])
print(tensor * 10)
# >>> tensor([10, 20, 30])
print(tensor / 10)
# >>> tensor([0.1000, 0.2000, 0.3000])
print(tensor * tensor)
# >>> tensor([1, 4, 9])

print('.......................operacje wbudowane w PyTorch')
print(torch.mul(tensor, 10))
# >>> tensor([10, 20, 30])
print(torch.add(tensor, 10))
# >>> tensor([11, 12, 13])
print(torch.sub(tensor, 10))
# >>> tensor([-9, -8, -7])

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
# >>> tensor([[ 58.,  64.],
#             [139., 154.]], device='cuda:0')
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
