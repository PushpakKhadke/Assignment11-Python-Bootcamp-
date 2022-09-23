# 2. Write a python script to calculate sum of squares of first N natural numbers

Number=int(input("Enter the Number: "))
Sum=0
for i in range(1,Number+1):
    print(i**2,end=" ")
    Sum+=i**2
print("\nSum of square of numbers from 1 to", Number, "is :", Sum)
print()

