#functions

# def cal_sum(a,b):
#     return a+b
# sum=cal_sum(10,5)
# print(sum)
# def cal_avg(a,b):
#      sum=cal_sum(a,b)
#      return sum/2
# avg=cal_avg(20,90)
# print(avg)

#ques-1
# def length(list=[]):
#      count = 0
#      for el in list:
#           count+=1
#      return count

# num=[1,2,3,4,5,6,7,8,9]
# size=length(num)
# print(size)

#ques--2factorial
# def fact(n=0):
#     if(n>=1):
#         return n*fact(n-1)
#     else:
#         return 1
# factorial=fact(3)
# print(factorial)

#ques-3
# def converter(money):
#     return money*88.143
# money_us = converter(100)
# print(money_us)

#ques-3
# def ev_odd(n):
#     if(n%2==0):
#         return "even"
#     else:
#         return "odd"
# number = int(input("enter the number:"))
# check=ev_odd(number)
# print(check)

#ques-3
# def sum_of_n(n):
#     if(n==0):
#         return 0
#     else:
#         return n + sum_of_n(n-1)
# number = int(input("enter the number:"))
# check=sum_of_n(number)
# print(check)

#ques-4
def show(list,index=0):
        if(index==len(list)):
                return
        print(list[index])
        show(list,index+1)
        
list=[1,2,3,4,5,6,7,8,9]
show(list)
