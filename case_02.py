# Progressive Electricity Billing
# Python Activity-Based Learning - Case Study 2

months = int(input("Enter number of months: "))
bills = []
for month in range(months):
    units = float(input("Enter units for month " + str(month + 1) + ": "))
    if units < 0:
        print("Invalid consumption")
        bills.append(0)
    else:
        if units <= 100:
            energy_charge = units * 1.50
        elif units <= 200:
            energy_charge = 100 * 1.50 + (units - 100) * 2.50
        else:
            energy_charge = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
        bill = energy_charge + 50
        if units <= 100:
            bill = bill - bill * 0.05
        bills.append(bill)
        print("Month", month + 1, "bill: Rs.", round(bill, 2))

for i in range(1, len(bills)):
    if bills[i - 1] > 0:
        increase = (bills[i] - bills[i - 1]) / bills[i - 1] * 100
        print("Change from month", i, "to", i + 1, ":", round(increase, 2), "%")
        if increase > 25:
            print("Unusual increase detected")
