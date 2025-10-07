'''
What I learned in this lab:
    1 - I learned how to use a set and when it should be used.
    2 - I learned that ".2f" is used to format numbers to two decimal places (e.g., 3.00).
'''


products = {
    'apple': 3.21,
    'banana': 4.32,
    'orange': 2.00,
    'mango': 4.94,
    'strawberry': 5.99,
    'grapes': 2.33
}

def fruitsStore():
    print("Hello, welcome to our store")
    print("We have the following fruits available:")
    for key in products.keys():
        print(f"- {key}")

fruitsStore()

fruit = input("\nEnter the fruit you want to buy: ").lower()


if fruit in products:
    price = products[fruit]
    quantity = int(input(f"How many {fruit}s would you like to buy? "))
    tax_rate = 0.075  # 7.5%

    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax

    print("\n----- Receipt -----")
    print(f"Item: {fruit.capitalize()}")
    print(f"Price per item: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (7.5%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("-------------------")
else:
    print("Sorry, that fruit is not available in our store.")