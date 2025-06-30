import sqlite3

# Connect to a local SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create a table for tasks
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'pending'
)
""")

# Insert 3 sample tasks
cursor.execute("INSERT INTO tasks (title, status) VALUES (?, ?)", ("Buy groceries", "pending"))
cursor.execute("INSERT INTO tasks (title, status) VALUES (?, ?)", ("Do homework", "completed"))
cursor.execute("INSERT INTO tasks (title, status) VALUES (?, ?)", ("Go for walk", "pending"))

# Save changes
conn.commit()

# Show all tasks (optional)
cursor.execute("SELECT * FROM tasks")
tasks = cursor.fetchall()

print("\n📋 Tasks in Database:")
for task in tasks:
    print(task)

# Close the connection
conn.close()
