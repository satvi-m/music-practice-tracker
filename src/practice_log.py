def log_practice_session():
    
    # Logs a practice session by prompting the user for details and saving them to a file.
    
    print("\n--- Log a Practice Session ---")
    
    # Prompting the user for practice session details
    date = input("Enter the date of the practice session (YYYY-MM-DD): ")
    duration = int(input("Enter the duration of the practice session (in minutes): "))
    practiced = input("Enter what you practiced during the session: ")
    notes = input("Enter what you'd like to work on by the next sessions: ")
    
    # Saving the practice session details to a file using "a" mode to append to the file and save the details of each practice session on a new line
    with open("practice_log.txt", "a") as file:
        file.write(f"Date: {date}, Duration: {duration} minutes, Notes: {notes}, Practiced: {practiced}\n")
    
    print("Practice session logged successfully!\n")


# for later: what if user wants to log a past practice session? 
# add a feature to allow them to do that and keep all session dats in order from earliest to latest. 
# maybe use a list to store all the sessions and then sort them by date before writing to the file.