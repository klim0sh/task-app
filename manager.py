from models import Task
from database import get_connection
class TaskManager:
    def add(self, task):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, priority, deadline, done) VALUES (?, ?, ?, ?)",
            (task.name, task.priority, task.deadline, int(task.done))
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, priority, deadline, done FROM tasks")
        rows = cursor.fetchall()
        tasks = [Task(name, priority, deadline, bool(done))
                for name, priority, deadline, done in rows]
        conn.close()
        return tasks
    
    def show_tasks(self):
        tasks = self.get_all()
        if not tasks:
            print("No tasks yet")
            return
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")         

    def remove(self, index):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM tasks")
        rows = cursor.fetchall()
        task_id = rows[index][0]
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

    def toggle_done(self, index):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, done FROM tasks")
        rows = cursor.fetchall()
        task_id, done = rows[index]
        new_done = 0 if done else 1
        cursor.execute("UPDATE tasks SET done = ? WHERE id = ?",
    (new_done, task_id))
        conn.commit()
        conn.close()
