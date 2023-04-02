zeros=positives=negatives=0
print("Enter the -1 to Exit: ")
while(1):
    a=int(input("Enter the a value: "))
    if(a==-1):
        break
    elif(a==0):
        zeros=zeros+1
    elif(a>0):
        positives=positives+1
    else:
        negatives=negatives+1
print("The Number of Zeros: ", zeros)
print("The Number of Positives: ", positives)
print("The Number of negatives: ", negatives)

