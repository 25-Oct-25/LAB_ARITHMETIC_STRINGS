price=2.99
quantity=3
tax_rate=7.5
subtotal=price*quantity
tax= (subtotal*tax_rate)/100
total= subtotal+tax

print(f"price of item: ${price} \nQuantity: {quantity} \nTax rate: {tax_rate}% \n\nSubtotal: ${subtotal}\nTax: ${format(tax ,'.2f')} \nTotal: ${format(total,'.2f')}")
