# cost funtions=1/2m(summation of i=1 to i=n (y hat -y2)^2)

# graph of slope is called gradient descent
#  choose global minimum in gradient descent  curve

# OVERFITTING->with the help of training dataset you are getting low error but when using test dataset you are getting high error


# UNDERFITTING->with the help of training dataset you are getting HIGH error AND ALSO when using test dataset you are getting high error

# WITH THE HELP OF RIDGE AND LASSO REGRESSION WE ARE CONVERTING HIGH VARIANCE TO LOW VARIANCE SINCE WE KNOW THAT HERE IS OVERFITTING

# In linear regression const function is =summaation from 1 to m (y hat -y)^2

# y =original points
# y hat is point we get in line


###RIDGE REGRESSION

# in ridge regression we add 2 more parameter to cost fuction which is lambda*(slope)^2

# mostly in steep slope lead to overfitting

# we are penalising higher slopes

# LAMBDA VALUE IS CHOOSED USING CROSS VALIDATION

##LASSO REGRESSION

# WE ADD lambda * |slope|

# It also helps to do feature selection
# wherever slope is 0 it will eliminate that feature because that feature is not important for predicting best fit line

# https://www.geeksforgeeks.org/lasso-vs-ridge-vs-elastic-net-ml/