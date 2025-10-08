price =19
quantity =2
tax_rate =0.15

subtotal= price * quantity
tax= subtotal * tax_rate
total= subtotal + tax

print(f"Price of item:", "$", "{:.2f}".format(price))
print(f"Quantity:", quantity)
print(f"Tax Rate:", tax_rate*100,"%\n")

print(f"Subtotal:", "$", "{:.2f}".format(subtotal))
print(f"Tax:", "$", "{:.2f}".format(tax))
print(f"Total:", "$", "{:.2f}".format(total))