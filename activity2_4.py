#profit and loss
#write a program to check if a person buying an orange at 100 rupees and later selling it at 120 rupees find that he has made a profit or loss
actual_cost=float(input("please enter the actual price"))
sale_amount=float(input("please enter the sale amount"))
if(sale_amount > actual_cost):
  amount=sale_amount-actual_cost
  print("total profit={0}".format(amount))
else:
  print("no profit")