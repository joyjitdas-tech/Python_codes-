#STRING
# str1 = "hi i'm joyit\nfrom howrah."
# print(str1)
# str2 = "study in makaut"
# print(str1+str2)
# print(len(str2))

#indexing
# str3="joyjit-das"
# print(str1[3])

#slicing--accesing parts of string--include staring index
# print(str1[3:5])

# #negatie index
# print(str3[-7:-1])

#string function
# print(str3.capitalize())
# print(str3.replace("j",'d'))
# print(str3.count("j"))

#condition statement
#ques-1
name = input("enter your name : ")
marks = int(input("enter your obtain marks: "))
if(marks>=90):
    print("congrats ",name,"you got grade A")
elif(marks<90 and marks>= 80):
    print("congrats ",name,"you got grade B")
elif(marks<80 and marks>= 70):
    print("well ",name,"you got grade C")
else:
    print("you failed")