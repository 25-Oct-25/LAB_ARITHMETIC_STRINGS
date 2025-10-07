price = 2.99 
quantity = 3
tax_rate = 7.5

subtotal = (price*quantity)

tax = (subtotal*(tax_rate/100))

total = (subtotal+tax)

print("Price of item: $" + str(price))
print("Quantity: " + str(quantity))
print("Tax rate: " + str(tax_rate) + "%")


print()

print("Subtotal: $" + str(subtotal))
print("Tax: $" + str(round(tax,2)))
print("Total: $" + str(round(total,2)))

