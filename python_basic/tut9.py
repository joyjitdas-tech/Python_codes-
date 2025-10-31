import random

target = random.randint(1,100)

while True:
    k = input("enter the number or press q for quit: ")
    if(k == 'q'):
        break
    k = int(k)
    if(k > target):
        print("you chose a big number!")
    elif(k<target):
        print("you chose a small number!")
    else:
        print("you find the number")
        break

print("game over")


