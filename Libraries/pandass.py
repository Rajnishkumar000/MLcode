import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"],columns=["Column1","Column2","Column3","Column4"])
print(df)
print(df.head())
print()
df.to_csv("Test.csv")

print(df.loc["Row1"])
print(type(df.loc["Row1"]))
print(df.iloc[:,:])

print(type(df.iloc[:,:]))

print(df.iloc[0:2,0:1])
print(df.iloc[0:2,0])


# data = [[50, True], [40, False], [30, False]]
# label_rows = ["Sally", "Mary", "John"]
# label_cols = ["age", "qualified"]
#
# df = pd.DataFrame(data, label_rows, label_cols)
#
# print(df.loc["Mary", "age"])
# print(df)

#CONVERT DATAFRAME INTO ARRAYS
print("Convert Dataframe to arrayss\n")#   ".value" is basically converting
ak=df.iloc[:,:].values
print(ak)
print(ak.shape)


# CHECKING NULL
print(df.isnull().sum())


# To find Unique categories when we have categorical features
print(df['Column1'].value_counts())
print(df['Column1'].unique())#just capture unique value . Does not count how many of them is of one type
print(df['Column2'])
print(df[['Column2','Column4']])
print(df.loc["Row1","Column2"])