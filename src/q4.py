def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return "Error: Input must be a string."
    rev_s = ""
    for char in s:
        rev_s = char + rev_s
    
    return rev_s


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print("Scenario 1: ")
print(string_reverse("Hello World"))

print("Scenario 2: ")
print(string_reverse("Python"))
