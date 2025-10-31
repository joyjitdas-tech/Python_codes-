#advance numpy->numpy is take less memory,time and more convenience then python list
import numpy as np

# a = np.random.randint(1,100,25).reshape(5,5)
# print(a)

# #fancy indexing
# print(a[:,[1,3]])
# print(a[[2,4]])

# #boolean indexing
# print(a[a>50])

# print(a[(a%2 == 0 )& (a>50)])
# print(a[a%7 != 0])


#broadcasting->describe how numpy traet different size of array at the time of arithmetic operation
#chota wala array repeat itself->only a matrix having one row or one col col it can boardcast
# a1 = np.arange(16).reshape(4,4)
# a2 = np.arange(4)

# print(a1)
# print(a2)

# print(a1+a2)

# a3 = np.arange(3).reshape(1,3)
# a4 = np.arange(4).reshape(4,1)

# print(a3)
# print(a4)

# print(a3+a4)

#sigmoid
# def sigmoid(array):
#     return 1/(1+np.exp(-(array)))
# a1 = np.arange(10)
# print(sigmoid(a1))

# #mean square error
# def mensqerror(actual,predicted):
#     return np.mean((actual - predicted)**2)
# actual = np.random.randint(1,50,25)
# predicted = np.random.randint(1,50,25)

# print(mensqerror(actual,predicted))

#categorical cross entropy
# def binaycrossError(act1,pred1):
#     pred1= np.clip(pred1, 1e-15, 1 - 1e-15)
#     return -np.mean((act1*np.log(pred1))+(1-pred1)*np.log(1-pred1))
# act1 = np.random.randint(1,50,25)
# pred = np.random.randint(1,50,25)
# print(binaycrossError(act1,pred))



#missing value
# a = np.array([1,2,3,4,np.nan,6])
# print(a)
# print(np.isnan(a))
# print(a[~np.isnan(a)])

#ploting graph

#x=y
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 50)
y = x

# plt.plot(x, y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Line Plot: y = x")
# plt.legend()
# plt.grid(True)
# plt.show()

# y = x**2

# plt.plot(x,y)
# plt.show()


# y = np.sin(x)
# plt.plot(x,y)
# plt.show()


# y = np.log(x)
# plt.plot(x,y)
# plt.show()

#sigmoid
y = 1/(1+np.exp(-x))
plt.plot(x,y)
plt.grid(True)
plt.show()