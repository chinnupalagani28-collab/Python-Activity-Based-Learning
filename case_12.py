# Attendance Recovery Computation
# Python Activity-Based Learning - Case Study 12

conducted = int(input("Classes conducted: "))
attended = int(input("Classes attended: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance data")
else:
    percentage = attended / conducted * 100
    print("Current attendance:", round(percentage, 2), "%")
    if percentage >= 75:
        print("No extra classes required")
    else:
        future = 0
        while (attended + future) / (conducted + future) * 100 < 75:
            future = future + 1
        print("Consecutive classes to attend:", future)
        print("Attendance after those classes:",
              round((attended + future) / (conducted + future) * 100, 2), "%")
