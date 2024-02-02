import numpy as np
# -----------------------------------------------------------------------------
# DataTypes & Attributes

a1 = np.array([1, 2, 3])
print(a1)
#[1 2 3]

print(type(a1))
# <class 'numpy.ndarray'>

a2 = np.array([[1, 2.0, 3.2],
               [4, 5,   6.4]])

a3 = np.array([[[1,2,3],
                [4,5,6],
                [7,8,9]],
               [[10,11,12],
                [13,14,15],
                [16,17,18]]])

print(a2)
# [[1.  2.  3.2]
#  [4.  5.  6.4]]

print(a3)
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]
#
#  [[10 11 12]
#   [13 14 15]
#   [16 17 18]]]

# axis=0 -> to y
# axis=1 -> to x
# axis=n -> to kolejne wymiary

print(a1.shape, a2.shape, a3.shape) # kształt
# (3,) (2, 3) (2, 3, 3)

print(a1.ndim, a2.ndim, a3.ndim) # ilość wymiarów
# 1 2 3

print(a1.dtype, a2.dtype, a3.dtype)
# int32 float64 int32

print(a1.size, a2.size, a3.size)
# 3 6 18

print(type(a1),type(a2),type(a3))
# <class 'numpy.ndarray'> <class 'numpy.ndarray'> <class 'numpy.ndarray'>

# -----------------------------------------------------------------------------
# Create a DataFrame from NumPy array
import pandas as pd
df = pd.DataFrame(a2)
print(df)
#      0    1    2
# 0  1.0  2.0  3.2
# 1  4.0  5.0  6.4

# -----------------------------------------------------------------------------
# Create arrays

sample_array = np.array([1, 2, 3])
print(sample_array)
# [1 2 3]
print(sample_array.dtype)
# int32

ones = np.ones((2, 3))
print(ones)
# [[1. 1. 1.]
#  [1. 1. 1.]]
print(ones.dtype)
# float64

zeros = np.zeros((2, 3))
print(zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]]

range_array = np.arange(0, 10, 2)
print(range_array)
# [0 2 4 6 8]

random_array = np.random.randint(0, 10, size=(3, 5))
print(random_array)
# [[8 6 4 6 9]
#  [3 9 7 1 7]
#  [8 7 6 9 9]]

print(np.random.random((5, 5)))
# [[0.85899443 0.56961315 0.34995295 0.03209657 0.39887244]
#  [0.90449937 0.90277167 0.52767459 0.38328488 0.72560342]
#  [0.07124479 0.13749627 0.78805935 0.99344739 0.20417705]
#  [0.78331081 0.48316437 0.59691352 0.38285312 0.27722661]
#  [0.40673424 0.29334718 0.03592001 0.75726255 0.91216435]]

random_array_2 = np.random.rand(5, 5) # to samo co wyżej
print(random_array_2)
# [[0.82671193 0.84860283 0.49914845 0.04560998 0.9403263 ]
#  [0.06681904 0.24817085 0.85349467 0.43214257 0.58841649]
#  [0.51111513 0.58391288 0.73086755 0.15116362 0.73037423]
#  [0.16272827 0.63117529 0.25642133 0.78441794 0.3330818 ]
#  [0.2644563  0.63975634 0.30347297 0.66837973 0.24641568]]

random_array_3 = np.random.rand(3, 3, 3)
print(random_array_3)
# [[[0.96291304 0.89945447 0.43265817]
#   [0.69793839 0.22826055 0.91699586]
#   [0.61214018 0.05342201 0.56591243]]

#  [[0.08661551 0.8293766  0.64475977]
#   [0.58876264 0.5400476  0.13925676]
#   [0.85854486 0.24138912 0.14744366]]

#  [[0.57118499 0.32548805 0.26507872]
#   [0.31321697 0.3000298  0.75592489]
#   [0.33796397 0.43105189 0.00103795]]]

# -----------------------------------------------------------------------------
# Pseudo-random numbers
# Random Seed

