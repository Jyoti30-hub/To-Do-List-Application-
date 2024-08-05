import os

tasks = []

def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks()

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    view_tasks()
    task_no = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no] = input("Enter the new task: ")
        save_tasks()
    else:
        print("Invalid task number")

def delete_task():
    view_tasks()
    task_no = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)
        save_tasks()
    else:
        print("Invalid task number")

def main():
    load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if _name_ == "_main_":
    main()