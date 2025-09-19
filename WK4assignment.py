with open("filput.txt", "w") as file:
        file.write("Hello, this is a sample text.")
        file.write("\nThis file is created using Python.")
        file.close()
    
with open("filput.txt", "r") as file:
    content = file.read()
    print(content)
    file.close()

with open("filput.txt", "r") as file:
    content = file.read()
    content = content.upper()
    print(content)
    file.close()

with open("filout.txt", "w") as file:
    file.write(content)
    file.close()


# Exception Handling Example

print('Enter a file name to read:')
file_name = input()
try:
    with open(file_name, "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not accessible. Please check the filename.")