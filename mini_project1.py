# This is a CLI Student Grade

# Mini Project 1: Student Grade Classifier


# Student data (name → score)
students = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 65,
    "Neville": 45
}

# Function to determine grade
def get_grade(score):
    if score >= 91 and score <= 100:
        return "Outstanding"
    elif score >= 81:
        return "Excellent"
    elif score >= 71:
        return "Very Good"
    elif score >= 61:
        return "Good"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"
        

#Function to process students
def process_students(data):
    results = {}

    for name, score in data.items():
        grade = get_grade(score)
        results[name] = {
            "score": score,
            "grade": grade
        }

    return results

#Function to display results
def display_results(results):
    print("\nStudent Grade Report")
    print("----------------------")
    print("Name\t\tScore\tGrade")
    print("----------------------")

    for name, info in results.items():
        print(f"{name}\t\t{info['score']}\t{info['grade']}")

# 5. Run the program
final_results = process_students(students)
display_results(final_results)