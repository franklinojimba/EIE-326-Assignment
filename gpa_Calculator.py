# Ojimba Chibuike Franklin  22CN031552  COMPUTER ENGINEERING
# Assignment 1

total_points = 0
total_credits = 0

for course_number in range(1, 7):
    print(f"\n--- Course {course_number} ---")

    grade = input("Enter the letter grade (e.g., A, B+, C): ").upper()

    # Get the credits for the course
    credit_unit = float(input("Enter the number of credits for this course: "))

    # Convert the letter grade to a grade point value
    if grade == "A+":
        grade_point = 4.0
    elif grade == "A":
        grade_point = 4.0
    elif grade == "A-":
        grade_point = 3.7
    elif grade == "B+":
        grade_point = 3.3
    elif grade == "B":
        grade_point = 3.0
    elif grade == "B-":
        grade_point = 2.7
    elif grade == "C+":
        grade_point = 2.3
    elif grade == "C":
        grade_point = 2.0
    elif grade == "C-":
        grade_point = 1.7
    elif grade == "D+":
        grade_point = 1.3
    elif grade == "D":
        grade_point = 1.0
    elif grade == "D-":
        grade_point = 0.7
    else:
        grade_point = 0.0

    course_points = grade_point * credit_unit

    total_points = total_points + course_points
    total_credits = total_credits + credit_unit

gpa = total_points / total_credits

print("\n--- Results ---")
print("Your GPA is:", gpa)
