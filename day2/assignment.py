# A program that asks for their birth year and calculates their current age automatically.
current_year = int(input("Enter the current year: "))
year_of_birth = int(input("Enter your birth year: "))
current_age = current_year - year_of_birth
print(f"You are", current_age, "years old")


age = int(input("Enter your age: "))
next_year_age = age + 1
print("You will be", next_year_age, "years old next year.")
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")