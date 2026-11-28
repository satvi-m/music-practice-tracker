def create_todo_list():

    print("Your To-Do List:")

    # Initializing an empty list to store the tasks of the to-do list
    todo_list = []

    # Prompting the user to enter tasks for their to-do list until they type 'done'
    while True:
        task = input("Enter a task to add to your to-do list (or type 'done' to finish): ")
        if task.lower() == 'done' and todo_list == []:
            print("No tasks were added!")
            return
        if task.lower() == 'done':
            break
        else:
            todo_list.append(task)

    # Saving the to-do list to a file using "w" mode to overwrite the past to-do list and save the new one
    with open("todo_list.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")

    # Displaying the to-do list in a numbered list format
    print("\nYour To-Do List:")
    for i, task in enumerate(todo_list, start=1): # uses enumerate to get both the index and the task, starting the index at 1 for a convenient numbering format
        print(f"{i}. {task}")

def view_todo_list():

    print("\n--- Viewing Your To-Do List ---")
    
    # Reading the to-do list from the file and displaying it in a numbered list format
    with open("todo_list.txt", "r") as file:
        todo_list = file.readlines() # reads all the lines from the file and stores them in a list called todo_list, where each line is a task in the to-do list
        # Checking if the to-do list is empty and displaying a message if it is
        if todo_list == []:
            print("Your to-do list is empty!")
            return
        # Displaying the to-do list in a numbered list format for easy readability and organization
        else:    
            print("Your To-Do List:")
            # Using enumerate to get both the index and the task, starting the index at 1 for a convenient numbering format
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task.strip()}")
