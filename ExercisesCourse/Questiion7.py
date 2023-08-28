def inches_to_cm(inches):
    return inches * 2.54

def feet_to_cm(feet):
    return feet * 12 * 2.54

# Get input from the user
inches = float(input("Enter length in inches: "))
feet = float(input("Enter length in feet: "))

# Perform the conversions
cm_from_inches = inches_to_cm(inches)
cm_from_feet = feet_to_cm(feet)

# Print the results
print(f"{inches} inches is equal to {cm_from_inches:.2f} centimeters")
print(f"{feet} feet is equal to {cm_from_feet:.2f} centimeters")
