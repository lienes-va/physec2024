# Create sets
numbers_1 = {1, 2, 3, 4, 4, 5, 5, 6}
numbers_2 = {5, 4, 3, 3, 1, 7, 12, 22, 11, 1, 4}
fruits = {"apple", "banana", "apple", "strawberry", "blueberry", "apple", "pickle"} 


print(numbers_1) # Output: {1, 2, 3, 4, 5, 6} (duplicates are removed)
print(numbers_2) # Output: {1, 3, 4, 5, 7, 11, 12, 22} (ordered from smallest)
print(fruits) #Output: {'banana', 'strawberry', 'pickle', 'apple', 'blueberry'} (duplicates are removed)

# Add an element
numbers_1.add(7)
print(numbers_1)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Remove an element
numbers_2.discard(22)
print(numbers_2)  # Output: {1, 3, 4, 5, 7, 11, 12}

# Check membership
print("Is 'apple' in the set?", "apple" in fruits)  # Output: True
print("Is 'pear' in the set?", "grape" in fruits)  # Output: False


# Union: Combine elements from both sets
union_set = numbers_1.union(numbers_2)
print("Union:", union_set)  # Output: Union: {1, 2, 3, 4, 5, 6, 7, 11, 12}

# Intersection: Common elements in both sets
intersection_set = numbers_1.intersection(numbers_2)
print("Intersection:", intersection_set)  # Output: Intersection: {1, 3, 4, 5, 7}

# Difference: Elements in set_a but not in set_b
difference_set = numbers_1.difference(numbers_2)
print("Difference (numbers_1 - numbers_2):", difference_set)  # Output: Difference (numbers_1 - numbers_2): {2, 6}


# Convert a string to a set (unique characters)
text = "Vidzemes Augstskola"
char_set = set(text)
print("Set of characters:", char_set)  # Output: Set of characters: {'s', 'V', 'i', 'e', 'A', 'o', 'u', ' ', 't', 'g', 'z', 'd', 'k', 'a', 'm', 'l'}