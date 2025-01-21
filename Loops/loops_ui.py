#Simple user input example. Please enter numbers only
while True:
    try:
        value = int(input("Enter a positive number: "))
        if value > 0:
            break
        print("This was definitely not a positive number, huh")
    except ValueError:
        print("Invalid input. This is not a valid number! Try again :)")
print(f"You entered: {value} well done!")
