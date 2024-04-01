import json
import os

def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (optional): ")
    tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})

def remove_task(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter task index to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task index!")

def mark_completed(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter task index to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
    else:
        print("Invalid task index!")

def print_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        print("\nTODO LIST MENU:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks, filename)
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
