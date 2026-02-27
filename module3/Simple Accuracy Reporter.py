# Ask the user to enter a floating-point accuracy value
accuracy_input = input("Enter model accuracy: ")

# Validate that the input is numeric
try:
    accuracy = float(accuracy_input)  # Explicit type conversion
    print(f"Model accuracy is {accuracy}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")