import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import init_db, close_db, add_task_to_db, get_all_tasks

TEST_DB_FILE = 'test_tasks.db'

def reset_db():
    
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)

def test_get_all_tasks():
    
    reset_db()
    init_db(TEST_DB_FILE)
    
    tasks = get_all_tasks()
    if len(tasks) > 0:
        print(f"Test setup failed: {len(tasks)} tasks found before the test started.")
        return
    
    task1_description = "Test task 1"
    task2_description = "Test task 2"
    add_task_to_db("Test User 1", task1_description)
    add_task_to_db("Test User 2", task2_description)
    
    tasks = get_all_tasks()
    
    if len(tasks) != 2:
        print(f"Test failed: Expected 2 tasks, but got {len(tasks)}.")
    else:
        print("Test passed: Correct number of tasks retrieved.")
    
    if tasks[0][2] != task1_description:
        print(f"Test failed: First task description mismatch. Expected '{task1_description}', got '{tasks[0][1]}'.")
    elif tasks[1][2] != task2_description:
        print(f"Test failed: Second task description mismatch. Expected '{task2_description}', got '{tasks[1][1]}'.")
    else:
        print("Test passed: Task descriptions match correctly.")
    
    close_db()

if __name__ == "__main__":
    test_get_all_tasks()
