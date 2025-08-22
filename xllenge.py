from os import name

'''
listA = input("Enter a list of numbers integers separated by spaces: ").split()     # Get input from user and split into a list
listA = [int(num) for num in listA]                                                 # Convert input strings to integers

print(listA)
print(sum(listA))                                       # Outputs the sum of all elements in the list
print(max(listA))                                       # Outputs the maximum value in the list
print(min(listA))                                       # Outputs the minimum value in the list

listA.sort()                                            # Sorts the list in ascending order

# Next

tupFav = 'Think & Grow Rich', 'Divine Direction', 'Winning Invisible Battles', 'Rich Dad, Poor Dad', 'Earths Earliest Ages'
for book in tupFav:                                     # Iterates through the tuple of favorite books
    print(book)                                         # Prints each book in the tuple

# Next
# name: , age: , FavColour: 

name = input("Enter your name: ")                        # Get user's name
age = int(input("Enter your age: "))                          # Get user's age
favColour = input("Enter your favorite color: ")        # Get user's favorite color

user = {'Name': name, 'Age': age, 'FavColour': favColour}  # Create a dictionary with user's details
print(user)                                                 # Outputs the user's details as a dictionary
print(f"Name: {name}, Age: {age}, FavColour: {favColour}")  # Outputs the user's details in a formatted string
'''
# Next

setA = set(input("Enter a set of numbers separated by comma: ").split(","))  # Get input from user and split into a set
print(setA)

setB = set(input("Enter a set of numbers separated by comma: ").split(","))  # Get input from user and split into a set
print(setB)

print(setA & setB)  # Outputs the intersection of setA and setB

'''
setA = {num.strip() for num in setA}  # Remove whitespace and create a set
setA = {int(num) for num in setA}  # Convert input strings to integers and create a set
'''