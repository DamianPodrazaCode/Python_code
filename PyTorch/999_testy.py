import torch
from torch import nn # torch.nn zawiera wszystko do budowania sieci neuronowych
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

X = torch.arange(0, 10, 1).unsqueeze(dim = 1) 
print(X[0])