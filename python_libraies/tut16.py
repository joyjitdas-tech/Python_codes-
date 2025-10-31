#pandas->pandas series->it like a col in a table , 1d data of any type
import numpy as np
import pandas as pd

#series using string
# country = ["India","nepal","aus","usa"]
# print(pd.Series(country))

#custom index
# marks = [40,50,77,91]
# subject = ["math","os","dsa","aiml"]

# print(pd.Series(marks,index = subject))

#setting a name
# marks = [40,50,77,91]
# subject = ["math","os","dsa","aiml"]

# print(pd.Series(marks,index = subject,name = "joyjit ki marks"))

#seres from dict
# marks = {
#     "math":68,
#     "dsa":99,
#     "os": 99,

# }
# print(pd.Series(marks,name="joyit ki marks"))
# mark_series = pd.Series(marks)
# #series attribute
# print(mark_series.size)
# print(mark_series.dtype)
# print(mark_series.name)

# #is_unique
# print(mark_series.is_unique)

# #index
# print(mark_series.index)
# print(mark_series.values)#its return numpy array


#series using resd csv(coma separated values)
#subs = pd.read_csv("tut16subs.csv",usecols=[0]).iloc[:,0]->if you dont know name of col
subs = pd.read_csv("tut16subs.csv",usecols=["Subscribers gained"])["Subscribers gained"]
# print(subs)

run = pd.read_csv("tut16kohli_ipl.csv",index_col="match_no",usecols=["match_no","runs"])["runs"]
# print(run)

movie = pd.read_csv("tut16bollywood.csv",index_col="movie",usecols=["movie","lead"])["lead"]
# print(movie)

#head & tail
# print(subs.tail(10))
# print(subs.head(10))

#sample->randomly generate
# print(movie.sample(5))

#value counts->to check frequence in values
# print(movie.value_counts())

#sort values
# print(run.sort_values(ascending=False).head(1).values[0])


#sorting in original but u have to copy it
# run.sort_values(inplace=True)

#sort by index
# print(movie.sort_index())


#math function in series

# #count->total num non missing values in sereis
# print(run.count())

# #sum
# print(subs.product())

# #mean->median->std->var

# print(subs.mean())
# print(subs.median())
# print(movie.mode())
# print(run.var())

# #min/max
 
# print(subs.min())
# print(subs.max())

# #describe
# print(run.describe())

#int indexing
# x = pd.Series([10,23,4,5,6,7,8,23,45,65,66])
# print(x[1])
# print(movie["Guddu Ki Gun"])#label indexin for this
# # print(movie[-1])

# #slicing
# print(run[5:16])
# print(movie[-5:])

# #fancy indexing
# print(run[[1,4,7]])


#editing item in series
marks = {
    "math":68,
    "dsa":99,
    "os": 67,
    "dbms":83,
    "oops":78,

}

marks1 = pd.Series(marks,name = "joyjit ki marks")
print(marks1)

#by indexing -> You use .loc when you want to select or edit data by the index label (name)
#You use .iloc when you want to select or edit data by integer position (like normal Python lists).
# marks1.loc["os"] = 30
# marks1.iloc[3] = 40
# marks1.loc["aoc"] = 90
# print(marks1)

# #by slicing
# x = pd.Series([10,23,4,5,6,7,8,23,45,65,66])
# x[2:4] = [100,200]
# print(x)

# #fancy indexing
# x[[0,5,6]] = [0,0,1]
# print(x)


#series with python function

# print(len(subs))
# print(dir(subs))
# print(sorted(subs))
# print("Alia Bhatt" in movie.values)

# # for i in movie:
# #     print(i)

# #broadcasting
# # s1 = 100 - marks1
# # print(s1)

# # #relation
# # print(run >= 50)

# #boolean indexing
# print(run[run == 0].size)

# print(subs[subs >= 200].size)

# num_movies = movie.value_counts()
# print(num_movies[num_movies> 20])

#graph plot
import matplotlib.pyplot as plt
# subs.plot()
# plt.show()

# run.plot()
# plt.show()

# movie.value_counts().head(20).plot(kind="pie")
# plt.show()

#special
import sys
print(sys.getsizeof(run))

print(sys.getsizeof(run.astype("int16")))

#betweeen
# print(run[run.between(51,99)])

# print(run.clip(100,150))

#drop duplicates[1,2,3,4,5,6,12,4,3]
temp = pd.Series([1,2,3,4,5,6,12,4,3])
temp = temp.drop_duplicates()
print(temp)