 #scope--you can change a global variable in local by using global key   
#enclosing scope
# def outer():
#     a = 3
#     def inner():
#         a = 1
#         print(a)
#     inner()
#     print(a)

# a = 9
# outer()
# print(a)
#inner is local and main program is global ->outer is enclosing LEGB rule follow local->enclosing->global->builtin
#as u can not directly change a value from local to global then use global keyword same here use nonlocal variable

# def outer():
#     a +=1
#     def inner():
#         nonlocal a
#         a+=1
#         print(a)
#     inner()
#     print(a)

# a = 9
# outer()
# print(a)

#decorator->its a func which take input a func and add decoration to it->it's possible because func in python are 1st class citizen
# def my_decorator(func):
#     def inner():
#         print("********")
#         func()
#         print("********")
#     return inner
# @my_decorator

# def hello():
#     print("hello")
# hello()

#decorator to fing execute time
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)# *args use to handle dynamically input in function
        print("func take time: ",func.__name__,time.time()-start,"secs")
    return wrapper
    
@timer
def hello():
    print("hello world")
hello()

@timer
def square(num):
    time.sleep(1)
    print(num**2)

# square(5)

#check right input decorater
def sanity_check(data_type):
    def outter_wrapper(func):
        def inner_wrapper(*args):
            if (type(*args) == data_type):
                func(*args)
            else:
                raise TypeError("ye nahi chalega")
        return inner_wrapper
    return outter_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

# square(4)
# import numpy as np
# print(np.__version__)