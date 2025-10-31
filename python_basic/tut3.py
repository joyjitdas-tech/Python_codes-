# TUPLE, LIST
# LIST -- mutable in python
# marks = [10, 45, 89, 99]
# # marks = [int(x) for x in marks]  

# print(type(marks), "length is", len(marks))

# marks[0] = 69
# print(marks[0])

# student = ["joyjit", 91, 18]
# print(student)

# # slicing
# print(marks[1:])

# # append -- add one element at the end
# marks.append(82)
# marks.insert(2,78)
# print(marks)
# marks.sort()
# marks.reverse()
# #remove del only first occurence,pop del particular index
# print(marks)

# tupple--immutable
# tupp = (1,2,3,7,5,4,)
# print(type(tupp))
# print(tupp[1:3])

#ques-1
# fav =[]
# fav.append(input("enter your fav movies: "))
# fav.append(input("enter your fav movies: "))
# fav.append(input("enter your fav movies: "))
# fav.sort()
# print(fav)

#ques-2
list = [1,2,3,2,1]
reversed_list=list[::-1]
print(reversed_list)
if(list == reversed_list):
    print("it is palindrome")
else:
    print("not palindrome")