np.random.seed(seed=42) # stały start random
random_array_4 = np.random.randint(10, size=(5, 3))
print(random_array_4)
# [[6 3 7]
#  [4 6 9]
#  [2 6 7]
#  [4 3 7]
#  [7 2 5]]

random_array_5 = np.random.rand(3, 3)
print(random_array_5)
# [[5.64115790e-02 7.21998772e-01 9.38552709e-01]
#  [7.78765841e-04 9.92211559e-01 6.17481510e-01]
#  [6.11653160e-01 7.06630522e-03 2.30624250e-02]]

# -----------------------------------------------------------------------------

# viewing arraus, matrices

print(random_array_4) 
# [[6 3 7]
#  [4 6 9]
#  [2 6 7]
#  [4 3 7]
#  [7 2 5]]

print(np.unique(random_array_4)) # wyświetlenie jakie są niepowtarzalne elementy w tablicy
# [2 3 4 5 6 7 9]

print('\n', a1, '\n\n', a2, '\n\n', a3)
#  [1 2 3]

#  [[1.  2.  3.2]
#  [4.  5.  6.4]]

#  [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]
#
#  [[10 11 12]
#   [13 14 15]
#   [16 17 18]]]

print(a1[0])
# 1

print(a2[0])
# [1.  2.  3.2]

print(a3[0])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(a3[:2, :2, :2]) # wyświetl do drugiej kolumny, drugiego wiersza i drugiego poziomu
# [[[ 1  2]
#   [ 4  5]]

#  [[10 11]
#   [13 14]]]

a4 = np.random.randint(10, size=(2, 3, 4, 5))
print(a4)
# [[[[9 2 6 3 8]
#    [2 4 2 6 4]
#    [8 6 1 3 8]
#    [1 9 8 9 4]]

#   [[1 3 6 7 2]
#    [0 3 1 7 3]
#    [1 5 5 9 3]
#    [5 1 9 1 9]]

#   [[3 7 6 8 7]
#    [4 1 4 7 9]
#    [8 8 0 8 6]
#    [8 7 0 7 7]]]


#  [[[2 0 7 2 2]
#    [0 4 9 6 9]
#    [8 6 8 7 1]
#    [0 6 6 7 4]]

#   [[2 7 5 2 0]
#    [2 4 2 0 4]
#    [9 6 6 8 9]
#    [9 2 6 0 3]]

#   [[3 4 6 6 3]
#    [6 2 5 1 9]
#    [8 4 5 3 9]
#    [6 8 6 0 0]]]]

print(a4[:, :, :, :4])
# [[[[9 2 6 3]
#    [2 4 2 6]
#    [8 6 1 3]
#    [1 9 8 9]]

#   [[1 3 6 7]
#    [0 3 1 7]
#    [1 5 5 9]
#    [5 1 9 1]]

#   [[3 7 6 8]
#    [4 1 4 7]
#    [8 8 0 8]
#    [8 7 0 7]]]


#  [[[2 0 7 2]
#    [0 4 9 6]
#    [8 6 8 7]
#    [0 6 6 7]]

#   [[2 7 5 2]
#    [2 4 2 0]
#    [9 6 6 8]
#    [9 2 6 0]]

#   [[3 4 6 6]
#    [6 2 5 1]
#    [8 4 5 3]
#    [6 8 6 0]]]]

# -----------------------------------------------------------------------------
# Manipulate arrays

print(a1)
# [1 2 3]

print(a1 + 1)
# [2 3 4]

ones = np.ones(3)
print(ones)
# [1. 1. 1.]

print(a1 + ones)
# [2. 3. 4.]

print(a1 - ones)
# [0. 1. 2.]

print(a2)
# [[1.  2.  3.2]
#  [4.  5.  6.4]]

print(a1 * a2)
# [[ 1.   4.   9.6]
#  [ 4.  10.  19.2]]

