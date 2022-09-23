# 4. Write a python script to calculate sum of first N odd natural numbers

Number=int(input("Enter the Number: "))
Sum=0
for i in range(1,Number*2,2):
        print(i,end=" ")
        Sum+=i
print(f"\nSum of first {Number} odd numbers is : {Sum}")
print()


