#data frame in pandas
import numpy as np
import pandas as pd

#creating data frame using list
student_data = [
    [100,70,5],
    [120,90,20],
    [50,50,5]
]

studen1 = pd.DataFrame(student_data,columns=["iq","marks","lpa"])
# print(student)

#creating data frame using dict

student_dict = {
    "name":["soumya","joy","arpan"],
    "iq":[120,90,80],
    "marks":[100,60,80],
    "package":[10,20,8]
}

student = pd.DataFrame(student_dict)
# print(studen1)

#import csv file
movies = pd.read_csv("tut17movies.csv")
# print(movies)

ipl = pd.read_csv("tut17ipl-matches.csv")
# print(ipl)

#some attributes of dataframe
#shape
# print(movies.shape)

# #dtypes
# print(ipl.dtypes)

# #index
# print(movies.index)

# #colums
# print(movies.columns)

# #values
# print(studen1.values)

#some function
#head and tail
# print(ipl.head(5))
# print(ipl.tail(2))

# #sample
# print(ipl.sample())

# #info
# print(movies.info())

#describe
# print(movies.describe())

# #isnull
# print(ipl.isnull().sum())

# #duplicated
# print(movies.duplicated().sum())

# #rename->rename col
# #not change but if u want permanently then use inplace
# print(student.rename(columns = {"lpa":"package"},inplace=True))
# print(student)


#math function for row wise axis=1
# print(student.sum())
# print(student.mean())
# print(student.std())


#use any col
# print(movies.columns)
# print(movies[["title_x","imdb_rating"]].sort_values(by="imdb_rating",ascending=False))


#how to fatch row
#iloc->searching using index position
#loc->searching using index labels
# print(student)
# student.set_index("name",inplace=True)

# # print(movies.iloc[0:5])

# # print(movies.iloc[[0,4,7]])

# print(student.loc["joy"])

# #fetching col & row
# print(movies.iloc[0:3,0:2])


#filtering data ->vvi

#find all the winner in ipl match
# print(ipl.columns)
# # print(ipl.head(2))

# mask = ipl["MatchNumber"] == "Final"
# new_df = ipl[mask]
# print(new_df[["Season","WinningTeam"]])

#superover mathches
# print(ipl.columns)

# print(ipl[ipl["SuperOver"] == "Y"].shape)

#how many matches csk won in kolkata
# print(ipl[(ipl["City"] == "Kolkata") & (ipl["WinningTeam"] == "Chennai Super Kings")][["Date","Player_of_Match"]]) 

#toss vs match winner
# print(ipl[ipl["TossWinner"] == ipl["WinningTeam"]].shape[0]/ipl.shape[0]*100)
 

 #movies with rating >8 and 1000<votes
#print(movies.columns)

#print(movies[(movies["imdb_rating"] > 8) & (movies["imdb_votes"] > 10000)][["title_x","imdb_rating","imdb_votes"]])

#action movies with higher rating ->as there multiplr gener in single movie we make this col then solit it to easy acess
#print(movies[(movies["genres"].str.split("|").apply( lambda x:"Action" in x)) & (movies["imdb_rating"] > 7.5)][["title_x","imdb_rating"]])

#track back two teams


#Adding new col
#new
# movies["country"] = "india"
# print(movies.columns)

#existing one
# movies["lead_actor"] = movies["actors"].str.split("|").apply(lambda x:x[0])
# print(movies)

#astype->to change data type
print(ipl.info())
ipl["ID"] = ipl["ID"].astype("int32")
ipl["Season"] = ipl["Season"].astype("category")
ipl["Team1"] = ipl["Team1"].astype("category")
ipl["Team2"] = ipl["Team2"].astype("category")
print(ipl.info())
