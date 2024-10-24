# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F




def students_grade(mark):
    if mark >= 90:
        return "Grade A"
    elif mark >= 80:
        return "Grade B"
    elif mark >= 70:
        return "Grade C"
    elif mark >= 60:
        return "Grade D"
    elif mark >= 40:
        return "Grade E"
    else:
        return "Grade F"


try:
    student_mark = float(input("Enter your mark scored: "))
    
    
    # Checking  if the mark is within a valid range
    if 0 <= student_mark <= 100:  
        grade = students_grade(student_mark)
        print(f"You obtained: {grade}")
    else:
        print("Please enter a valid mark between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")