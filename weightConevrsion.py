# Python Weight Converter Program

# Get user's weight as a float number (allows decimal values)
weight = float(input("Enter your weight: "))

# Ask for weight unit (K for Kilograms or L for Pounds)
unit = input("Kilograms or Pounds (K or L): ")

# Check if unit is Kilograms (K)
if unit == "K":
    # Convert kilograms to pounds (1 kg = 2.205 lbs)
    weight = weight * 2.205
    # Update the unit to pounds
    unit = "Lbs."
    # Display converted weight rounded to 1 decimal place
    print(f"Your weight is: {round(weight, 1)} {unit}")

# Check if unit is Pounds (L)
elif unit == "L":
    # Convert pounds to kilograms (1 lb = 1/2.205 kg)
    weight = weight / 2.205
    # Update the unit to kilograms
    unit = "Kgs."
    # Display converted weight rounded to 1 decimal place
    print(f"Your weight is: {round(weight, 1)} {unit}")

# Handle invalid unit input
else:
    # Note: There's an issue here - 'main' is not defined in this code
    # This would cause an error if an invalid unit is entered
    # Better alternative would be:
    # print(f"Error: '{unit}' is not a valid unit. Please enter K or L.")
    print(f"{unit} was not valid")