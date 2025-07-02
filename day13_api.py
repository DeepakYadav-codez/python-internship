from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Fetch tasks from the database
def fetch_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    tasks = [{"id": row[0], "title": row[1]} for row in rows]
    return tasks

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    print("✅ /api/tasks called")
    return jsonify(fetch_tasks())

if __name__ == "__main__":
    app.run(debug=True)
