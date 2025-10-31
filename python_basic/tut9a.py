import random
import string
pass_len = int(input("enter the lenght of password"))
charvalues = string.ascii_letters + string.punctuation  + string.digits
# password = ""
# for i in range(pass_len):
#     password +=random.choice(charvalues)

# print(password)

#list comprehension
res = "".join([random.choice(charvalues) for i in range(pass_len)])
print(res)