import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import init_db, close_db, add_task_to_db, get_all_tasks, complete_task_db

TEST_DB_FILE = 'test_tasks.db'

def reset_db():
    
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)

def test_complete_task():
    
    reset_db()
    init_db(TEST_DB_FILE)
    
    tasks = get_all_tasks()
    if len(tasks) > 0:
        print(f"Test setup failed: {len(tasks)} tasks found before the test started.")
        return
  
    task_description = "Test task to complete"
    author = "test_author"
    add_task_to_db(author, task_description)

    tasks = get_all_tasks()
    if len(tasks) == 0:
        print("Test setup failed: Task was not added.")
        return
    
    task_id = tasks[0][0]

    completed = complete_task_db(task_id, author)
    
    if not completed:
        print(f"Test failed: Task with ID {task_id} could not be marked as completed.")
    else:
        tasks = get_all_tasks()
        if tasks[0][3] != 1:  
            print(f"Test failed: Task with ID {task_id} was not marked as completed.")
        else:
            print(f"Test passed: Task {task_id} was successfully marked as completed.")
    
    close_db()

if __name__ == "__main__":
    test_complete_task()
