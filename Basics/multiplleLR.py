import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('50_Startups.csv')

x=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

states=pd.get_dummies(x['State'],drop_first=True)
# print(states)
x=x.drop('State',axis=1)
x=pd.concat([x,states],axis=1)

# states = pd.get_dummies(dataset['State'], drop_first=True)
# x = pd.concat([states, dataset.drop('State', axis=1)], axis=1)
# print(x)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

print(y_test)
print("\n")


from sklearn.metrics import r2_score
score=r2_score(y_test,y_pred)
# r2 is used to know how good our model is if it is near to 1 then it is good
print(score)