def swap(x, y):
    """
    Task 1
    - Swaps the values of x and y using only x and y as variables.
    - x and y must be numeric.
    - Returns -1 if x and y are not numeric.
    - Prints the swapped values if both x and y are numeric.
    """

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # Print original values 
    print(f"Original values: x = {x}, y = {y}")

    # Swapping logic
    x,y = y,x

    # Print the swapped values
    print(f"Swapped values:  x = {x}, y = {y}")

print("Scenario 1: ")
result1 = swap("Apple", 10)
print({result1})

print("\nScenario 2: ")
result2 = swap(9, 17)
print({result2})
