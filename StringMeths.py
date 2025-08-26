Name = "John"
print(Name)                         # outputs the value of Name variable

klass = 'custom'

message = "wai my 2k dozz"
print(message)                      # outputs the value of message variable

print(message[3])                   # outputs the character at index 3 of message variable
print(message[0:3])                # outputs the substring from index 0 to 2 of message variable
print(message[0:])                 # outputs the substring from index 0 to the end of message variable
print(message[-1])                  # outputs the last character of message variable

print('length of message is:', len(message))

# multiline string
moreLines = """This is a multiline string.
It can span multiple lines.
"""
print(moreLines)                     # outputs the multiline string

#comparing strings

strA = "Hello"
strB = "Hello"
strC = "World"

print(strA == strB)                  # outputs True
print(strA == strC)                  # outputs False
print(strA != strC)                  # outputs True
print(strA < strC)                   # outputs True
print(strA > strC)                   # outputs False

profile = klass + " " + Name         # concatenates (joins) two or more strings
print(profile)

# iterating through strings
for char in message:
    print(char)

print(message.upper())                # converts the string to uppercase
print(message.lower())                # converts the string to lowercase

print(message.replace("2k", "2000"))  # replaces "2k" with "2000" in the string
print(message.split())               # splits the string into a list of words

print(len(message))                 # outputs the length of the message
print(message.find("my"))           # outputs the index of the first occurrence of "my"
print(message.index("my"))          # outputs the index of the first occurrence of "my"
print(message.count("my"))          # outputs the number of occurrences of "my"

# string membership test

print('a' in 'klass')                # outputs False
print('a' not in 'klass')            # outputs True

# testing an actual string that is not a variable
print('a' in 'program')              # outputs True
print('a' not in 'program')          # outputs False

# Escape sequences... There is a list of escape sequences supported in python

example = "He said, \"what's going on?\"" # escape quotes (\"") allows the use of quotes within the string

# String formatting - f-Strings
male = "John"
female = "Jane"
country = 'Nigeria'
age = 30
formatted = f"My name is {male} and I am {age} years old."
print(formatted)

print(f"My name is {female} and I am {age} years old.")
print(f"my name is {female} , I am {age} years old and I live in {country}.")
