import numpy as np
import pandas as pd

#data frame sof pandas

marks = pd.DataFrame([
     [100,30,50],
     [100,30,40],
     [100,30,50]
],columns=['iq','marks','package'])

# print(marks)

# print(marks.value_counts())

ipl = pd.read_csv("tut17ipl-matches.csv")

# print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

import matplotlib.pyplot as plt

# ipl['TossDecision'].value_counts().plot(
#     kind='pie',
#     autopct='%1.1f%%',     # show percentages
#     startangle=90,          # start pie from top
#     shadow=True,            # add shadow effect
#     figsize=(5, 5),         # make chart a bit larger
#     ylabel=''               # remove automatic y-label
# )

# plt.title("Toss Decision Distribution")
# plt.show()
#matched [played by a team]
# print((ipl['Team1'].value_counts() + ipl['Team2'].value_counts()).sort_values(ascending = False))

movies = pd.read_csv("tut17movies.csv")
# print(movies.sort_values('title_x'))

# print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))

mark = {
    'math':39,
    'eng':49,
    'science':99
}
mark_series = pd.Series(mark)
# print(mark_series.sort_index())

#set & reset index ,reset turn a series into dataframe
# print(mark_series.reset_index())
movies.set_index('title_x',inplace=True)

movies.rename(columns={'imdb_id':'imdb'},inplace=True)
# print(movies)

#isnull->gives true where value not present

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

# print(students)

# print(students['name'].isnull())

#dropna
# print(students['name'].dropna())


# print(students.dropna(how="all"))

# print(students.dropna(subset=['name','college']))

#fillna

# print(students.fillna('unknown'))


#drop duplicated->
#print(marks.drop_duplicates(keep='last'))

#last match played against dd by king
# Combine players from both teams into one list per match
ipl['all_players'] = ipl['Team1Players'] + ipl['Team2Players']

# Function to check if Virat Kohli played in that match
def did_kohli_play(players_list):
    return 'V Kohli' in players_list

# Apply the function to each row
ipl['did_kohli_play'] = ipl['all_players'].apply(did_kohli_play)


#print(ipl[(ipl['City'] == 'Delhi') & (ipl['did_kohli_play'] == True)].drop_duplicates(subset=['City','did_kohli_play'],keep='first'))

#drop by index
# print(students.drop(columns=['branch','cgpa']))
# print(students.drop(index=[0,8]))


#apply function
points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)

print(points_df)

def euclidian(row):
    pt_a = row['1st point']
    pt_b = row['2nd point']

    return ((pt_a[0]-pt_b[0])**2 + (pt_a[1]-pt_b[1])**2)**0.5

points_df['Euclidian distance'] = points_df.apply(euclidian,axis=1)

print(points_df)