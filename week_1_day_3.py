tasks = []

def add_task(task_name):
    tasks.append({"task": task_name, "status": "pending"})
    print(f"Task '{task_name}' added.")

def remove_task(task_name):
    for task in tasks:
        if task["task"] == task_name:
            tasks.remove(task)
            print(f"Task '{task_name}' removed.")
            return
    print(f"Task '{task_name}' not found.")

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - {task['status']}")

def save_tasks_to_file(filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']} - {task['status']}\n")
    print(f"\n✅ Tasks saved to {filename}")

# --------- Sample Program Execution ---------

add_task("Buy groceries")
add_task("Do homework")

print("\n📋 Current Tasks:")
show_tasks()

remove_task("Buy groceries")

print("\n📋 Updated Tasks:")
show_tasks()

# Save all tasks to file
save_tasks_to_file("tasks.txt")
