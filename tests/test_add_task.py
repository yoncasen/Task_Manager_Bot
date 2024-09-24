import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import init_db, close_db, add_task_to_db, get_all_tasks


TEST_DB_FILE = 'test_tasks.db'

def reset_db():
    
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)

def test_add_task():
    
    reset_db()
    init_db(TEST_DB_FILE)

    author = "Test User"
    task_description = "Test task"

    add_task_to_db(author, task_description)

    tasks = get_all_tasks()

    if len(tasks) == 0:
        print("Test failed: No tasks were added.")
    elif tasks[0][1] != author:
        print(f"Test failed: Expected author '{author}', got '{tasks[0][2]}'.")
    elif tasks[0][2] != task_description:
        print(f"Test failed: Expected task description '{task_description}', got '{tasks[0][2]}'.")
    else:
        print(f"Test passed: Task {task_description} added successfully by {author}.")

    close_db()

if __name__ == "__main__":
    test_add_task()
