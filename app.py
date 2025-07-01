from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# 🔧 Create the database/table if not exists
def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# 🏠 Home Page: Show tasks
@app.route("/")
def index():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

# ✅ START THE APP HERE
if __name__ == "__main__":
    init_db()
    print("✅ Flask app is starting...")
    app.run(debug=True)
