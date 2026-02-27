# Ask the user for their birth year
birth_year = input("Enter your birth year: ")

# Explicit type conversion from string to integer
birth_year = int(birth_year)

# Current year is 2026
current_year = 2026

# Calculate age
age = current_year - birth_year

# Print the result
print("You are", age, "years old.")