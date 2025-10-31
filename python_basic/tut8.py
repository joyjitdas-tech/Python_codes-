#class is a blueprint for creating a oject
""" attributes are two types class & instance attributes"""
# class student:
#     college_name = "MAKAUT"  #class attributes
#         #constructor
#     def __init__(self,fullname,age,sgpa):
#         self.name = fullname    #object attributes
#         self.age=age
#         self.sgpa=sgpa
#     def welcome(self):
#         print("welcome coder")

# s1 = student("joyjit",18,9)
# print(s1.name,s1.age)
# s2 = student("soumya",21,9.5)
# print(s2.name,s2.age)
# s1.welcome()


#ques-1
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your score is ",sum/3)
# s1 = student("joyjit das",[98,79,67])
# s1.get_avg()

#static method--don't use self parameter
# just use @staticmethod before declair a fun in class



#abstruction--hiding the unnessary process from user
#encapsulation--wrapping data anf func in a sigle unit(object)

#ques-2
# class account:

#     def __init__(self,balence,acc_no):
#         self.balence = balence
#         self.acc_no = acc_no

#     def debit(self,ammount):
#         self.balence -= ammount
#         print("Rs",ammount," debited")
#         print("you balence is:",self.get_balence())
#     def credit(self,ammount):
#         self.balence += ammount
#         print("Rs",ammount," credited")
#         print("you balence is:",self.get_balence())
#     def get_balence(self):
#         return self.balence
    
        
# acc_1 = account(10000,101)
# acc_1.credit(98250)
# acc_1.debit(56000)
# print(acc_1.balence)

#del keyword
# class account:

#     def __init__(self,balence,acc_no):
#         self.balence = balence
#         self.acc_no = acc_no

#     def debit(self,ammount):
#         self.balence -= ammount
#         print("Rs",ammount," debited")
#         print("you balence is:",self.get_balence())
#     def credit(self,ammount):
#         self.balence += ammount
#         print("Rs",ammount," credited")
#         print("you balence is:",self.get_balence())
#     def get_balence(self):
#         return self.balence
    
        
# acc_1 = account(10000,101)
# acc_1.credit(98250)
# acc_1.debit(56000)

# del(acc_1)
# print(acc_1.balence)

#to make a attribute private just do __ befor name in constructor
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#         # print(self.__acc_pass)
#     def __hello(self):
#         print("hello")
#     def welcome(self):
#         self.__hello()

# acc1 = Account("101","abcd")
# # print(acc1.__acc_pass)
# acc1.welcome()

#inheritance--some properties which we take form parent
#3 types--1)single inheritance
# class car:
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("stop")
# class toyotacar(car):
#     def __init__(self,name):
#         self.name = name
# car1 = toyotacar("helix")

# car1.start()

#2)multi-lable inheritance
# class car:
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("stop")
# class toyotacar(car):
#     def __init__(self,brand):
#         self.brand = brand
# class helix(toyotacar):
#     def __init__(self, name):
#         self.name = name
        
# car1 = helix("pratrol")
# car1.start()

#super()--use to inheritaed properties of parent constructor

class car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("stop")
class toyotacar(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        # self.type = type
car1 = toyotacar("helix","electric")
print(car1.type)


#class decorator--to change somthing in class from object method
# class student:
#     name = "unknown"
#     @classmethod
#     def change_name(cls,name):
#         cls.name = name
# s1 = student()
# s1.change_name("joy")
# print(s1.name)

#property decode--to change some attributes directly
# class student:
#     def __init__(self,name,chem,phy,math):
#         self.name = name
#         self.chem = chem
#         self.phy = phy
#         self.math = math
#     @property
#     def percentage(self):
#         return str((self.chem+self.phy+self.math)/3)+"%"
    
# s1 = student("joy",78,99,84)
# print(s1.percentage)
        
#polymorphism--same operater have multiple meaning according to its contexts
# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img= img
#     def show(self):
#         print(self.real,"i +",self.img,"j")
#     def __add__(self,num2):
#         newreal = self.real+num2.real
#         newimg = self.img+num2.img
#         return complex(newreal,newimg)

# num1= complex(4,6)
# num1.show()
# num2=complex(9,3)
# num2.show()
# num3 = num1 + num2
# num3.show()
