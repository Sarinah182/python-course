print ("enter a number (numerator):")
numb=int (input())
print ("enter a number (denominator):")
d=int (input())
if numb % d ==0 :
    print ("\n",str(numb),"is divisible by",str(d))
else:
    print ("\n",str(numb),"is not divisible by",str(d))