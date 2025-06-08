def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        print("Error: Both inputs must be numeric.")
        return None

    if divisor == 0:
        print("Error: Cannot divide by zero.")
        return None

    return num % divisor == 0


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print("Scenario 1: ")
print(check_divisibility(10, 2))

print("\nScenario 2: ")
print(check_divisibility(7, 3))
