color=input("enter color=>").lower()
if color=="green":
    print('car is allowed to go')
elif color=='yellow':
    print("car has two wait")
elif color=="red":
    print("car has to stop")
else:
    print('unrecognized signal')