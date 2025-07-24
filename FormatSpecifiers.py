# Python String Format Specifiers Examples

# Basic value formatting
price = 123.45678
quantity = 5

# 1. Rounding to decimal places (fixed point)
print("\n1. Rounding to decimal places:")
print(f"Price: {price:.2f}")  # Rounds to 2 decimal places
print(f"Price: {price:.3f}")  # Rounds to 3 decimal places

# 2. Allocating spaces
print("\n2. Allocating spaces:")
print(f"Price: {price:10.2f}")  # Allocates 10 spaces, right-aligned by default
print(f"Quantity: {quantity:5d}") # Allocates 5 spaces for integer

# 3. Zero padding
print("\n3. Zero padding:")
print(f"Order ID: {7:03d}")      # Output: 007
print(f"Hour: {9:02d}:{5:02d}")  # Output: 09:05

# 4. Alignment
print("\n4. Alignment:")
print(f"Left: |{'text':<10}|")    # Left-aligned in 10 spaces
print(f"Right: |{'text':>10}|")   # Right-aligned in 10 spaces
print(f"Center: |{'text':^10}|")  # Center-aligned in 10 spaces

# 5. Number signs
print("\n5. Number signs:")
positive = 42
negative = -42
print(f"Default: {positive} {negative}")  # No sign for positive
print(f"Always show sign: {positive:+} {negative:+}")  # + for positive
print(f"Space for positive: {positive: } {negative: }")  # Space for positive

# 6. Sign positioning
print("\n6. Sign positioning:")
print(f"Default: {positive:=8d}")  # Sign at left, numbers right-aligned
print(f"Negative: {negative:=8d}")

# 7. Thousands separator
print("\n7. Thousands separator:")
big_number = 1234567.89
print(f"With commas: {big_number:,.2f}")  # Adds commas as thousands separators

# 8. Combining multiple flags
print("\n8. Combining flags:")
print(f"Combined: {big_number:+=20,.2f}")  # Show sign, 20 spaces, commas, 2 decimals

# 9. Percentage formatting
print("\n9. Percentage formatting:")
ratio = 0.456
print(f"Percentage: {ratio:.1%}")  # Formats as percentage with 1 decimal place

# 10. String truncation
print("\n10. String truncation:")
long_text = "This is a very long string"
print(f"Truncated: {long_text:.10}...")  # Shows only first 10 characters