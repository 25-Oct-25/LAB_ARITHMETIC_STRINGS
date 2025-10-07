#variables
price= 2.99
quantity= 3
tax_rate= 0.075

#calculating variables
subtotal= price * quantity
tax= round(subtotal * tax_rate,2)
total= subtotal + tax

#print results
print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"tax rate: {tax_rate*100}%\n")

print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")