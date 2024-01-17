import torch
from torch import nn # torch.nn zawiera wszystko do budowania sieci neuronowych
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# X = torch.arange(0, 10, 1).unsqueeze(dim = 1) 
# print(X[0])

#print('....................... wizualizacja danych')
# def plot_predictons(train_data = X_train, train_labels = y_train, test_data = X_test, test_label = y_test, predictions = None) :
#     plt.figure(figsize=(10, 7))
#     if train_labels is not None :
#         plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")
#     if test_label is not None :
#         plt.scatter(test_data, test_label, c="g", s=4, label="Testing data")
#     if predictions is not None :
#         plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")
#     plt.legend(prop={"size": 14})
    
#     plt.show()            

# print(X_train, y_train) # domyślne dane wejściowe do plot_predictons()
# print(X_test, y_test)
#plot_predictons()

#print(torch.__version__)
# 2.1.2+cu121

    # if epoch % 10 == 0:
    #     epoch_count.append(epoch)
    #     loss_values.append(loss)
    #     test_loss_values.append(test_loss)
    
lista = [[1,2,3], [4,5,6]]
print(lista)