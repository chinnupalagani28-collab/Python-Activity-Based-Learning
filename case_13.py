# ATM Transaction Sequence Simulation
# Python Activity-Based Learning - Case Study 13

balance = 5000
accepted = 0
rejected = 0
count = int(input("Number of transactions: "))

for i in range(count):
    kind = input("Enter deposit or withdraw: ").lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Rejected: amount must be positive")
        rejected = rejected + 1
    elif kind == "deposit":
        balance = balance + amount
        accepted = accepted + 1
        print("Deposit accepted")
    elif kind == "withdraw":
        if amount > 2000:
            print("Rejected: withdrawal limit is Rs. 2000")
            rejected = rejected + 1
        elif amount > balance:
            print("Rejected: insufficient balance")
            rejected = rejected + 1
        else:
            balance = balance - amount
            accepted = accepted + 1
            print("Withdrawal accepted")
    else:
        print("Rejected: unknown transaction")
        rejected = rejected + 1

print("\nTRANSACTION SUMMARY")
print("Final balance: Rs.", round(balance, 2))
print("Accepted transactions:", accepted)
print("Rejected transactions:", rejected)
