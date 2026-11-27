# Student Performance Trend Analysis
# Python Activity-Based Learning - Case Study 17

subjects = ["Python", "Mathematics", "English"]
first_marks = []
second_marks = []

for subject in subjects:
    first = float(input("First exam marks in " + subject + ": "))
    second = float(input("Second exam marks in " + subject + ": "))
    if first < 0 or first > 100 or second < 0 or second > 100:
        print("Invalid marks")
        first = 0
        second = 0
    first_marks.append(first)
    second_marks.append(second)

total = 0
print("\nSUBJECT-WISE TREND")
for i in range(len(subjects)):
    change = second_marks[i] - first_marks[i]
    print(subjects[i], "change:", round(change, 2))
    if change > 0:
        print("Improvement")
    elif change < 0:
        print("Decline")
    else:
        print("No change")
    if second_marks[i] < 40:
        print("Weak subject")
    total = total + second_marks[i]

average = total / len(subjects)
print("Latest average:", round(average, 2))
if average >= 75:
    print("Overall category: Excellent")
elif average >= 50:
    print("Overall category: Satisfactory")
else:
    print("Overall category: Needs Improvement")
