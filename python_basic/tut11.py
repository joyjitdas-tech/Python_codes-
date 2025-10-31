"""complie time error is-syntax error
    execution error--exception
    how to handle->try except block
"""
# with open("tut11.txt","w") as f:
#     f.write("hi my name is joyjit")
# try:
#     with open("tut11.txt","r") as f:
#         # print(f.read())
#         print(5)
#         # print(3/0)
# except FileNotFoundError:
#     print("sorry file not found")
# except NameError:
#     print("variable not found")
# except ZeroDivisionError:
#     print("you can not divide by 0")
# except Exception as e:
#     print(e)


#else-- if you sure about execution :if except not run then else print
# try:
#     f = open("tut161.txt","r")
# except FileNotFoundError:
#     print("error 404")
# else:
#     print(f.read())

#finaly--it will surely execute
# try:
#     f = open("tut161.txt","r")
# except FileNotFoundError:
#     print("error 404")
# else:
#     print(f.read())
# finally:
#     print("sure")

#raise exception
# class Bank:
#     def __init__(self,balence):
#         self.balence = balence
#     def withdrow(self,ammount):
#         if (ammount>self.balence):
#             raise Exception("paisa nahi hain")
#         if(ammount<0):
#             raise Exception("monry cant got -ve")
#         self.balence-=ammount
# ammount_to = int(input("enter ammount: "))
# obj = Bank(1100)

# try:
#     obj.withdrow(ammount_to)
# except Exception as e:
#     print(e)
# else:
#     print(obj.balence)


#custom exception--is a class
# class Myexception(Exception):
#     def __init__(self, message):
#         print(message)
        
# class Bank:
#     def __init__(self,balence):
#         self.balence = balence
#     def withdrow(self,ammount):
#         if (ammount>self.balence):
#             raise Myexception("paisa nahi hain")
#         if(ammount<0):
#             raise Myexception("monry cant got -ve")
#         self.balence-=ammount
# ammount_to = int(input("enter ammount: "))
# obj = Bank(1100)

# try:
#     obj.withdrow(ammount_to)
# except Myexception as e:
#    pass
# else:
#     print(obj.balence)

#custom exception uses_-aplication based progrram
class SequrityError(Exception):
    def __init__(self,Message):
        print(Message)
    def logout(self):
        print("logout from all device")
    

class Google:
    def __init__(self,name,email,password,device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self,email,password,device):
        if(device != self.device):
            raise SequrityError("bhai tere lag gayi")
        if(email == self.email and password == self.password):
            print(self.name)
        else:
            print("login error")
        
obj = Google("joyjit","enfm@gmail.com",35464,"android")
try:
    obj.login("enfm@gmail.com",35464,"andr11oid")
except SequrityError as e:
    e.logout()
else:
    print(obj.name)
finally:
    print("no tension")
