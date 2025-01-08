c=0
ans="yes"
for i in range(1,6):
        print("you completed",i,"km")
        ans=input("are you tired?")
        if ans=="no":
            print("continue")
            c=c+1
        else:
            print("u ran", c, "kms,but didn't complete the race")
            c=c+1
            break
if c==5:
    print("congrats")
