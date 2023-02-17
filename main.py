#find the largest of three numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if number1 > number2 and number1 > number3:
    print("The first number is the largest")
elif number2 > number1 and number2 > number3:
    print("The second number is the largest")
elif number3 > number1 and number3 > number2:
    print("The third number is the largest")
else:
    print("There is no largest number among these numbers")

