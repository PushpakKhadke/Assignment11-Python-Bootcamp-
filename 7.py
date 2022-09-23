# 7. Write a python script to count digits in a given number

Count = 0
Number = int(input("Enter a number: "))
while Number>0:
    Number = Number//10
    Count = Count + 1
print("Total number of digits :",Count)