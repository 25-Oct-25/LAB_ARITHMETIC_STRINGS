


price = 2.98635
print("Price of item: $" + str(round(price,2))) #done

quantity = 3
print("Quantity: " + str(quantity)) #done

tax_rate = 7.5
print("Tax rate: " + str(tax_rate) + "%\n")

subtotal = price * quantity
print("Subtotal: $" + str(round(subtotal, 2)))

tax = subtotal * (tax_rate / 100)
print("Tax: $" + str(round(tax, 2)))

total = subtotal + tax
print("Total: $" + str(round(total, 2)))







