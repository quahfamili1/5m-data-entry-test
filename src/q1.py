def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    
    result = "" 
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        result = "-1"

    # Swapping logic
    else:
        x,y = y,x
        result = "Swapped values:  x = " + str(x) + ", y = " + str(y) 
        
    return result

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

print("Scenario 1: ")
result1 = swap("Apple", 10)
print(result1)

print("\nScenario 2: ")
result2 = swap(9, 17)
print(result2)
