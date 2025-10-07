price = 2.99 # 2.99$
quantity = 3 # 3 items
tax_rate = 7.5 # 7.5%

subtotal = price * quantity

tax = subtotal * (tax_rate/100)
total = subtotal + tax

print(f"Price of item: {price}$\n Quantity: {quantity}\n Tax rate: {tax_rate}%\n")
print(f"Subtotal: {subtotal}$\n Tax: {round(tax,2)}$\n Total: {round(total,2)}$\n")