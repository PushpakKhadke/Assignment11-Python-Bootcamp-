# 5. Write a python script to calculate sum of first N even natural numbers

Number=int(input("Enter the Number: "))
Sum=0
for i in range (1,Number*2,2):
    print(i+1,end=" ")
    Sum+=i+1
print("\nSum of even numbers from 1 to", Number*2, "is :", Sum)
print()