def swap(x, y):
    """
    Task 1
    - Swaps the values of x and y using only x and y as variables.
    - x and y must be numeric.
    - Returns -1 if x and y are not numeric.
    - Prints the swapped values if both x and y are numeric.
    """
    
    result = "" 
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        result = "-1"

    # Swapping logic
    else:
        x,y = y,x
        result = "Swapped values:  x = " + str(x) + ", y = " + str(y) 
        
    return result
    
    
print("Scenario 1: ")
result1 = swap("Apple", 10)
print(result1)

print("\nScenario 2: ")
result2 = swap(9, 17)
print(result2)
