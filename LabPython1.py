price:float = 2.99
quantity:int = 3
tax_rate:float = 7.5
print(f"Price of item: ${price}")
print(f"Quantity: {quantity}" )
print(f"Tax rate: {tax_rate}%\n")

subtotal:float = price * quantity
print(f"Subtotal: ${subtotal}")

tax:float = subtotal * (tax_rate / 100)
print(f"Tax: $ {round(tax, 2)}")

total_cost = subtotal + tax
print(f"Total: ${round(total_cost, 2)}")