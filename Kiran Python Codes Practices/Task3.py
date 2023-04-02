###DMart Billing###

item1=int(input("Enter Item1 Cost: "))
item1_percentage=int(input("Enter item1 Percentage: "))

item2=int(input("Enter Item2 Cost: "))
item2_percentage=int(input("Enter item2 Percentage: "))

item3=int(input("Enter Item3 Cost: "))
item3_percentage=int(input("Enter item3 Percentage: "))

item4=int(input("Enter Item4 Cost: "))
item4_percentage=int(input("Enter item4 Percentage: "))

item5=int(input("Enter Item5 Cost: "))
item5_percentage=int(input("Enter item5 Percentage: "))


item1_price= item1*(100-item1_percentage)/100
item2_price= item2*(100-item2_percentage)/100
item3_price= item3*(100-item3_percentage)/100
item4_price= item4*(100-item4_percentage)/100
item5_price= item5*(100-item5_percentage)/100

total_price=item1_price+item2_price+item3_price+item4_price+item5_price
print(total_price)
