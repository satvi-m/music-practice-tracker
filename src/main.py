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
        
# displaying the main menu for the program
menu = """
What would you like to do?
1. Log a practice session
2. Set a weekly practice goal
3. Get some motivation!
4. Create a to-do list
5. Exit the program
"""
print(menu)
choice = input("Enter your choice (1-5): ")
