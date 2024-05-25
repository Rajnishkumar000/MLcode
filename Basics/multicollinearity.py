import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df=pd.read_csv('Advertising.csv',index_col=0)
x=df[['TV','Radio','Newspaper']]
y=df['Sales']
print(df.head())

x=sm.add_constant(x)
# print(x)
model=sm.OLS(y,x).fit()
print(model)
print(model.summary())

print(x.iloc[:,1:].corr())

df=pd.read_csv('Salary_Data.csv')
x=df[['YearsExperience','Age']]
y=df['Salary']
print(df.head())

x=sm.add_constant(x)
# print(x)
model=sm.OLS(y,x).fit()
print(model)
print(model.summary())

print(x.iloc[:,1:].corr())

