# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

from sklearn.metrics import accuracy_score


warnings.filterwarnings('ignore')
plt.style.use('ggplot')

# Loading Data
data = pd.read_csv('data.csv')

plt.figure(figsize=(10,5))
plt.title('HEIGHT vs WEIGHT')
plt.xlabel('Height', fontsize=15)
plt.ylabel('Weight', fontsize=15)
plt.scatter(data.Height, data.Weight, color='blue')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
print(f'X_train: {X_train.shape}\nX_test: {X_test.shape}\ny_train: {y_train.shape}\ny_test: {y_test.shape}')


regr = LinearRegression()
regr.fit(X_train, y_train)

print(f'Coefficient: {regr.coef_}')
print(f'Intercept: {regr.intercept_}')


plt.figure(figsize=(10,5))
plt.title('Regression Line on Training set')
plt.xlabel('Height', fontsize=15)
plt.ylabel('Weight', fontsize=15)
plt.scatter(X_train, y_train,s=75, color='blue')
plt.plot(X_train, regr.predict(X_train), color='red')
plt.show()

y_pred = np.round(regr.predict(X_test), decimals=2)
print(pd.DataFrame({'Height': X_test[:,0], 'Actual Weight': y_test, 'Predicted Weight': y_pred}))

plt.figure(figsize=(10,5))
plt.title('Regression Line on Testing set')
plt.xlabel('Height', fontsize=15)
plt.ylabel('Weight', fontsize=15)
plt.scatter(X_test, y_test,s=75, color='red')
plt.plot(X_test, y_pred, color='blue')
plt.show()



print(f'Mean Absolute Error(MAE): {metrics.mean_absolute_error(y_test, y_pred)}')
print(f'Residual Sum of Squares(MSE): {metrics.mean_squared_error(y_test, y_pred)}')
print(f'R2-Score: {metrics.r2_score(y_test, y_pred)}')



height_to_predict = np.array([[56]])
predicted_weight = regr.predict(height_to_predict)
print(f'Predicted weight for height 56: {predicted_weight}')