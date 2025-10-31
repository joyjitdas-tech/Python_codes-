#ques-1
# class cirle:
#     def __init__(self,redius):
#         self.redius = redius
#     def area(self):
#         return 3.14*(self.redius**2)
#     def perimeter(self):
#         return 2* 3.14*self.redius
# circle1 = cirle(5)
# print("area of the circle is: ",circle1.area())
# print("perimeter of the circle is: ",round(circle1.perimeter(),2))


#ques-2
class employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def show_details(self):
        print("my role is:",self.role,"at",self.dept,"department"," & salary is: ",self.salary)
class engineer(employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("sde","it",120000)
engg1 = engineer("joyjit",24)
engg1.show_details()

#ques-3
class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,ord2):
        return self.price > ord2.price


ord1 = order("chips",5)
ord2 = order("samosa",25)
if(ord1>ord2):
    print("greater price")
else:
    print("false")

