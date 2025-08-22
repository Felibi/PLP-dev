my_list = []                        # Initialize an empty list
# my_list.append(10, 20, 30, 40)  # Attempt to append multiple elements at once (this will raise an error)

my_list.append(10)                  # Append 10 to the list
my_list.append(20)                  # Append 20 to the list
my_list.append(30)                  # Append 30 to the list
my_list.append(40)                  # Append 40 to the list

my_list.insert(1, 15)               # Insert 15 at index 1
my_list.extend([50, 60, 70])        # Extend the list with multiple elements
my_list.remove(my_list[-1])         # Remove the last element from the list

my_list.sort()                       # Sort the list in ascending order
print(my_list)                       # Output the list

my_list.index(30)                    # Find the index of the first occurrence of 30
print(my_list.index(30))             # Output the index of 30