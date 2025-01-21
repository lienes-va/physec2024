# Create a dictionary
person = {"name": "Liene", "age": 39, "city": "Valmiera"}

# Access values
print(person["name"])  # Output: Liene
print(person.get("city")) # Output: Valmiera

# Add a key-value pair
person["job"] = "DevOps"
print(person)  # Output: {'name': 'Liene', 'age': 39, 'city': 'Valmiera', 'job': 'DevOps'}

# Update a key-value pair
person["job"] = "DevOps specialist"
print(person)  # Output: {'name': 'Liene', 'age': 39, 'city': 'Valmiera', 'job': 'DevOps specialist'}

# Remove a key-value pair
del person["age"]
print(person)  # Output: {'name': 'Liene', 'city': 'Valmiera', 'job': 'DevOps specialist'}

# Iterate over keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Liene
# city: Valmiera
# job: DevOps specialist