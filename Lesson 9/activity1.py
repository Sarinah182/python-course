medical_cause=(input("did you have a medical cause Y or N"))
atten=int(input("enter the attendance of the students")) 
if medical_cause=="Y" : 
    print ("you are allowed")
else :
    if atten >= 75 :
        print ("Allowed")
    else :
        print ("not Allowed")