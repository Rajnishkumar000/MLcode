# Numpy is used because it has bindings of c++ library
# C++ library is efficient and faster
# Operation within it takes Quickly

import numpy as np
lst=[1,2,3,"Raj"]
arr=np.array(lst)
print(arr)
arr[1]=5
print(arr)
print(type(arr))
print(arr.shape)

# SHAPE-RESHAPE
lst1=[4,3,2,11]
lst2=[9,8,7,0]
lst3=[6,5,1,14]
arr1=np.array([lst2,lst1,lst3])
print(arr1)
arr1=arr1.reshape(4,3)
print(arr1)
print()

# 2-D ARRAY
arr=np.array([[1,2,3,4,5],[2,3,4,5,6],[9,7,6,8,9]])
print(arr[0:2,0:2])
print(arr)
print(arr[1:2,1:4])
print()

# ARANGE
# it will pick up element between the given range
arr=np.arange(0,10,step=2)# it takes one more parameter step to jump
print(arr)
print()

#linspace
# between start and end how many equal divided points you want
arr=np.linspace(0,100,5)
print(arr)

# Copy
print()
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
arr[4:]=100
print(arr)
arr1=arr
arr1[4:]=500
print(arr1)
print(arr)
# To Prevent the change and successful copy we use copy function
arr2=arr.copy()
print("After changin to 1000")
arr2[7:]=1000
print(arr)
print(arr2)
print(arr1)

# SOME IMPORTANT USES
print()

arr=np.array([1,2,3,4,5,6])
print(arr>3)
print(arr[arr>3])
print(arr*2)

print(np.ones(4))
print(np.ones(4,dtype=int))
print(np.ones((2,4),dtype=int))

print()
# select random value of given shape bw 0 and 1
print(np.random.rand(3,4))
print(np.random.randn(3,4))#standard normal
print(np.random.randint(0,100,8))#s8 nos bw 0 to 100
print(np.random.randint(0,100,8).reshape(2,4))
print(np.random.random_sample(0,5))#Return random floats in half open interval
