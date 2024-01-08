import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

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

# range - tensor w zakresie
print(torch.arange(0, 10)) # int 
# >>> tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
data = torch.arange(0., 10.) # float
print(data)
# >>> tensor([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
print(torch.arange(0, 10, 2)) # int ze skokiem co 2
# >>> tensor([0, 2, 4, 6, 8])

# tensor o takim samym kształcie jak wejściowy, wypełnony zerami
dataCopy = torch.zeros_like(input=data)
print(dataCopy)
# >>> tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

# typy danych w tensor
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

# operacje na tensor (dodawanie, odejmowanie, mnożenie, dzielenie, mnożenie macierzy)

