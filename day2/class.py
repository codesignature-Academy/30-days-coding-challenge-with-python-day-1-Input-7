"""
print("Welcome to the arithmetic Operations program!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose an option:\n1) Addition\n2) Subtract\n3) Division\n4)Multiplication\n5) Exponentiation")

option = (input(""))

if option == "1":
    print("The Sum of ", num1, "and", num2, "is", num1 + num2)
elif option == "2":
    print("The Difference between ", num1, "and", num2, "is", num1 - num2)
elif option == "3":
    print(num1, "Divided by", num2, "is", num1 / num2)
elif option == "4":
    print("The Product of", num1, "and", num2, "is", num1 * num2)
elif option == "5":
    print(num1, "Raised to the power of", num2, "is", num1 ** num2)
else:
    print("Invalid option selected.")
""" 

age = 15
print(type(age))
age = str(age)
print(type(age))
age = float(age)
print(type(age))
