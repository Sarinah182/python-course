print ("select your ride")
print ("1.bike")
print ("2.car")
choice=int (input("enter your choice"))
if choice==1: 
    print ("what type of bike")
    print ("1.scooty")
    print ("2.scooter")
    choice2=int(input("enter your choice"))
    
    if choice2== 1:
        print ("you have selected scooty")
    else :
        print ("you have selected scooter ")
elif choice==2: 
    print ("what type of car?")
    print ("1.sedan")
    print ("2.xuv")
    choice3=int (input("enter your choice"))
    if choice3==1:
        print ("you have selected sedan")
    else : 
        print ("you have selected xuv")
else: 
    print ("wrong choice")