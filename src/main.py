# FINAL PROJECT: src/main.py

# displaying the title for the program

title = "MUSIC PRACTICE TRACKER"
for i in range(len(title)):
    print("=", end="")
    if i == len(title) - 1:
        print()
print(title)
for i in range(len(title)):
    print("=", end="")
    if i == len(title) - 1:
        print()
print()

# displaying the main menu for the program
print("What would you like to do?")
print("\n1. Log a practice session\n2. Set a weekly practice goal\n3. Get some motivation!\n4. Create a to-do list\n5. Exit the program")
choice = input("Enter your choice (1-5): ")
