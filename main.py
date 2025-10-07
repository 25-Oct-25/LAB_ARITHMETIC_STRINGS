price = 2.99
quantity = 3
tax_rate = 0.075

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
print("price: $", price)
print("quantity: $", quantity)
print(f"tax rate: {tax_rate * 100}%")

print("\nsubtotal: $", round(subtotal, 2))
print("tax: $", round(tax, 2))
print("total: $", round(total, 2))