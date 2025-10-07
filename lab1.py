
item_name = "Ella Matcha"  
price = 20
quantity = 3
tax_rate = 7.5  


subtotal = price * quantity
tax = subtotal * (tax_rate / 100)
total = subtotal + tax


print(f"Item: {item_name}")
print(f"Price per item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%\n")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
