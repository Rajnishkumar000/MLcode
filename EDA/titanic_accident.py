import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import numpy as np

train=pd.read_csv('titanic_train.csv')
print(train.head())
print(train.info())
# FIRST CHECK HOW MANY MISSING DATA IS THERE
# print(train.isnull()) #This method is not considered in case of big data set.
                      # Here there is big data set so this method will not be used

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# sns.heatmap(train.isnull(),cbar=False,cmap='viridis')
# sns.heatmap(train.isnull(),cbar=False)
# sns.heatmap(train.isnull(),cmap='viridis')
# sns.heatmap(train.isnull())
# plt.show()

# sns.set_style('whitegrid')
# sns.set_style()
# sns.countplot(x='Survived',hue='Sex',data=train)
# plt.show()
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')
# plt.show()


# print("\n\n\n")

#This function gives count of the age that how many people of x age is present
# They are kind of normal distribution
# sns.distplot(train['Age'].dropna(),kde=False,color='darkred',bins=20)#distplt has been depreciated use "displot"
train['Age'].hist(bins=20,color='darkred',alpha=0.3)
# plt.show()

# sns.countplot(x='SibSp',data=train,palette='rainbow') #Assign hue to experience better colour while assigning palette
sns.countplot(x='SibSp',hue='SibSp',legend=False,data=train,palette='rainbow')#here legend is optional
# plt.show()










# DATA CLEANING

plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass',y='Age',hue='Pclass',legend=False,data=train,palette='winter')
# sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')
# plt.show()

def impute_age(cols):

    # age=cols[0]
    # Pclass=cols[1]
    age = cols.iloc[0]  # USE THIS iloc TO REMOVE WARNING
    Pclass=cols.iloc[1]

    if pd.isnull(age):
        if Pclass==1:
            return 37
        elif Pclass==2:
            return 29
        else:
            return 24
    else:
        return age

train['Age']=train[['Age','Pclass']].apply(impute_age,axis=1)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# plt.show()

# SINCE CABIN HAS SO MANY NULL VALUE SO WE HAVE TO APPLY FEATURE ENGINEERING BUT FOR NOW WE ARE DROPPING THIS COLOUMN
train.drop('Cabin',axis=1,inplace=True)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# plt.show()
print(train.head())

#REFER THIS BELOW LINK TO KNOW DROPNA.DROP DIRECTLY TAKES COLOUMN NAME WHILE DROP NA TAKES AXIS=0 OR 1 TO REMOVE NAN VALUE
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html

# dropna removes the entire row or coloumn if it found at least 1 nan value in the respective row or coloumn
print(train.info())
train.dropna(inplace=True)
print(train.info())

# now converting the columns with categoral features to so dummy variables

# pd.get_dummies(train['Embarked'],drop_first=True).head()
# print(pd.get_dummies(train['Embarked'],drop_first=True).head()) #THIS IS NOT APPLIED NOW I JUST HAVE USED GET FUNCTION TO PRINT TO SHOW MYSELF
#THAT HOW IT IS CHANGING

# Here am creating dummy variables for categorical features
sex=pd.get_dummies(train['Sex'],drop_first=True)
embark=pd.get_dummies(train['Embarked'],drop_first=True)
print(train['Embarked'].head())

#Now am droppiing the categorical and useless coloumn
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
print(train.head())

# NOW CONCATENATING DUMMY VARIABLES
train=pd.concat([train,sex,embark],axis=1)
print(train.head())
# NOW WE HAVE DONE WITH CLEANING DATA AND THIS IS OUR MAIN DATA WHICH WE HAVE TO CONSIDER









# APPLYING LOGISTIC REGRESSION MODEL TO TRAIN MODEL

# BEFORE APPLYING TRAIN TEST SPLIT WE FIRST DROP THE SURVIVED COLOUMN WHICH IS DEPENDENT FEATURES
print(train.drop('Survived',axis=1).head())
print(train['Survived'].head())


# NOW USING TRAIN TEST SPLIT
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html

# SPLITTING THE DATA AS X AND Y
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(train.drop('Survived',axis=1),train['Survived'],test_size=0.3,random_state=101)

# NOW USING LOGISTIC MODEL
from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression(max_iter=5000)
logmodel.fit(X_train,y_train)

predctions=logmodel.predict(X_test)


from sklearn.metrics import confusion_matrix
accuracy=confusion_matrix(y_test,predctions)
print(accuracy)

from sklearn.metrics import accuracy_score
percentage_accuracy=accuracy_score(y_test,predctions)
print(percentage_accuracy)
print(predctions)

print("------------------------------------------------------------------------------------END----------------------------------------------------------------------------------------------------------------")