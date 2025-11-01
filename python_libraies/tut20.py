import numpy as np
import pandas as pd

course = pd.read_csv('tut20courses.csv')
nov = pd.read_csv('tut20reg-month1.csv')
dec = pd.read_csv('tut20reg-month2.csv')
student = pd.read_csv('tut20students.csv')

temp_df = pd.DataFrame({
    'student_id':[26,27,28],
    'name':['Nitish','Ankit','Rahul'],
    'partner':[28,26,17]
})

student = pd.concat([student,temp_df],ignore_index=True)
#print(student)
#concact->for vartical ->pd.concat
regs = pd.concat([nov,dec],ignore_index=True)
#print(regs.shape)
concat2 = pd.concat([nov,dec],keys=['nov','dec'])
#print(concat2.loc[('nov',6)])
#concact->horizontaly->
concat3 = pd.concat([nov,dec],axis=1)
#print(concat3)


#inner join_>merge
inner1 = student.merge(regs,how='inner',on='student_id')
#print(inner1)

#left join
left1 = course.merge(regs,how='left',on='course_id')  
#print(left1)

#right join
right1 = student.merge(regs,how='right',on='student_id')
#print(right1)

#outer join
outer1 = student.merge(regs,how='outer',on = 'student_id')
#print(outer1.tail(10))

# 1 find total revenue
total = regs.merge(course,on='course_id')['price'].sum()
#print(total)

#find month by month revenue
concat2 = pd.concat([nov,dec],keys=['nov','dec']).reset_index()
#print(concat2.merge(course,how='inner',on='course_id').groupby('level_0')['price'].sum())

# 3 print student with name course price
#print(regs.merge(student,how='inner',on='student_id').merge(course,how='inner',on='course_id')[['name','course_name','price']])

# 4 enroll at both month
comn_id = np.intersect1d(dec['student_id'],nov['student_id'])

#print(student[student['student_id'].isin(comn_id)])

# 5 no enrollment
course2 = np.setdiff1d(course['course_id'], regs['course_id'])
#print(course[course['course_id'].isin(course2)])

# 6 student no enrollment
student2 = np.setdiff1d(student['student_id'],regs['student_id'])
#print(student[student['student_id'].isin(student2)])

#self join->table join with itself

# 7 student name with partner
# print(student.merge(student,left_on='partner',right_on='student_id')[['name_x','partner_x','name_y']])

# 8 top 3 student for enrollment
#print(regs.merge(student,on='student_id').groupby(['student_id','name'])['name'].count().sort_values(ascending=False).head(3))

# 9 find the student who spend most money
#print(regs.merge(student,on='student_id').merge(course,on='course_id').groupby(['student_id','name'])['price'].sum().sort_values(ascending=False).head(3))

# 10 IPL PROBLEM
ipl_delivary = pd.read_csv('tut19deliveries.csv')
ipl_matches = pd.read_csv('tut20matches.csv')
#Top 3 stadim highest six match ratio
temp_df = ipl_delivary.merge(ipl_matches,how='inner',left_on='match_id',right_on='id')
six_df=temp_df[temp_df['batsman_runs'] ==6]
six_no = six_df.groupby('venue')['venue'].count()

num_matches = ipl_matches['venue'].value_counts()

#print((six_no/num_matches).sort_values(ascending=False).head(3))


#find orange cap holder all season
print(temp_df.groupby(['season','batsman'])['batsman_runs'].sum().reset_index().sort_values('batsman_runs',ascending=False).drop_duplicates('season',keep='first').sort_values('season',ascending=False))