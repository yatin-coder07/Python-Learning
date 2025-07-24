k = 3.14
y = 4
z = 5

# Different math operations (uncomment one at a time to see results)
result = round(k)      # Rounds k to nearest integer (3)
# result = abs(y)      # Absolute value of y (4)
# result = pow(y, 3)   # 4 to the power of 3 (64)
# result = max(k, y, z) # Returns largest value (5)
# result = min(k, y, z) # Returns smallest value (3.14)

print(result)

# Import the math module which contains mathematical functions and constants
import math

# Assign the value 9.9 to variable x
x = 9.9

# These are commented out examples of other math operations:
# print(math.pi)      # Prints the value of π (pi) - approximately 3.141592653589793
# print(math.e)       # Prints the value of e (Euler's number) - approximately 2.718281828459045
# result = math.sqrt(x)  # Calculates the square root of x (√9.9 ≈ 3.1464)
# result = math.ceil(x)  # Rounds x UP to the nearest integer (10)

# Calculate the floor of x (rounds DOWN to nearest integer) and store in result
result = math.floor(x)  # Returns 9 since 9.9 rounds down to 9

# Print the final result
print(result)  # Output will be: 9