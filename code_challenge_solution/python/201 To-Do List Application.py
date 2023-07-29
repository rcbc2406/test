# Importing the necessary modules
import os

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the to-do list
def display_list():
    clear_console()
    print("TO-DO LIST\n")
    if len(todo_list) > 0:
        for i, item in enumerate(todo_list):
            print(f"{i+1}. {item}")
    else:
        print("No items in the list.")

# Function to add a new task to the list
def add_task():
    clear_console()
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

# Function to mark a task as completed
def complete_task():
    clear_console()
    display_list()
    task_id = int(input("Enter the task number to mark as completed: "))
    if task_id >= 1 and task_id <= len(todo_list):
        task = todo_list[task_id-1]
        todo_list.remove(task)
        completed_list.append(task)
        print(f"Task '{task}' marked as completed.")
    else:
        print("Invalid task number.")

# Function to remove a task from the list
def remove_task():
    clear_console()
    display_list()
    task_id = int(input("Enter the task number to remove: "))
    if task_id >= 1 and task_id <= len(todo_list):
        task = todo_list[task_id-1]
        todo_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print("Invalid task number.")

# Main program loop
if __name__ == "__main__":
    todo_list = []
    completed_list = []

    while True:
        clear_console()
        print("TO-DO LIST APPLICATION\n")
        print("1. Display the to-do list")
        print("2. Add a new task")
        print("3. Mark a task as completed")
        print("4. Remove a task from the list")
        print("5. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_list()
            input("\nPress Enter to continue...")
        elif choice == "2":
            add_task()
            input("\nPress Enter to continue...")
        elif choice == "3":
            complete_task()
            input("\nPress Enter to continue...")
        elif choice == "4":
            remove_task()
            input("\nPress Enter to continue...")
        elif choice == "5":
            clear_console()
            break
        else:
            input("Invalid choice. Press Enter to continue...")

