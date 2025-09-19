'''
def calculate_discount(price, discount_percent):        # Calculate the discount based on price and discount percentage
    if price > 0:                                     # Check if the price is greater than 0
        return price - (price * discount_percent)
    return price
print(int(input(calculate_discount(price, discount_percent))))
'''

# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if price > 0 and discount_percent >= 0.2:         # Check if the discount is 20% or higher
        return price - (price * discount_percent)
    return price
print('Enter the original price:')
price = int(input())
print('Enter the discount percentage:')
discount_percent = float(input())
print(int(input(calculate_discount(price, discount_percent))))