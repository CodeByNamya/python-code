import random
l1=[]
l2=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    l1.append(random.randint(1,5))
    l2.append(random.randint(1,5))
print("list1=>",l1)
print("list2=>",l2)

if l1[0]==l1[-1]:
    print("in list1 both values are same ")
else:
    print("both values in l1 are diff")
if l2[0]==l2[-1]:
    print("in list2 both values are same ")
else:
    print("both values in l2 are diff")

"""
when you want to access each value then use loop
"""


