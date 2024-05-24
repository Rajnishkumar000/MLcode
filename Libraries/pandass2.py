import pandas as pd
import numpy as np
df=pd.read_csv('mercedesbenz.csv') #takes a separator also by default it is comma
print(df.head(),"\n")
print(df.info(),"\n")
print(df.describe(),"\n\n\n") # only interger and floating column is taken into consideration , object(categorical) column is omited

from io import StringIO,BytesIO
data=('c1,c2,c3\n'
      'x,y,1\n'
      'a,b,2\n'
      'c,d')
print(data)
print("Type of data",type(data))
df=pd.read_csv(StringIO(data),dtype=object)
print("After converting to dataframe")
print(df)
df=pd.read_csv(StringIO(data),usecols=['c1','c2'])
print("Selecting only c1 and c2")
print(df)


print("\n\nConverting DataFrame to CSV file\n")
df.to_csv('pandasss2.csv')
print(df.dtypes)
print("\n\n\n")
data=('index,a,b,x\n'
      '4,apple,bat,5.7\n'
      '8,orange,cow,10')
print(data)
#1
print(1)
df=pd.read_csv(StringIO(data))
print(df)
print("\n\n\n")
# data=pd.read_csv(StringIO(data))
# print(data) #by default first coloumn is added 0 1 to omit default we use

#2
print(2)
df=pd.read_csv(StringIO(data),index_col=0)
print(df)
print("\n")

#3
print(3)
data=('a,b,c\n'
      '4,apple,bat,\n' #LAST comma is important 
      '8,orange,cow,')
df=pd.read_csv(StringIO(data)) #use index_col=False to remove Nan
print(df)
print("\n\n")


#4
print(4)
data=('a,b,c\n'
      '4,apple,bat\n' #LAST comma is important Removing comma
      '8,orange,cow')
df=pd.read_csv(StringIO(data)) #use index_col=False to remove Nan
print(df)
print("\n\n")

#5
print(5)
data=('a,b,c\n'
      '4,apple,bat\n' #LAST comma is important Removing comma
      '8,orange,cow')
df=pd.read_csv(StringIO(data),index_col=False) #use index_col=False to remove Nan
print(df)


# pd.read_json
# pd.read_excel
# pd.read_html
#also reads table from webpages as df[0] and match parameter orient and record parameter
