height=float (input("enter your height in centimeter:"))
weight=float (input("enter your weight in kilogram :"))
bmi= weight/ (height/100) **2
print ("your bmi is",bmi)
if bmi <= 18.5 :
    print ("you are underweight")
elif bmi <= 21.9 :
    print ("you are healthy")
elif bmi <= 29.9 :
    print ("you are overweight")
elif bmi <= 34.9 :
    print ("you are severely overweight")
elif bmi <= 39.9 :
    print ("you are obese")
else :
    print ("you are severely obese")
 