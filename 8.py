# 8. Write a python script to calculate sum of digits of a given number

Number=int(input("Please Enter any Number: "))
Sum =0
while(Number > 0):
    Reminder=Number % 10
    Sum=Sum+Reminder
    Number=Number //10
print("Sum of the digits of Given Number is : %d" %Sum)
print()