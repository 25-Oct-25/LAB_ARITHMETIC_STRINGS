price:float = 2.99
quantity:int = 3
tax_rate = 0.075
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax 

print("Price of item: $" +str(price) )
print(f"Quantity: {quantity}")
print("Tax rate: {}%".format(tax_rate*100))

print("\nSubtotal: ${}".format(subtotal))
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")