print(a1 / ones)
# [1. 2. 3.]

print(a2 / a1)
# [[1.         1.         1.06666667]
#  [4.         2.5        2.13333333]]

print(a2 // a1) # dzielenie bez reszt (obcinanie do dołu)
# [[1. 1. 1.]
#  [4. 2. 2.]]

print(a2 ** 2) # potęga 2
# [[ 1.    4.   10.24]
#  [16.   25.   40.96]]

print(np.square(a2)) # też potęga 2
# [[ 1.    4.   10.24]
#  [16.   25.   40.96]]

print(np.add(a1, a2))
# [[2.  4.  6.2]
#  [5.  7.  9.4]]

print(a2 % a1) # reszta z dzielenia
# [[0.  0.  0.2]
#  [0.  1.  0.4]]

print(np.exp(a1))
# [ 2.71828183  7.3890561  20.08553692]

print(np.log(a1))
# [0.         0.69314718 1.09861229]

# -----------------------------------------------------------------------------
# Aggregation

listy_list = [1, 2, 3]
print(type(listy_list))
# <class 'list'>

print(sum(listy_list))
# 6

print(a1)
# [1 2 3]
print(sum(a1))
# 6
print(np.sum(a1))
# 6
# taki sam wynik, ale powinno się używać metod numpy na danych numpy, a metod pythona na danych pythona

# wielkie tablice
massive_array = np.random.random(1000000)
print(massive_array.size)
# 100000

print(massive_array[:10])
# [0.22793516 0.42710779 0.81801477 0.86073058 0.00695213 0.5107473
#  0.417411   0.22210781 0.11986537 0.33761517]

import time
start = time.time()
sum(massive_array)
end = time.time()
print(end - start)
# 0.09500288963317871 [s]
# 95 [ms]

start = time.time()
np.sum(massive_array)
end = time.time()
print(end - start)
# 0.0020046234130859375 [s]
# 2 [ms]

print(a2)
# [[1.  2.  3.2]
#  [4.  5.  6.4]]

print(np.mean(a2)) # średnia tablicy
# 3.6

# Standard deviation (standardowe odchylenie) to miara rozproszenia danych wokół ich średniej arytmetycznej. Jest to jedna z najczęściej używanych miar w statystyce.
# Standard deviation jest obliczane jako pierwiastek kwadratowy wariancji. 
# Wariancja mierzy, jak bardzo dane różnią się od średniej, a standard deviation dostarcza miary tego rozrzutu w jednostkach oryginalnych danych.
print(np.std(a2)) # standardowe odchylenie
# 1.8

# Wariancja (Variance) - W statystyce wariancja to miara, która określa, 
# jak bardzo wartości zbioru danych różnią się od średniej arytmetycznej tych wartości. 
# Im większa wariancja, tym większe są różnice między poszczególnymi wartościami a średnią.
print(np.var(a2)) # variance 
# 3.24

print(np.sqrt(np.var(a2))) # standardowe odchylenie
# 1.8

# -----------------------------------------------------------------------------
# STD and VAR

high_var_array = np.array([1, 100, 200, 300, 4000, 5000])
low_var_array = np.array([2, 4, 6, 8, 10])

print(np.var(high_var_array))
# 4296133.472222221
print(np.var(low_var_array))
# 8.0

print(np.std(high_var_array))
# 2072.711623024829
print(np.std(low_var_array))
# 2.8284271247461903

print(np.mean(high_var_array))
# 1600.1666666666667
print(np.mean(low_var_array))
# 6.0

import matplotlib.pyplot as plt 
# plt.figure(1)
# plt.hist(high_var_array)
# plt.plot(high_var_array)
# plt.figure(2)
# plt.hist(low_var_array)
# plt.plot(low_var_array)
# plt.show()

# -----------------------------------------------------------------------------
# Reshape and Transposing

print(a2)
# [[1.  2.  3.2]
#  [4.  5.  6.4]]

print(a3)
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]

