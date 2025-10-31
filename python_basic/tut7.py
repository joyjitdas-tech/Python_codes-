#i/o file
# import os
# with open("tut7a.txt", "r") as f:
#     data = f.read()
#     print(data)
# with open("tut7a.txt","a+") as file:
#     file.write("I AM FROM HOWRAH")
#     print(file.read())
# os.remove("tut7a.txt")

# with open("tut7a.txt","w") as f:
#     f.write("hi i am joyjit das\n")
#     f.write("i am from howrah")
# word = input("enter what you want to find:")
# with open("tut7a.txt","r") as f:
#     data = f.read()
#     new_data=data.replace("joyjit","debi")
#     print(new_data)
#     if(data.find(word)!= -1):
#         print("found")
# with open("tut7a.txt","w") as f:#over write in txt file
#     f.write(new_data)


#seek and tell
with open("tut7a.txt","r") as f:
    print(f.read(10))
    print(f.tell())
    f.seek(5)
    print(f.tell())
#ques-1
# def check_for_line(word):
#     data = True
#     line_no=1
#     with open("tut7a.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#             line_no+=1
       


# word = input("enter the word:")
# check_for_line(word)

#ques-2
# def check_ev_odd():
#     count = 0
#     with open("tut7b.txt","r") as f:
#         num=f.read()
        
#         num1=num.replace("\n",",").split(",")
#         for val in num1:
#             if(int(val)%2 == 0):
#                 count+=1
#     return count

# with open("tut7b.txt","w+") as f:
#     f.write("1,2,3,4,5,6,7,8,9\n")
#     f.write("9,8,7,6,5,4,3,2,1")
# print(check_ev_odd())


    

