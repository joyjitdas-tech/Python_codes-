#DICTIONARY & SET
student = {
    "name" : "joyjit",
    "subject": ["aiml","data","it"],
    "age" :18,
    "job":"aiml-learner",
    "score": {
        "chem": 38,
        "phys": 78,
        "math": 99,
    }
}
student["age"]="20"
#null
# null_dict={}
# null_dict["name"]="debi"
# print(student)

# print(student.keys())
# print(len(student))
#type cast
# pair = list(student.items())
# print(pair[1])
# print(student.get("score").get("phys"))
# print(student["score"]["chem"])

# student.update({"city":"howrah"})
# print(student.get("city"))

# new = {"name":"soumya","age":"29"}
# student.update(new)
# print(student)

#set
#each is unique & immutable & duplication is not allowed
# set1 ={1,2,3,4,5,3}
# print(set1)
# set_empty=set()
# set_empty.add(2)
# set_empty.add(4)
# set_empty.add(7)
# set_empty.add(1)
# print(set_empty)

# #union
# set2={2,3,4,9,8,7,4,5}
# print(set1.union(set2))
# #intersectiom
# print(set1.intersection(set2))

#ques-1
# dictionary={
#     "cat":"a animal",
#     "table":["something","made of wood"]
# }
# print(dictionary)
# #ques-2
# classroom={"py","java","java","cpp","js","py","c","cpp"}
# print(len(classroom))

#ques-3
# result ={}
# chem = int(input("marks for chem: "))
# phys=int(input("marks for phys:"))
# math=int(input("marks for math: "))
# result.update({"chemistry":chem,"physics":phys,"mathmatics":math})
# print(result)

#ques-4
values={9,'9.0'}
print(values)