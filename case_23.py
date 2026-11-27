# Student Timetable Conflict Detection
# Python Activity-Based Learning - Case Study 23

count = int(input("Number of timetable entries: "))
schedules = []

for i in range(count):
    course = input("Course name: ")
    day = input("Day: ").lower()
    start = int(input("Start period: "))
    end = int(input("End period: "))
    room = input("Room: ")
    if start <= 0 or end < start:
        print("Invalid period range; entry skipped")
    else:
        entry = (course, day, start, end, room)
        schedules.append(entry)

conflict_found = False
for i in range(len(schedules)):
    course1, day1, start1, end1, room1 = schedules[i]
    for j in range(i + 1, len(schedules)):
        course2, day2, start2, end2, room2 = schedules[j]
        if day1 == day2 and room1 == room2:
            if start1 <= end2 and start2 <= end1:
                print("Conflict:", course1, "and", course2,
                      "on", day1, "in", room1)
                conflict_found = True

if conflict_found == False:
    print("No timetable conflicts found")
