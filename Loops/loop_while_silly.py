start = 100
while start > 0:
    print(f"Your number of something is: {start}")
    action = input("Choose action (add/remove/quit): ").lower()
    if action == "remove":
        start -= 20
        print("You lost 20 something :)")
    elif action == "add":
        start += 10
        print("You gained 10 soomething :D")
    elif action == "quit":
        print("Exiting the most useful and entertaining game.")
        break
    else:
        print("Invalid action. Please, learn typing :)")
else:
    print("Game Over! No more something")

