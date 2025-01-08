print("temp<0: Freezing atmos")
print("temp 0-10: very cold atmos")
print("temp 10-20: cold atmos")
print("temp 20-30: Normal atmos")
print("temp 30-40: Hot atmos")
print("temp>40: very hot atmos")
temp=int(input("enter temperature->"))
if temp<0:
    print("temp<0: Freezing atmos")
elif temp>0 and temp<10:
    print("temp 0-10: very cold atmos")
elif temp>10 and temp<20:
    print("temp 10-20: cold atmos")
elif temp>20 and temp<30:
    print("temp 20-30: Normal atmos")
elif temp>30 and temp<40:
    print("temp 30-40: Hot atmos")
elif temp>40:
    print("temp>40: very hot atmos")
else:
    print("wrong input")





