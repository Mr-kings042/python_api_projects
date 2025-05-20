# build basic todo app
# with a list of tasks

Todo_list = []
def add_task(task):
    Todo_list.append(task)
    print(f"Task '{task}' added to the list.")
def remove_task(task):
    if task in Todo_list:
        Todo_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")
def view_tasks():
    if Todo_list:
        print("Todo List:")
        for i, task in enumerate(Todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("Todo list is empty.")
def main():
    while True:
        print("\nTodo App Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting the Todo App.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()