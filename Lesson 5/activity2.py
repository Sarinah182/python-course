actual_costs=float (input("please enter actual product price :"))
sale_amount=float (input("please enter sales amount :"))
if (sale_amount > actual_costs) :
    amount = sale_amount-actual_costs
    print ("total profit={0}".format(amount))
else :
    print ("no profit!!!")