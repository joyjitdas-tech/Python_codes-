#numpy array
import numpy as np
# a = np.array([1,2,3])

# #2d
# # b = np.array([[1,2,4],[4,5,6]])
# # print(b)

# #dtype
# c = np.array([1,2,3],dtype=float)
# print(c)
# #arange
# d = np.arange(1,11)
# print(d)
# #reshape
# e = np.arange(1,11).reshape(5,2)
# print(e)
# #np.one
# f = np.ones((4,3))
# print(f)
# #randomply
r = np.random.random((3,2))
print(r)
# #linspace->(lowe,upper,number)->generate numbers in equal distances
# l = np.linspace(-10,10,10)
# print(l)
# #identity
# i = np.identity(3)
# print(i)


#ndim
# a1 = np.arange(9)
# print(a1.ndim)
# a2 = np.arange(12).reshape(3,4)
# print(a2.ndim)
# a3 = np.arange(8).reshape(2,2,2)
# print(a2.ndim)

# #shape
# print(a3.shape)
# print(a3)

# #itemsize->give total size
# print(a3.itemsize)

#astype->to change data type
# a3 = a3.astype(np.int32) # convert to float32
# print(a3.dtype)  

#operation  in array
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(12,24).reshape(3,4)
# print(a2*2)

# #relation

# print(a2<5)

# #dynamic
# print(a2+a3)
# print(a2*a3)

#function
# a1 = np.random.random((3,3))
# a1 = np.round(a1*100)
# print(a1)
# print(np.max(a1))
# print(np.sum(a1))
#max/min
#row->1col->0
# print(np.max(a1,axis=0))

#mean/median.std/var
# print(np.mean(a1,axis= 1))
# print(np.median(a1,axis= 1))
# print(np.std(a1,axis= 1))
# print(np.var(a1,axis= 1))

#trignometric
# print(np.sin(a1))

#dot product
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(12,24).reshape(4,3)
# print(np.dot(a2,a3))

# print(np.log(a1))

# #round,floar,cill
# print(np.round(np.random.random((3,3))*100))

#indexing & slicing

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# print(a1[-1])

# #2d array
# print(a2)
# print(a2[1,2])

# #3d array
# print(a3)
# print(a3[0,0,0])

#slicing
# print(a1[2:5])
#2d
# print(a2)
# print(a2[0,:])
# print(a2[:,3])
# print(a2[1:2,0:4:3])
# print(a2[:2,1::])
#3d
a3 = np.arange(27).reshape(3,3,3)
# print(a3)
# print(a3[0:3,1:2,0::])
# print(a3[::2,::3,::2])

#loop
# for i in a1:
#     print(i)
# for i in a2:
#     print(i)
#for loop in every single eliment
# for i in np.nditer(a3):
#     print(i)

#reshaping
#traspose
print(a2.T)
#ravel->to convert any array in 1d
print(a3.ravel())

#stacking array->two types_>horizontal & vertical
a4 = np.arange(9).reshape(3,3)
a5 = a4.T
a6 = np.hstack((a4,a5))
#print(a6)
a7 = np.vstack((a5,a4))
print(a7)

#spiting->
a8 = np.hsplit(a6,2)
print(a8)
a9 = np.vsplit(a7,3)
print(a9)