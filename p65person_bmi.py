BMI=float(input("enter BMI="))
if BMI<=0:
    print("enter BMI correctly")
elif BMI<18.5:
    print("you are underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("you are normal weight")
elif BMI>=25 and BMI<=29.9:
    print("you are overweight")
elif BMI>=30:
    print("you are obese")
