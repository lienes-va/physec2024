from collections import Counter

# Create a list
fruits = ["apple", "banana", "apple", "strawberry", "blueberry", "apple", "pickle"]

# Access element
print(fruits[0])  # Output: apple

# Add an element
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'apple', 'strawberry', 'blueberry', 'apple', 'pickle', 'orange']

# Count occurrences of each element
counter = Counter(fruits)
print(counter)  # Output: Counter({'apple': 3, 'banana': 1, 'strawberry': 1, 'blueberry': 1, 'pickle': 1, 'orange': 1})

# Remove an element
fruits.remove("apple")  # Removes the first occurrence of 'apple'
print(fruits)  # Output: ['banana', 'apple', 'strawberry', 'blueberry', 'apple', 'pickle', 'orange']

# Iterate over a list
for fruit in fruits:
    print(fruit) #Output column of fruits
