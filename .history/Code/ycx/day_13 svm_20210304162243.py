import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('./datasets/Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values





