import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('iris.csv')
print(df.head())
print(df.shape)

##  UNIVARIATE ANALYSIS

# df_setosa=(df.loc[df['species']=='setosa'])
# df_virginica=(df.loc[df['species']=='virginica'])
# df_versicolor=(df.loc[df['species']=='versicolor'])
# plt.plot(df_setosa['sepal_length'],np.zeros_like(df_setosa['sepal_length']),'o')#since it is univariate we only pass x and in place of y we pass something like constant
# plt.plot(df_virginica['sepal_length'],np.zeros_like(df_virginica['sepal_length']),'o')#since it is univariate we only pass x and in place of y we pass something like constant
# plt.plot(df_versicolor['sepal_length'],np.zeros_like(df_versicolor['sepal_length']),'o')#since it is univariate we only pass x and in place of y we pass something like constant
# # print(np.zeros_like(df_setosa['sepal_length']))
# plt.xlabel('Petal Length')
# plt.show()

##BIVARIATE ANALYSIS

# sns.FacetGrid(df,hue="species").map(plt.scatter,"petal_length","sepal_width").add_legend()
# plt.show()


##MULTIVARIATE ANALYSIS

sns.pairplot(df,hue="species",height=1,size=2)
plt.show()