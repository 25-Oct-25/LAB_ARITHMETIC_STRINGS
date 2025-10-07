price = 2.99
quantity = 3
tax_rate = 0.075

subtotal = price * quantity
tax = subtotal * tax_rate

total = subtotal + tax

print(f"Price of itemm: ${price} \n Quantity: {quantity} \n Tax rate: {tax_rate * 100}% "
      f"\n \n Subtotal: ${subtotal: .2f} \n Tax: ${tax: .2f} \n Total: ${total: .2f}")
