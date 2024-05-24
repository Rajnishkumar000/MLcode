import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
import scipy.stats as stats
from scipy.stats import chi2

df=sns.load_dataset('tips')

x=df[['total_bill','smoker','day','time']]
y=df['tip']
# print(x)
# print(y)
print(df.head())

df_table=pd.crosstab(df['sex'],df['smoker'])
print(df_table)

print("\n\nObserved values")
print(df_table.values)  #OBSERVED VALUES
ObservedValue=df_table.values

val=stats.chi2_contingency(df_table)
print("\nAll info")
print(val)

print("\n\nExpected value")
expected_values=val[3]
print(expected_values)

rows=len(df_table.iloc[0:2,0])
column=len(df_table.iloc[0,0:2])

dof=(rows-1)*(column-1)
print("Degree of freedom=",dof)

alpha=0.05

chi_square=sum([(o-e)**2/e for o,e in zip(ObservedValue,expected_values)]) #zipping because pf 2x2 matirx
chi_square_statistics=chi_square[0]+chi_square[1]

print("CHI square statistic ",chi_square_statistics)

critical_value=chi2.ppf(q=1-alpha,df=dof)

pvalue=1-chi2.cdf(x=chi_square_statistics,df=dof)
print("P value is ",pvalue)
print("significance lever is ",alpha)
print("Degre of freedom is ",dof)

if chi_square_statistics>=critical_value:
    print("Reject H0, There is a relationship between 2 categorical variable")
else:
    print("Retain H0, There is no relationship between 2 categorical variable")


if pvalue<=alpha:
    print("Reject H0, There is a relationship between 2 categorical variable")
else:
    print("Retain H0, There is no relationship between 2 categorical variable")