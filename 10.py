# 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)

print("Enter the Decimal Number: ")
Decimal_Number = int(input())
i=0
Octal_Number=[]
while Decimal_Number!=0:
    Reminder=Decimal_Number%8
    Octal_Number .insert(i,  Reminder)
    i=i+1
    Decimal_Number=int(Decimal_Number/8)
print("Equivalent Octal Value is:")
i=i-1
while i>=0:
    print(Octal_Number [i], end="")
    i=i-1
print()
