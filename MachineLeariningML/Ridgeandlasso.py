import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#
# column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
# data = pd.read_csv('housing.csv', header=None, delimiter=r"\s+", names=column_names)
# print(data.head())
#
# df=data.to_csv("housing1.csv")
# print(df)
#
# dataset=pd.DataFrame(df.data)
# print("\n")
# print(data.shape)
# print("\n")
# print(df.target.shape)
df=pd.read_csv('housing1.csv')
# df=pd.DataFrame('housing1.csv')
print(df)

