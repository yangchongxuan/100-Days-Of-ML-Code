import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('./datasets/Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# 特征量化
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# 创建混淆矩阵
from sklearn.metrics import  confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# 训练集合结果可视化
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train