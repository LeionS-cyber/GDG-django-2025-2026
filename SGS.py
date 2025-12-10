def get_grade(student_grades, student_name):
    """
    Tries to return the student's grade. 
    If the student does not exist, returns "Student not found in the system".
    """
    try:
        # Attempt to access the value associated with student_name
        return student_grades[student_name]
    except KeyError:
        # This block executes if student_name is not a key in student_grades
        return "Student not found in the system"

# Example usage:
grades = {
    "Alice": "A",
    "Bob": "B+",
    "Charlie": "A-"
}

print(f"Alice's grade: {get_grade(grades, 'Alice')}")
print(f"Eve's grade: {get_grade(grades, 'Eve')}")
print(f"Bob's grade: {get_grade(grades, 'Bob')}")
