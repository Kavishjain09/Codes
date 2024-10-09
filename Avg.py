# Defining a class
class MarkRecord:
    def __init__(self, year, class_name, subject, student_name, marks):
        self.year = year
        self.class_name = class_name
        self.subject = subject
        self.student_name = student_name
        self.marks = marks

# Create an array of mark records
mark_records = [
    MarkRecord(2020, "FE - Mech", "Math", "Rahul", 55),
    MarkRecord(2020, "SE - Civil", "Fluid Mech", "Smita", 67),
    MarkRecord(2020, "FE - Mech", "Math", "Ankit", 60),
    MarkRecord(2020, "SE - Civil", "Fluid Mech", "Rajesh", 72),
    MarkRecord(2020, " - CSE", "Physics", "Neha", 70),
    MarkRecord(2020, "SE - Civil", "Math", "Priya", 65),
    MarkRecord(2020, "TE - CSE", "Physics", "Vishal", 62),
    MarkRecord(2020, "SE - Civil", "Math", "Rohit", 68),
    MarkRecord(2021, "FE - ECE", "Electronics", "Amit", 75),
    MarkRecord(2021, "SE - Mech", "Thermodynamics", "Gaurav", 80)
]
def calculate_average_marks(mark_records):
    # Create a dictionary to store the total marks and count for each class and subject
    class_subject_marks = {}
    # Calculate the total marks and count for each class and subject
    for record in mark_records:
        class_subject_key = (record.year, record.class_name, record.subject)
        if class_subject_key in class_subject_marks:
            total_marks, count = class_subject_marks[class_subject_key]
            total_marks += record.marks
            count += 1
            class_subject_marks[class_subject_key] = (total_marks, count)
        else:
            class_subject_marks[class_subject_key] = (record.marks, 1)

    # Calculate the average marks for each class and subject
    for key, value in class_subject_marks.items():
        year, class_name, subject = key
        total_marks, count = value
        average_marks = total_marks / count
        print(f"{year} | {class_name} | {subject} | {average_marks}")
calculate_average_marks(mark_records)
