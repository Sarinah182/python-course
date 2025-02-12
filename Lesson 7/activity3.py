print ("enter marks obtain in 5 subjects")
mark1=int (input("enter the marks:")) 
mark2=int (input("enter the marks:"))
mark3=int (input("enter the marks:"))
mark4=int (input("enter the marks:"))
mark5=int (input("enter the marks:"))
total= mark1+mark2+mark3+mark4+mark5
average=total/5 
print ("total marks",total)
print ("average marks",average)
if average >= 91 and average <= 100 :
    print ("your grade is A1")
elif average >=81 and average <=91 :
    print ("your grade is A2")
elif average >=71 and average <=81 :
    print ("your grade is B1")
elif average >=61 and average <=71 :
    print ("your grade is B2")
elif average >=51 and average <=61 :
    print ("your grade is C1")
elif average >=41 and average <=51 :
    print ("your grade is C2")
elif average >=31 and average <=41 :
    print ("your grade is D")
elif average >=21 and average <=31 :
    print ("your grade is E1")
elif average >=11 and average <=21 :
    print ("your grade is E2")
else:
    print ("invalid input"
