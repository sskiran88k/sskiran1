Total_Amount=int(input("Enter Amount: "))
print(Total_Amount)
if Total_Amount > 1000 :
    Total_after_disc = Total_Amount*0.8
    print("Paid Amount is: ", Total_after_disc)
elif Total_Amount < 999 and Total_Amount > 499 :
    Total_after_disc = Total_Amount*0.7
    print("Paid Amount is: ", Total_after_disc)
else :
    print("Paid Amoutn is: ", Total_Amount)
