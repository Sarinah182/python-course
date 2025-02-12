string=(input("please enter your own word"))
character=input("please enter your own character")
i=0 
count=0 
while i< len(string) :
    if string [i]==character :
        count=count+1
    i=i+1
print ("total number of times",character,"has occured=",count)