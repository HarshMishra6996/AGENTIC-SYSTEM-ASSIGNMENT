# Define the function
def check_even_odd(number):
    if number % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"

# Main code
num = 4
result = check_even_odd(num)

# Print the result (outside the function)
print(result)