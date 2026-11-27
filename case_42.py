# Student Marks Matrix Analysis
# Python Activity-Based Learning - Case Study 42

students = ["Asha", "Bala", "Charan", "Divya"]
subjects = ["Python", "Maths", "English"]
marks = []

for student in students:
    row = []
    print("Enter marks for", student)
    for subject in subjects:
        mark = float(input(subject + ": "))
        if mark < 0 or mark > 100:
            print("Invalid mark; storing 0")
            mark = 0
        row.append(mark)
    marks.append(row)

highest_total = -1
top_student = ""
print("\nSTUDENT RESULTS")
for i in range(len(students)):
    total = 0
    for j in range(len(subjects)):
        total = total + marks[i][j]
    average = total / len(subjects)
    print(students[i], "total:", total, "average:", round(average, 2))
    if total > highest_total:
        highest_total = total
        top_student = students[i]

print("\nSUBJECT AVERAGES")
for j in range(len(subjects)):
    total = 0
    for i in range(len(students)):
        total = total + marks[i][j]
    average = total / len(students)
    print(subjects[j], ":", round(average, 2))
    if average < 50:
        print("Low average subject:", subjects[j])

print("Top performer:", top_student, "with", highest_total, "marks")
