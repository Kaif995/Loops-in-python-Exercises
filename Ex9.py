list=(1, 4, 9, 16, 25, 36, 49, 64, 81,100,49)
x=100
# x=int(input("Enter any number to find in Above Tuple :"))
index=0
for el in list:
    if(el == x):
        print("Found at index:",index)
    index+=1