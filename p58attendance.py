classesheld=int(input("enter number of classes held="))
classesattended=int(input("enter number of classes attended="))
percentage=classesattended/classesheld*100
print("attendance is",percentage,"%")
if percentage<75:
    print("student is not allowed to sit in the exam")
else:
    print("student is allowed to sit in the exam")