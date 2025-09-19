'''
List comprehensions in Python provide a concise and elegant way to create and manipulate lists.
They offer a more readable and expressive alternative to traditional loops for generating lists.
List comprehensions can be used for various tasks, such as filtering elements, transforming data, and creating new lists from existing ones.
'''
# Basic Syntax
# new_list = [expression for item in iterable if condition]

# Traditional Loop
squares = []                            # empty list to store squares
for x in range(5):
    squares.append(x**2)
print(squares)                          # Output: [0, 1, 4, 9, 16]

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)                          # Output: [0, 1, 4, 9, 16]

# List Comprehension with condition

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)                      # Output: [0, 2, 4, 6, 8]

# List Comprehension with function
def square(x):
    return x**2

squares = [square(x) for x in range(5)]
print(squares)                          # Output: [0, 1, 4, 9, 16]

# Nested List Comprehension
# List comprehensions can be nested to handle complex operations, such as creating a matrix
# List comprehension can also be used to flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)                        # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# create a 3x3 matrix using nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)                           # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Transforming Data
names = ['Alice', 'Bob', 'Charlie']
uppercased = [name.upper() for name in names]
print(uppercased)                       # Output: ['ALICE', 'BOB', 'CHARLIE']

# Filtering Data
numbers = [10, 15, 18, 20, 25, 30]
div_by_5 = [n for n in numbers if n % 5 == 0]
print(div_by_5)                        # Output: [10, 15, 20, 25]

# Flattening a List
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatList = [item for sublist in nested_list for item in sublist]
print(flatList)                        # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Xample
result = []
for x in range(10):
    for y in range(5):
        if x + y > 5:
            result.append((x * y))

# Conclusion
# List comprehensions are a versatile and efficient tool in Python, enabling you to write cleaner and faster code. 
# They are ideal for transforming, filtering, or generating lists in a Pythonic way. 
# Start practicing them to enhance your coding skills!