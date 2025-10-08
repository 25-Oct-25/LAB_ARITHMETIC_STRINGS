price = 2.99
quantity = 3
tax_rate = 7.5

subtotal = price * quantity
tax = subtotal * 0.075
total = subtotal + tax

print(f"Price of item: ${round(price, 2)}")
print(f"Quantity     : {quantity}")
print(f"Tax Rate     : {tax_rate}%")
print()
print(f"SubTotal     : ${round(subtotal, 2)}")
print(f"Tax          : ${round(tax, 2)}")
print(f"total        : ${round(total, 2)}")