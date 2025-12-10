 num_items = int(input("Enter the number of items you want to buy: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    # Exit or set a default value, for simplicity, we'll stop here if invalid
    # For a real application, you'd loop until valid input is received.
else:
    # Check the condition for discount
    if num_items > 3:
        print("Discount applied")
    else:
        print("No discount")
