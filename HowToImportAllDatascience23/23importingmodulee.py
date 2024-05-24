from pyforest import active_imports
import pandas as  pd
import matplotlib.pyplot as plt
df=pd.read_csv('Test.csv')
print(df.head())

lst1=[1,2,3,4]
lst2=[1,2,3,4]
plt.plot(lst1,lst2)
plt.show()

print(active_imports())
