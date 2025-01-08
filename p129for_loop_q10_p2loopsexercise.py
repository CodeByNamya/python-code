import colorama
from colorama import Fore, Back, Style
colorama.init()
n=int(input("enter limit="))
s1=0
c1=0
s2=0
c2=0
for i in range(1,n+1):
    if i%2==0:
        print(Back.GREEN,Fore.BLACK,i)
        c1=c1+1
        s1=s1+i
    else:
        print(Back.BLUE, Fore.CYAN, i)
        c2=c2+1
        s2=s2+i
print(Back.CYAN,Fore.BLACK,"count of even=",c1,"sum of even=",s1)
print(Back.RED,Fore.YELLOW,"count of odd=", c2, "sum of of odd=", s2)

