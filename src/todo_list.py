def create_todo_list():

    print("Your To-Do List:")

    # Initializing an empty list to store the tasks of the to-do list
    todo_list = []

    # Prompting the user to enter tasks for their to-do list until they type 'done'
    while True:
        task = input("Enter a task to add to your to-do list (or type 'done' to finish): ")
        if task.lower() == 'done':
            break
        else:todo_list.append(task)

    # Displaying the to-do list in a numbered list format
    print("\nYour To-Do List:")
    for i, task in enumerate(todo_list, start=1): # uses enumerate to get both the index and the task, starting the index at 1 for a convenient numbering format
        print(f"{i}. {task}")
