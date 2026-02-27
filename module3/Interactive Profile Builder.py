# Ask for user's name
user_name = input("Enter your name: ")

# Ask for user's age
user_age_input = input("Enter your age: ")
user_age = int(user_age_input)  # Explicit type conversion

# Ask whether the user is active (True/False)
active_status_input = input("Are you an active user? (True/False): ")
active_status = active_status_input.strip().lower() == "true"  # Convert to boolean

# Print formatted summary using f-string
print(f"User {user_name} is {user_age} years old. Active status: {active_status}")