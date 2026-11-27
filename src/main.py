# FINAL PROJECT: src/main.py

# displaying the title for the program
title = "PracticePal: Your Music Practice Tracker ˖ ݁♬⋆.˚𝄞"
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

# handling the user's choice and calling the appropriate function from the corresponding module
while choice != "5":
    if choice == "1":
        from practice_log import log_practice_session   
        log_practice_session()
    elif choice == "2": 
        from practice_goal import set_weekly_practice_goal
        set_weekly_practice_goal()
    elif choice == "3":
        from motivation import get_motivation
        get_motivation()
    elif choice == "4":
        from todo_list import create_todo_list
        create_todo_list()    
    elif choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Invalid choice. Please enter a number between 1 and 5.")
    print(menu)
    choice = input("Enter your choice (1-5): ")
if choice == "5":
    print("Thank you for using PracticePal! Goodbye!")
    exit()
