#Groupby in pandas
import numpy as np
import pandas as pd

movies = pd.read_csv('tut19imdb-top-1000.csv')

geners = movies.groupby('Genre')
#print(geners.sum())

#find top 3 genre by total earning
#print(geners.sum()['Gross'].sort_values(ascending=False).head(3))

#find the genre with height avg IMDB rating
#print(geners['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

#find director with most popularity
#print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))

#find the highst rating movies sin each genre
#print(geners['IMDB_Rating'].max())

#find top 10 animation


#find no movies done by each actor
#print(movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False))

#groupby attributes
# print(len(geners))
# print(geners.size())
# print(geners.first())
# print(geners.nth(3))


# print(geners.get_group('Fantasy'))

# print(geners.groups)

#describe->all math operation in numarical col
# print(geners.describe())

# print(geners.nunique())

# print(geners.agg({
#     'Runtime':['mean','max'],
#     'IMDB_Rating':'mean',
#     'No_of_Votes':'sum',
#     'Gross':'sum'}))

#looping on groups
# for group,data in geners:
#     print(data)

#find the highst rating movies sin each genre
# df = pd.DataFrame(columns=movies.columns)
# for group,data in geners:
#     df = df._append(data[data['IMDB_Rating'] == data['IMDB_Rating'].max()])
# print(df)

#split apply combine

#find no of moives in every genre started with A

# def func(group):
#     print( group['Series_Title'].str.startswith('A').sum())

# geners.apply(func)

#rank in every genre
# def rank_movies(group):
#     group['IMDB_rank'] = group['IMDB_Rating'].rank(ascending = False)
#     return group

# df1 = geners.apply(rank_movies)
# print(df1)

#normalized rating
# def normal(group):
#     group['Norm_rank'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
#     return group

# df2 = geners.apply(normal)
# print(df2)

#group by in multiple cols
duo = movies.groupby(['Director','Star1'])
# print(duo.size())
# print(duo.get_group(('Zoya Akhtar','Hrithik Roshan')))

#best director & actor duo
# print(duo['Gross'].sum().sort_values(ascending=False).head(1))

# #actor & genre combination
# print(movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head())

# #agg on multiple group
# print(duo.agg(['min','max']))

#ipl datas set
ipl = pd.read_csv('tut19deliveries.csv')
# print(ipl.shape)

#find the top batsman interms of run
batsman = ipl.groupby('batsman')
#print(batsman['batsman_runs'].sum().sort_values(ascending=False).head(10))

#find the batsman with man six
six = ipl[ipl['batsman_runs'] == 6]

# print(six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(10))

#find the batsman who hit 4 & 6 in last 5 over
over = ipl[ipl['over']>15 ]
temp_run = over[over['batsman_runs'] ==4 | (over['batsman_runs'] == 6)]

#print(temp_run.groupby('batsman')['batsman'].count().sort_values(ascending=False))

#find king record against kohli

temp_df = ipl[ipl['batsman'] == 'V Kohli']

#print(temp_df.groupby('bowling_team')['batsman_runs'].sum())


#highst score of any batsman
# def highest(batsman):
#     temp_df = ipl[ipl['batsman'] == batsman]
#     return temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending = False).head(1).values[0]

def highest(batsman):
    # Filter data for that batsman
    temp_df = ipl[ipl['batsman'] == batsman]

    # Calculate total runs per match
    runs_per_match = temp_df.groupby('match_id')['batsman_runs'].sum()

    # Find match where he scored the most runs
    top_match_id = runs_per_match.idxmax()
    top_runs = runs_per_match.max()

    # Find the bowling team in that match
    bowling_team = temp_df[temp_df['match_id'] == top_match_id]['bowling_team'].iloc[0]

    # Return both
    return top_runs, bowling_team

print(highest('V Kohli'))