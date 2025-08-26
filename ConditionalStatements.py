temp = int(input())                     # Get the temperature from the user
if temp > 30:
    print("It's a hot day")
elif temp < 10:
    print("It's a very cold day")
elif temp >= 38:
    print("It's a very hot day")
elif temp <= 20:
    print("It's a cold day")
else:
    print("It's a pleasant day")


# For Loop
'''
name = input("Enter your name: ")          # Get the user's name
name = name.strip()                        # Remove any leading/trailing whitespace
name = name.lower()                        # Convert the name to lowercase
name = name.capitalize()                   # Capitalize the first letter of the name
name = name.replace(" ", "_")              # Replace spaces with underscores
name = name[:10]                            # Truncate the name to 10 characters
name = name.replace("_", " ")                # Replace underscores with spaces

name = 'Mutemi'                              # Assign a new value to the name variable

for char in name:                          # Iterate through each character in the name
    print(char)                            # Print the current character
'''

instructors = ['Alice', 'Bob', 'Charlie', 'Precious', 'James', 'Felix']       # List of instructor names

print(instructors[3])                           # Print the instructor at index 3
for instructor in instructors:                  # Iterate through each instructor in the list
    print(instructor)                           # Print the current instructor's name

# While Loop

count = 1
while count <= 5:                           # Continue looping while count is less than or equal to 5
    print(count)                            # Print the current value of count
    count += 1                              # Increment count by 1

# Loop Controls: break & continue
# The break statement is used to terminate the loop immediately it is encountered.
# The continue statement is used to skip the current iteration and move to the next iteration of the loop.

for number in range(1, 10):               # Iterate through numbers from 1 to 9
    if number == 5:                       # If the current number is 5
        print('breaking the loop at 5')   
        break                             # Exit the loop when number is 5
    elif number % 2 == 0:
        print(f"skipping {number} because it's even")
        continue                          # Skip the rest of the loop for even numbers
    print(f'Processing number: {number}')                         # Print the current number

# Nested Loops
for i in range(1, 4):                       # Outer loop
    for j in range(1, 4):                   # Inner loop
        print(f'Outer loop {i}, Inner loop {j}')               # Print the current values of i and j
                                            # The inner loop completes all its iterations for each iteration of the outer loop.

