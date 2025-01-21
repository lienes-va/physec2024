#For loop

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 0]
for elements in numbers:
    print(elements) #Output (in column): 2 3 4 5 6 7 8 9 0


for el in reversed(numbers):
    print(el) #Output: reversed numbers

for i in range(6):
    print(i)    # Output 0 to 5

mixed_numbers = [2, 1, 3, 7, 4, 5, 8, 6, 19, 7, 8, 9, 0]
for num in sorted(mixed_numbers):
    print(num) #Output: sorted numbers

student = {"name": "Liene", "age": 39, "height": 1.60, "city": "Riga"}
for key, value in student.items():
    print(f"{key}: {value}")
#Output:
#name: Liene
#age: 39
#height: 1.6
#city: Riga

university = "Vidzemes Augstskola"
for char in university:
    print(char) #Output (in column): Vidzemes Augstskola


#While 
username = ""
password = ""
while username != "admin" or password != "123":
    username = input("Enter username: (hint: admin)")
    password = input("Enter password: (hint: 123)")
print("Access granted!")

while True:
    value = int(input("Enter a positive number: "))
    if value > 0:
        break
    print("Invalid input. Try again.")
print(f"You entered: {value}")

