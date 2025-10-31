#sorting
import numpy as np

a = np.random.randint(1,100,20)
# a = np.sort(a)
# print(a)
# print(np.ones((2,3)))
# b = np.random.randint(1,100,20).reshape(4,5)
# print(b)
# # print(np.sort(b))
# # print(np.sort(b,axis=0))#col
# print((b.shape[0]))
# b = np.append(b,np.ones((1,b.shape[1])),axis = 0)
# # print((b.shape[1]))
# print(b)

# c = np.append(b,np.ones((b.shape[0],1)),axis=1)
# print(c) 

#concatenation
# a1 = np.arange(1,10).reshape(3,3)
# a2 = np.arange(10,19).reshape(3,3)

# print(np.concatenate((a1,a2),axis=1))

#unique

e = np.random.randint(1,50,20)
f = np.random.randint(1,50,20).reshape(4,5)
# print(e)
# print(np.unique(e))

#expand dimension->add dimension
# e = np.expand_dims(e,axis=0)
# print(e)
# print(e.shape)

#np.where->given index
# print(np.where(e%2 == 0))
# print(np.where(e%2==0,0,e))

# #argmax->find max num
# print(np.argmax(e))
# print(np.argmin(e))

#np.cumsum
# print(np.cumsum(e))
# print(f)
# print(np.cumsum(f,axis=1))
# print(np.cumprod(f,axis=1))

#np.percentile
# print(np.percentile(e,0))

# #histogram->to find num present in giver data range
# print(np.histogram(e,bins=[0,10,20,30,50]))


#np.corrcoef->pearson formula _1<->1
# salary = np.array([20000,30040,10000,5000,70000])
# experience = np.array([1,5,3,2,6])
# print(np.corrcoef(salary,experience))

#isin->to check multiple item have or not
item =[30,27,19,40,27,25,46]


# a = a[np.isin(a,item)]
# print(a)

#flip
print(a)
# a = np.flip(a)
# print(f)
# print(np.flip(f,axis=0))

#to change item
# np.put(a,[0,1],[101,201])
# print(a)

#delete
print(np.delete(a,5))


#set-theory
m = np.array([1,2,3,4,5,6])
n = np.array([3,4,5,6,7,8,])

# print(np.union1d(m,n))
# print(np.intersect1d(m,n))
# print(np.setdiff1d(m,n))
# print(np.setxor1d(m,n))

#clip->giving a range
print(np.clip(a,a_min=20,a_max=75))