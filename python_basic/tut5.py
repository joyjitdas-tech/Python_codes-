#loops
#while
# count = 1
# while count<=5:
#     print("hi")
#     count +=1
# i = 10
# while i>=1:
#     print(i)
#     i-=1

#ques-1
# number = int(input("enter the number: "))
# i = 1
# while i<=10:
#     print(number,"*",i,"=",number * i)
#     i+=1
#ques-2
# x=int(input("enter the you want to find: "))
# list1 = (1,5,6,7,4,6,78,8,656,4,776,7,8)
# n = len(list1)
# i = 1

# while i< n:
#     if(list1[i]==x):
#         print(list1[i],"founded")
#     i+=1

#break--break in a particular condition matched
#continue--terminated only this condition then go for next termination

#for loop
# list1 = (1,5,6,7,4,6,78,8,656,4,776,7,8)
# for el in list1:
#     print(el)

#ques-1
# list1 = (1,5,6,7,4,6,78,8,656,4,776,7,8)
# x = int(input("enter the number: "))
# for el in list1:
#     if(el == x):
#         print(x,"founded")
#     # else:
#     #     print("not found")
# else:
#     print("loop end")

#range function--range(start,stop,skip)--ending not include
for el in range(2,11,2):
    print(el)