import random
c=0
heads=0
tails=0

for i in range(1,10):
    coin=random.randint(1,2)
    if coin==1:
        print("heads")
        heads+=1
        c=c+1
    else:
        print("tails")
        tails+=1
        c=c+1
print("heads is flipped",heads,"times")
print("tails is flipped",tails,"times")







