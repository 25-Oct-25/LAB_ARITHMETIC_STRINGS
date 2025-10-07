price = 2.99
quantity = 3
tax_rate = 0.075
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax 
print (f"price of item: ${price}")
print (f"Quantity: {quantity}")
print (f"Tax rate: {tax_rate*100}% \n")

print (f"subtotal: {subtotal}")
print (f" tax: ${round(tax,2)}")
print (f"Total: ${round(total,2)}")

