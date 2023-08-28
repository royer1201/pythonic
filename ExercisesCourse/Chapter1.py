# -------------------Exercises part 1---------------------#
#                    Question1:
print("Net4U, is the best place \n...in the world")
# --------------------------------------------------------#
#                    Question2:
import datetime
x = datetime.datetime.now()
print(x)
# --------------------------------------------------------#
#                    Question3:
full_name = input("Enter your full name")
#    print(full_name)
#   print(full_name[::-1])
#    print(' '.join(full_name[::-1]))
# --------------------------------------------------------#
#                    Question4:
import os

# Get the filename from the user
filename = input("Enter the filename: ")

# Extract the file extension
file_extension = os.path.splitext(filename)[1]

# Remove the leading dot from the extension
file_extension = file_extension.lstrip('.')

# Convert the file extension to lowercase
file_extension = file_extension.lower()

print("File extension:", file_extension)



