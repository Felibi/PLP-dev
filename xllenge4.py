# create a file called input.txt
with open("input.txt", "w") as file:
    file.write("Hello, this is a new file.")
    file.write("\nThis file is created using Python.")
    file.write("\nThis is the third line.")
    file.write("\nThis is the fourth line.")
    file.write("\nThis is the fifth line.")
    file.close()

# Read the contents of input.txt
with open("input.txt", "r") as file:        # Open the file in read mode
    content = file.read()                   # Read the entire file
    print(content)
    file.close()

# Count the number of words in input.txt
word_count = len(content.split())
print(f"Number of words in the input.txt: {word_count}")

# Convert all text to uppercase in input.txt
with open("input.txt", "r") as file:
    content = file.read()
    content = content.upper()
    print(content)
    file.close()

# Write the processed text and the word count to output.txt
with open("output.txt", "w") as file:
    file.write(content)
    file.write(f"\nNumber of words: {word_count}")
    file.close()

# Print success message once the new file is created
print("Processing complete. Check output.txt for results.")