# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)

Decimal_Number=int(input("Enter the Decimal Number: "))
Binary=0
i = 0
temp = Decimal_Number # Copy Decimal_Number
while temp>0:
    Binary = ((temp%2)*(10**i)) + Binary
    temp = int(temp/2)
    i += 1
print("Binary of {x} is : {y}".format(x = Decimal_Number, y = Binary))
print()
