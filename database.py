import sqlite3
import os

db_connection = None

# def reset_db(db_path):
#     if os.path.exists(db_path):
#         os.remove(db_path)

def init_db(db_path):
    global db_connection
    db_connection = sqlite3.connect(db_path) 
    cursor = db_connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            task TEXT NOT NULL,
            is_completed BOOLEAN DEFAULT 0
        )
    ''')
    db_connection.commit()
    print("Database connection is initialized.")


def close_db():
    global db_connection
    if db_connection:
        db_connection.close()
        print("Database connection is closed.")

def add_task_to_db(author,task):
    cursor = db_connection.cursor()
    cursor.execute('INSERT INTO tasks (author, task) VALUES (?, ?)', (author, task))
    db_connection.commit()

def get_all_tasks():
    cursor = db_connection.cursor()
    cursor.execute('SELECT id, author, task, is_completed FROM tasks')
    tasks = cursor.fetchall()
    return tasks

def delete_task_from_db(task_id,author):
    cursor = db_connection.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ? AND author = ?', (task_id, author))
    db_connection.commit()

    if cursor.rowcount > 0:
        #reassign_ids()
        return True
    else:
        return False
        
def complete_task_db(task_id,author):
    cursor = db_connection.cursor()
    cursor.execute('UPDATE tasks SET is_completed = 1 WHERE id = ? AND author = ?', (task_id, author))
    db_connection.commit()

    if cursor.rowcount > 0:
        return True
    else:
        return False
            

# def reassign_ids():
#     cursor = db_connection.cursor()
#     cursor.execute('SELECT * FROM tasks ORDER BY id')
#     tasks = cursor.fetchall()

#     for new_id, task in enumerate(tasks, start=1):
#         cursor.execute('UPDATE tasks SET id = ? WHERE id = ?', (new_id, task[0]))
  