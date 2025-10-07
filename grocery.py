price =2.99
quantity = 3
tax_rate=0.075
subtotal = price * quantity
tax= subtotal * tax_rate
total= subtotal + tax
print("Prie of item: $", price)
print("Quantity:", quantity)
print("Tax rate:", tax_rate*100,"%")
print("Subtotal: $", subtotal)
print("Tax: $", tax)
print("Total: $", total)