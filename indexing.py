# Indexing = accessing elements of a sequence using [] (indexing operator)
# Basic syntax: [start : end : step]

credit_number = "1234-5678-9012-3456"

# Example 1: Access first character (index 0)
# print(credit_number[0])  # Output: '1'

# Example 2: Get first 4 characters (indices 0 to 3)
# print(credit_number[:4])  # Output: '1234'

# Example 3: Incorrect usage - start:end:step with invalid range
# print(credit_number[:5:9])  # Doesn't make practical sense (output: '1')

# Example 4: Get first 5 characters stepping by 1 (normal forward sequence)
# print(credit_number[:5:1])  # Output: '1234-'

# Example 5: Get last character (negative index starts from end)
# print(credit_number[-1])  # Output: '6'

# Example 6: Corrected version - get every other character (step of 2)
print(credit_number[::2])  # Output: '13-68-02-46's