# build basic todo app
# with a list of tasks

Todo_list = {}
task_id = 1
def add_task(task):
    global task_id
    Todo_list[task_id] = task
    print(f"Task '{task}' added to the list with ID {task_id}.")
    task_id += 1
def remove_task(task):
   try:
        task_id = int(task)
        if task_id in Todo_list:
            removed_task = Todo_list.pop(task_id)
            print(f"Task '{removed_task}' with ID {task_id} removed from the list.")
        else:
            print(f"Task ID {task_id} not found in the list.")
   except ValueError:
        print("Invalid task ID. Please enter a valid number.")
def view_tasks():
    if  Todo_list:
        print("Todo List:")
        for task_id, task in Todo_list.items():
            print(f"{task_id}. {task}")
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
            task = input("Enter the task ID to remove: ")
            remove_task(task_id)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting the Todo App.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()