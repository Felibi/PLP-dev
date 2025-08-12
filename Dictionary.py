from turtle import clear, st


staffID = {1001 : 'Felix', 1002 : 'Anna', 1003 : 'John', 1004 : 'Emma', 1005 : 'Tom'}  # create a dictionary for staff IDs

staffID[1006] = 'Sophia'                # adds a new staff member named Sophia (value) with staff ID 1006(key)
staffID[1002] = 'Annie'                 # updates the name for staff ID 1002 to Annie

print(staffID)                          # outputs the dictionary of staff IDs
print(staffID[1001])                    # outputs the name associated with staff ID 1001
print(staffID.keys())                   # outputs all keys in the dictionary
print(staffID.values())                 # outputs all values in the dictionary
print(staffID.items())                  # outputs all key-value pairs in the dictionary

print(len(staffID))                     # outputs the number of entries in the dictionary
print(sorted(staffID))                  # outputs the dictionary sorted by keys
# print(clear())                          # clears the dictionary, removing all entries

del staffID[1005]                       # deletes the entry for staff ID 1005

print(staffID.get(1005))                         # outputs the updated dictionary after deletion

print(staffID[1005]) if 1005 in staffID else "Staff ID 1005 not found"  # checks if staff ID 1005 exists and prints its value or a message

# Dict membership test || we can test if a key exists in the dictionary using the keyword 'in'
# Membership test are only for keys and not for values
print(1001 in staffID)                   # outputs True
print(1005 in staffID)                   # outputs False

# Iterating over keys
for v in staffID:
    print(staffID[v])              # outputs each key-value pair
