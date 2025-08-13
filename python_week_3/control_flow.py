# Create a function that calculates the final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else: 
        return price

# Get user input and calculate and display the final price
original_price = float(input("Enter the original price: $"))
discount_percent = float (input("Enter the discount percent:"))
final_price = calculate_discount(original_price, discount_percent)
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: ${final_price}")
else:
    print(f"No discount. Original price: ${original_price:.2f}")