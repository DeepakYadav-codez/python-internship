import os

tasks = []

def load_tasks_from_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                task_name, status = line.strip().split(" - ")
                tasks.append({"task": task_name, "status": status})
        print(f"📂 Loaded tasks from {filename}")
    except FileNotFoundError:
        print(f"⚠️ {filename} not found. Starting with an empty task list.")
    except Exception as e:
        print(f"❌ Error while reading file: {e}")

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
        print("\n📋 Current Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - {task['status']}")

def save_tasks_to_file(filename):
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(f"{task['task']} - {task['status']}\n")
        print(f"\n✅ Tasks saved to {filename}")
    except Exception as e:
        print(f"❌ Error while saving file: {e}")

# --------- Run App ---------

filename = "tasks.txt"

load_tasks_from_file(filename)

add_task("Learn Python")
remove_task("Do homework")
show_tasks()

save_tasks_to_file(filename)
