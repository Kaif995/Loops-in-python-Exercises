numbers=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=int(input("Enter a number to find from above Tuple: "))
i=0
while i<len(numbers):
    if(numbers[i]==x):
        print("Found at index",i)
        break
    else:
        print("WaitFinding...")
    i+=1
print("End of Loop!")
       