#  [[10 11 12]
#   [13 14 15]
#   [16 17 18]]]

print(a2.shape, a3.shape)
# (2, 3) (2, 3, 3)

# można mnożyć tablice:
# - jak kształty dwóch tablic są takiesame
# - jeżeli nie są równe to jeden wymiar musi mieć 1


a2_reshape = a2.reshape(2, 3, 1)
print(a2)
# [[[1. ]
#   [2. ]
#   [3.2]]

#  [[4. ]
#   [5. ]
#   [6.4]]]
print(a3)
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]

#  [[10 11 12]
#   [13 14 15]
#   [16 17 18]]]

print(a2_reshape * a3)
# [[[  1.    2.    3. ]
#   [  8.   10.   12. ]
#   [ 22.4  25.6  28.8]]

#  [[ 40.   44.   48. ]
#   [ 65.   70.   75. ]
#   [102.4 108.8 115.2]]]

# -----------------------------------------------------------------------------

# Transpose (transpozycja) to operacja matematyczna polegająca na zamianie miejscami kolumn i wierszy w macierzy.
print(a3)
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]

#  [[10 11 12]
#   [13 14 15]
#   [16 17 18]]]

# print(a3.transpose())
print(a3.T) # to co wyżej
# [[[ 1 10]
#   [ 4 13]
#   [ 7 16]]

#  [[ 2 11]
#   [ 5 14]
#   [ 8 17]]

#  [[ 3 12]
#   [ 6 15]
#   [ 9 18]]]

# -----------------------------------------------------------------------------
# "Element-wise multiplications"

np.random.seed(0)

mat1 = np.random.randint(10, size=(5, 3))
mat2 = np.random.randint(10, size=(5, 3))
print(mat1)
# [[5 0 3]
#  [3 7 9]
#  [3 5 2]
#  [4 7 6]
#  [8 8 1]]

print(mat2)
# [[6 7 7]
#  [8 1 5]
#  [9 8 9]
#  [4 3 0]
#  [3 5 0]]

print(mat1.shape, mat2.shape)
# (5, 3) (5, 3)


# "Element-wise multiplications" oznacza, że mnożenie odbywa się na odpowiadających sobie elementach dwóch tensorów.
# Macierze muszą mieć tą samą liczbę elementów, jeżeli nie mają dopełnia się je przez reshaping jedynkami.
# Monoży się element przez element.

print(mat1 * mat2)
# [[30  0 21]
#  [24  7 45]
#  [27 40 18]
#  [16 21  0]
#  [24 40  0]]

# -----------------------------------------------------------------------------
# Dot product (iloczyn skalarny)

print(mat1)
# [[5 0 3]
#  [3 7 9]
#  [3 5 2]
#  [4 7 6]
#  [8 8 1]]

print(mat2)
# [[6 7 7]
#  [8 1 5]
#  [9 8 9]
#  [4 3 0]
#  [3 5 0]]

# Dot product (iloczyn skalarny) to operacja matematyczna, która ma zastosowanie w algebrze liniowej i analizie wektorowej.
# Żeby można było wykonać iloczyn skalarny, to macieże powinny być odpowiednio ułożone, i mieć odpowiedni shape,
# ilość kolumn w pierwszej musi się zgadzać z ilością wierszy w drugiej.

print(mat1)
# [[5 0 3]
#  [3 7 9]
#  [3 5 2]
#  [4 7 6]
#  [8 8 1]]

print(mat2.T)
# [[6 8 9 4 3]
#  [7 1 8 3 5]
#  [7 5 9 0 0]]

mat3 = np.dot(mat1, mat2.T)

print(mat3)
# [[ 51  55  72  20  15]
#  [130  76 164  33  44]
#  [ 67  39  85  27  34]
#  [115  69 146  37  47]
#  [111  77 145  56  64]]

print(mat1.shape, mat2.shape, mat3.shape)
# (5, 3) (5, 3) (5, 5)

# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------