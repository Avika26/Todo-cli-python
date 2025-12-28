from mytodo import TodoList, Task  # Make sure your file is named mytodo.py

# Create TodoList instance
todo_list = TodoList()
todo_list.load_tasks()  # Load saved tasks if data.json exists

def show_menu():
    print("\n--- Todo List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task Completed")
    print("4. List Tasks")
    print("5. Save & Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter description (optional): ")
        priority = input("Enter priority (High/Medium/Low, default Medium): ") or "Medium"
        task = Task(title, description, priority)
        todo_list.add_task(task)

    elif choice == "2":
        todo_list.list_tasks()
        index = input("Enter task index to remove: ")
        if index.isdigit():
            todo_list.remove_task(int(index))
        else:
            print("Invalid input!")

    elif choice == "3":
        todo_list.list_tasks()
        index = input("Enter task index to mark as completed: ")
        if index.isdigit():
            todo_list.mark_completed(int(index))
        else:
            print("Invalid input!")

    elif choice == "4":
        todo_list.list_tasks()

    elif choice == "5":
        todo_list.save_tasks()
        print("Tasks saved. Exiting...")
        break

    else:
        print("Invalid choice! Enter a number between 1 and 5.")
