binary=int(input("Enter the binary Number: "))
decimal=0
i=0
while(binary!=0):
    reminder=binary%10
    decimal=decimal+reminder*(2**i)
    binary=binary/10
    i=i+1
print(decimal)
