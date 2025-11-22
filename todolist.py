# Simple To-Do List Application in Python

todo_list = []

def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print(f"Task added: {task}")

    elif choice == "2":
        print("\nYour To-Do List:")
        if len(todo_list) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\nWhich task do you want to remove?")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
        
        num = int(input("Enter task number: "))
        
        if 1 <= num <= len(todo_list):
            removed_task = todo_list.pop(num - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number!")

    elif choice == "4":
        print("Exiting the To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
