# 3. Write a python script to calculate sum of cubes of first N natural numbers

Number=int(input("Enter the Number: "))
Sum=0
for i in range(1,Number+1):
    print(i**3,end=" ")
    Sum+=i**3
print("\nSum of cubes of  numbers from 1 to", Number, "is :", Sum)
print()

