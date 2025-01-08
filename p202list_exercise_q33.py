import random

dice=[]
x=6
n=int(input("no of tries=>"))
for i in range(1,n+1):
    y=random.randint(1,6)
    dice.append(y)
print(dice)
print("you rolled six",dice.count(x),"times")

