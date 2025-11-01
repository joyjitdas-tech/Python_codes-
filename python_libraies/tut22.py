import numpy as np
import pandas as pd
import seaborn as sns
titanic = pd.read_csv('tut22titanic.csv')
expense = pd.read_csv('tut22expense_data.csv')

# What are vectorized operations
a = np.array([1,2,3,4])
# print(a*5)

# problem in vectorized opertions in vanilla python
# s = ['cat','mat',None,'rat']
# [i.startswith('c') for i in s]

# How pandas solves this issue?

s = pd.Series(['cat','mat',None,'rat'])
# string accessor
# print(s.str.startswith('c'))

#common function in string
# print(titanic['Name'].str.upper())
# print(titanic['Name'].str.capitalize())
# print(titanic['Name'].str.title())

#len
# print(titanic['Name'][titanic['Name'].str.len() == 82].values[0])

#strip
# print(titanic['Name'].str.strip())

#split
titanic['surname'] = titanic['Name'].str.split(',').str.get(0)
titanic[['title','firstname']] = titanic['Name'].str.split(',').str.get(1).str.strip().str.split(' ',n=1,expand=True)
# print(titanic.sample())

# print(titanic['title'].value_counts())

#replace function
titanic['title'] = titanic['title'].str.replace('Ms.','Miss.')
titanic['title'] = titanic['title'].str.replace('Mlle.','Miss.')
# print(titanic['title'].value_counts())

#filtering
# print(titanic[titanic['firstname'].str.startswith('A')])
# print(titanic[titanic['firstname'].str.endswith('A')])

#regular ex
# print(titanic[titanic['firstname'].str.contains('john',case=False)])

#start and end with a
#print(titanic[titanic['surname'].str.contains('^[aeiouAEIOU].+[aeiouAEIOU]$')]['surname'])

#slicing
# print(titanic['Name'].str[:4])

#DATE AND TIME IN PANDAS
#timestamp in pandas
pd.Timestamp('2025/11/1')
#print(pd.Timestamp('2025/11/1 9:20AM'))
t = pd.Timestamp('2025/11/1 8:20AM')
# print(t)

#DATETIMEINDEX->a collection of pandas timestrap
dt_index = pd.DatetimeIndex(['2025/1/16','2025/8/20','2025/11/1'])

#print(pd.Series([1,2,3],index=dt_index))

#date range funtion
#print(pd.date_range(start='2025/11/1',end='2025/11/30',freq='2D'))

#business day
#print(pd.date_range(start='2025/11/1',end='2025/11/30',freq='B'))

#hourly
#print(pd.date_range(start='2025/11/1',end='2025/11/30',freq='H'))

#to_datetime->convert an exsisting object to timestarp/datetimeindex in pandas

s = pd.Series(['2025/1/16','2025/8/20','2025/11/1'])
# print(s)
# print(pd.to_datetime(s).dt.year)

#for error
s1 = pd.Series(['2025/1/16','2025/80/20','2025/11/1'])
# print(pd.to_datetime(s1,errors='coerce').dt.year)

expense['Date'] = pd.to_datetime(expense['Date'])
#print(expense.info())

# print(expense['Date'].dt.year)

#graph of expense
import matplotlib.pyplot as plt
# plt.plot(expense['Date'], expense['INR'], marker='o', color='teal')
# plt.title('Daily Expenses')
# plt.xlabel('Date')
# plt.ylabel('Amount (INR)')
# plt.grid(True)
# plt.show()

#day name wise bar chart
expense['day_name'] = expense['Date'].dt.day_name()
expense.groupby('day_name')['INR'].sum().plot(kind='bar')
# plt.show()

#month name wise bar chart
expense['month_name'] = expense['Date'].dt.month_name()
expense.groupby('month_name')['INR'].sum().plot(kind='bar')
plt.title('Monthly Expenses')
plt.xlabel('month')
plt.ylabel('Amount (INR)')
plt.show()