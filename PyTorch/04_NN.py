import torch
from torch import nn 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# Ustawienie urządzenia którego będzie używał PyTorch ('cpu', 'cuda')
device = "cuda" if torch.cuda.is_available() else "cpu"
#device = "cpu" # wymuszenie działania na procesorze
print('Urządzenie którego będę używał:', device)

torch.manual_seed(42)  