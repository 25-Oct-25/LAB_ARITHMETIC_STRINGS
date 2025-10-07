# نواف البريكان

price =2.99
quantity = 3
tax_rate=0.075
subtotal = price * quantity
tax= subtotal * tax_rate
total= subtotal + tax
print("Prie of item: $", price)
print("Quantity:", quantity)
print("Tax rate:", tax_rate*100,"%")

print("")

print("Subtotal: $", subtotal)
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
