a=[1, 4, 5.0, 6, 8, 9, 10, 12, "Hello", True]
a.append("Kiran")
a.remove(9)
a.insert(10, "Srinith")
a.reverse()
i=0
while (i<len(a)):
    print(f"The index is : a[{i}] Type is : {type(a[i])} and value {a[i]}")
    i=i+1
