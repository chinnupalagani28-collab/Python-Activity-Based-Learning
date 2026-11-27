# Warehouse Inventory Reconciliation
# Python Activity-Based Learning - Case Study 14

count = int(input("Number of products: "))
for i in range(count):
    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    received = int(input("Received quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    recorded = int(input("Recorded closing stock: "))
    target = int(input("Target stock: "))

    if opening < 0 or received < 0 or dispatched < 0 or recorded < 0 or target < 0:
        print("Invalid stock data")
    elif dispatched > opening + received:
        print("Invalid: dispatch exceeds available stock")
    else:
        expected = opening + received - dispatched
        difference = recorded - expected
        print("Product:", name)
        print("Expected closing stock:", expected)
        if difference == 0:
            print("Status: Reconciled")
        else:
            print("Discrepancy:", difference)
        if recorded < target:
            print("Replenishment required:", target - recorded)
        else:
            print("Replenishment required: 0")
