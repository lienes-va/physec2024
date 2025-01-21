#Simple user input example. Please enter numbers only
while True:
    value = int(input("Enter a positive number: "))
    if value > 0:
        break
    print("Invalid input. Try again :)")
print(f"You entered: {value}")
