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
matryca = torch.tensor([[1,2],
                        [3,4]])
print(matryca, ' - ', matryca.ndim, ' - ', matryca.shape) 
# >>> tensor([[1, 2],
#             [3, 4]])  -  2  -  torch.Size([2, 2])

# dostęp do danych
print(matryca[0])
# >>> tensor([1, 2])
print(matryca[1])
# >>> tensor([3, 4])

# tensor
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

# tensor wypełniony zerami albo jedynkami
zeroTensor = torch.zeros(size=(5, 5))
print(zeroTensor)
'''
tensor([[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]])
'''

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