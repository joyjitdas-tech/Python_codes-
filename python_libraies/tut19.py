import numpy as np
import pandas as pd

# can we have multiple index? Let's try
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a = pd.Series([1,2,3,4,5,6,7,8],index=index_val)
#print(a)
#problem is cse and year is together

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
multiindex.levels[1]
# 2. pd.MultiIndex.from_product()
multi = pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]])
#print(multi)

#creating series
s = pd.Series([1,2,3,4,5,6,7,8],index=multi)
# print(s)
# print(s['cse'])

#to convert multiindex series in a datafrma called unstack function->vice versa use stack
# print(s.unstack())

#multiindex datframe
branch_df1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index = multiindex,
    columns = ['avg_package','students']
)

# print(branch_df1)

# print(branch_df1['students'])

#multiindex datframe in colums
branch_df2 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
    ],
    index = [2019,2020,2021,2022],
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

# print(branch_df2)
# print(branch_df2['delhi'])
# print(branch_df2.loc[2020])

# Multiindex df in terms of both cols and index

branch_df3 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
        [9,10,0,0],
        [11,12,0,0],
        [13,14,0,0],
        [15,16,0,0],
    ],
    index = multiindex,
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

#print(branch_df3)

#stacking & unstacking
#print(branch_df3.stack().stack())

# print(branch_df3.shape)
# print(branch_df3.info())
# print(branch_df3.value_counts())
# print(branch_df3.isnull())

#extracting rows 
#print(branch_df3.loc[('cse',2019):('ece',2020):2])

#extrating by col
# print(branch_df3['delhi'])
# print(branch_df3.iloc[[0,4],[1,2]])

#soring the index
#print(branch_df3.sort_index(ascending=[False,True]))

#traspose
#print(branch_df3.transpose())

#swaplevel
#print(branch_df3.swaplevel())

#LONG VS WIDE DATA
long1 = pd.DataFrame(
    {
        'branch':['cse','ece','mech'],
        '2020':[100,150,60],
        '2021':[120,130,80],
        '2022':[150,140,70]
    }
).melt(id_vars=['branch'],var_name='year',value_name='students')
# print(long1)

confirmed = pd.read_csv('tut19time_series_covid19_confirmed_global.csv')
death = pd.read_csv('tut19time_series_covid19_deaths_global.csv')
#print(death)

death_melted = death.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='Date',value_name='num_cases')
confirmed_melted = confirmed.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='Date',value_name='num_deaths')
merged = confirmed_melted.merge(death_melted,on=['Province/State','Country/Region','Lat','Long','Date'])[['Country/Region','Date','num_cases','num_deaths']]
print(death_melted)
print(merged.head())