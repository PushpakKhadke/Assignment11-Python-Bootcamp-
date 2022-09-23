# 6. Write a python script to calculate factorial of a given number

Number= int(input("Enter a Number: "))
Factorial = 1
for i in range(1, Number + 1):
    Factorial = Factorial * i
print("The factorial of", Number, "is :", Factorial)
print()
