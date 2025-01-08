import colorama
from colorama import Fore,Back,Style
colorama.init()
marks=int(input("enter the marks=>"))
if marks>20:
    print(Back.LIGHTBLUE_EX, Fore.BLACK,"VERY GOOD")
else:
    print(Back.RED, Fore.BLACK,"WORK HARD")