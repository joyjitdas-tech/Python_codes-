#problem with text file--use of binary file
# with open("tut10image.png","rb") as f:
#     with open("tut10image_copy.png","wb") as wf:
#         wf.write(f.read())

#int/float/dic--only string can read and write in normal file -- to solve this we use serialization and deserialization
#serialization--process to conver python data types in JSON(java script on notation) format
#deserialization--process to convert JSON(java script on notation) in  python data types format

#serialization use list--dictionary
import json

# l = [1,2,3,4,5,6,7]
# d = {
#     "name":"joy",
#     "age":16,
# }
# with open("tut10_demo.json","w") as f:
#     json.dump(d,f,indent=4)
# with open("tut10_demo.json","r") as f:
#    print(json.load(f))

#for tupple--they can not store ,they store in list

#class handleing

# import json

# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

# def show_object(obj):
#     if isinstance(obj, Student):
#         return {
#             "name": obj.name,
#             "age": obj.age,
#             "marks": obj.marks
#         }
#     # if obj is not a Student, raise error so json knows
#     raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# stu1 = Student("joyjit", 18, 95)

# print(stu1.age)  

# with open("tut10_demo1.json", "w") as f:
#     json.dump(stu1, f, default=show_object)


#pickling--where python object trasfer into a byte system
#upickling --reverse process
import pickle
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print("i am",self.name,"my age is",self.age)

stu1 = Student("joyjit",18,78)
with open("tut10_demo2.pkl","wb") as f:
    pickle.dump(stu1,f)




""" pickle store the dat in binary format.JSON stoer the dat in human readable format"""