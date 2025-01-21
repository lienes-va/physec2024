# Create a tuple
numbers = (10, 20, 30, 40, 50)

# Accessing elements
print(numbers[0])  # Output: 10
print(numbers[1:])  # Output: (20, 30, 40, 50)

# Nested tuples
nested_numbers = (1, 2, (3, 4), 5)
print(nested_numbers[2])  # Output: (3, 4)

# Tuple unpacking
point = (8, 9, 10)
x, y, z = point
print(f"x: {x}, y: {y}, z: {z}")  # Output: x: 8, y: 9, z: 10

# Using with functions
def get_coordinates():
    return (10, 20, 30)

x, y, z = get_coordinates()
print(f"x: {x}, y: {y}, z: {z}")  # Output: x: 10, y: 20, z: 30


# Tuple with different data types
person = ("Liene", 39, 1.60, True)

# Accessing individual elements
print(person[0])  # Output: Liene
print(person[1])  # Output: 39
print(person[2])  # Output: 1.6
print(person[3])  # Output: True

# Using *args to collect a tuple of arguments
def summarize(*args):
    total = sum(args)
    print(f"Total sum of arguments: {total}")

summarize(10, 20, 30, 40, 50)  # Output: Total sum of arguments: 150

# Comparing tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 5, 4)

print(tuple1 < tuple2)  # Output: True (compares elements sequentially)
print(tuple1 == tuple2)  # Output: False

# Tuple with numbers
numbers1 = (10, 20, 30, 40, 50)

# Find the minimum and maximum values
print("Min:", min(numbers1))  # Output: Min: 10
print("Max:", max(numbers1))  # Output: Max: 50