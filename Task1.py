price: float = 2.99
quantity: int = 3
tax_rate: float = 0.075


subtotal: float = price * quantity 

tax: float = subtotal * tax_rate 

total: float = subtotal + tax




print(f"price per item :{price:.2}")
print(f"Quantity :{quantity}")
print(f"tax reat : {tax_rate*100:.1f}")
print("-"*50)
print(f"subtotal     : SAR {subtotal:.2f}")
print(f"tax          : SAR {tax:.2f}")
print(f"total        : SAR {total:.2f}")