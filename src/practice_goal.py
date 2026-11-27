def set_weekly_practice_goal():
    # Sets a weekly practice goal by prompting the user for details and saving them to a file.
    
    print("\n--- Set a Weekly Practice Goal ---")
    
    # Prompting the user for weekly practice goal details
    goal_hours = float(input("Enter your weekly practice goal (in hours): "))
    goal_minutes = int(goal_hours * 60)  # Convert hours to minutes
    
    # Saving the weekly practice goal details to a file using "w" mode to overwrite the past goal and save the new goal
    with open("practice_goal.txt", "w") as file:
        file.write(f"Weekly Practice Goal: {goal_hours} hours ({goal_minutes} minutes)\n")
    
    print("Weekly practice goal set successfully!\n")