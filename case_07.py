# Retail Billing with Multiple Discount Rules
# Python Activity-Based Learning - Case Study 7

count = int(input("Enter number of products: "))
subtotal = 0
for i in range(count):
    name = input("Product name: ")
    price = float(input("Unit price: "))
    quantity = int(input("Quantity: "))
    if price < 0 or quantity < 0:
        print("Invalid item; skipped")
    else:
        line_total = price * quantity
        subtotal = subtotal + line_total
        print(name, ":", quantity, "x", price, "=", round(line_total, 2))

if subtotal >= 2000:
    discount = subtotal * 0.10
else:
    discount = 0
if discount > 500:
    discount = 500

taxable = subtotal - discount
gst = taxable * 0.05
total = taxable + gst

print("\nRETAIL INVOICE")
print("Subtotal:", round(subtotal, 2))
print("Discount:", round(discount, 2))
print("GST:", round(gst, 2))
print("Amount payable:", round(total, 2))
