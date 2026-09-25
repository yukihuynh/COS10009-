
def average(marks):
    if (len(marks) == 0):
        return 0
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"


def main():
    students = [
        {"name": "Alice", "marks": [85, 90, 78]},
        {"name": "Bob",   "marks": [60, 55, 70]},
        {"name": "Carol", "marks": []},
        {"name": "Dave",  "marks": [40, 35, 50]},
    ]

    for student in students:
        avg = average(student["marks"])
        grade = get_grade(avg)
        print(f"{student['name']}: {avg:.1f} → {grade}")


main()
