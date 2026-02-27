# Function 1: Greeting
def greet_student(name):
    return f"Hello, {name}"


# Function 2: Calculate subjects and average
def calculate_scores(scores):
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects
    return num_subjects, average_score


# Function 3: Determine result
def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Main function
def main():
    # Input
    student_name = input("Enter student name: ")
    
    scores_input = input("Enter scores separated by space: ")
    scores = [float(score) for score in scores_input.split()]
    
    # Function calls
    greeting = greet_student(student_name)
    subjects, average = calculate_scores(scores)
    result = evaluate_result(average)
    
    # Final output
    print("\n" + greeting)
    print(f"Subjects: {subjects}")
    print(f"Average Score: {average}")
    print(f"Result: {result}")


# Start the program
main()