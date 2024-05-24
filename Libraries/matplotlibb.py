import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10)
y=np.arange(11,21)

# plt.scatter(x,y,c='r')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph in 2-D")

# plt.plot(x,x*x,c='g')
# plt.show()

# plt.subplot(2,2,1)
# plt.plot(x,y,'r')
# plt.subplot(2,2,2)
# plt.plot(x,y,'b')
# plt.subplot(2,2,3)
# plt.plot(x,y,'g')
# plt.subplot(2,2,4)
# plt.plot(x,y,'y')
# plt.show()

x=np.arange(1,10)
y=np.sin(x)
# plt.plot(x,y)
# plt.bar(x,y)
# plt.show()

a=np.array([1,1,2,2,2,3,4,5,6,6,6,7,8,9,10]) #y-axis show density that is count(how many times 1 is present)
plt.hist(a)
plt.show()