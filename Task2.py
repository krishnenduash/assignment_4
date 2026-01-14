filename = "output.txt"
user_first_input = input("Enter text to write to the file: ")
with open(filename, 'wt') as file:
    file.write(user_first_input + '\n')
print(f"Data successfully written to {filename}.\n")

user_additional_input = input("Enter additional text to append: ")
with open(filename, 'at') as file:
    file.write(user_additional_input + '\n')
print(f"Data successfully append to {filename}.\n")

print(f"Final content of {filename}:")
with open(filename, "rt") as file:
    print(file.read())