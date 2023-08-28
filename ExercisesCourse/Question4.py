import os

# Get the filename from the user
filename = input("Enter the filename: ")

# Extract the file extension
file_extension = os.path.splitext(filename)[1]
print(file_extension)
# Remove the leading dot from the extension
file_extension = file_extension.lstrip('.')
print("File extension:", file_extension)
