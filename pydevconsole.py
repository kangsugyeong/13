import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import S                       

header = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names = header)

array = data.values
X = array[:, 0:8]
Y = array[:, 8]
print(X.shape, Y.shape)

scaler = MinMaxScaler(feature_range=(0,1))


# plt.clf()
# pd.plotting.scatter_matrix(data)
# plt.savefig('./results/scatter.png')
# data.hist(figsize=(12,10), bins=5)
# plt.tight_layout()
# plt.savefig('./results/histogram.png')

# data.plot(kind="density", figsize=(12,10), subplots=True, layout=(3,3), sharex = False)
# plt.savefig('./results/boxplot.png')

