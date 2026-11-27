# Employee Payroll and Deduction Analysis
# Python Activity-Based Learning - Case Study 4

name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive: "))

if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid salary input")
else:
    hra = basic * 0.20
    travel = basic * 0.10
    overtime = hours * 100
    gross = basic + hra + travel + overtime + incentive
    if gross <= 20000:
        deduction = gross * 0.05
    else:
        deduction = 20000 * 0.05 + (gross - 20000) * 0.10
    net = gross - deduction

    print("\nEMPLOYEE SALARY STATEMENT")
    print("Name:", name)
    print("Basic pay:", round(basic, 2))
    print("HRA:", round(hra, 2))
    print("Travel allowance:", round(travel, 2))
    print("Overtime:", round(overtime, 2))
    print("Incentive:", round(incentive, 2))
    print("Gross salary:", round(gross, 2))
    print("Deduction:", round(deduction, 2))
    print("Net salary:", round(net, 2))
