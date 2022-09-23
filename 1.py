# 1. Write a python script to calculate sum of first N natural numbers

Number=int(input("Enter the Number: "))
Sum=0
for i in range(Number):
    print(i+1,end=" ")
    Sum+=i+1
print("\nSum of natural numbers from 1 to", Number, "is :", Sum)
print()
