# Food Waste Monitoring System
# Python Activity-Based Learning - Case Study 53

days = int(input("Number of days: "))
for day in range(days):
    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))

    if prepared <= 0 or served < 0 or served > prepared:
        print("Invalid meal data")
    else:
        leftovers = prepared - served
        wastage = leftovers / prepared * 100
        print("Day", day + 1)
        print("Leftover meals:", leftovers)
        print("Wastage percentage:", round(wastage, 2), "%")
        if wastage > 10:
            print("Status: Above acceptable limit")
        else:
            print("Status: Within acceptable limit")
