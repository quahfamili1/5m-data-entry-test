def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        print("Error: Input 'lst' must be a list.")
        return None

    modified_list = []
    for item in lst:
        if item == find_val:
            modified_list.append(replace_val)
        else:
            modified_list.append(item)
            
    return modified_list


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

print("Scenario 1: ")
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(f"Modified list: {result1}")


print("\nScenario 2: ")
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(f'Modified list: {result2}')
