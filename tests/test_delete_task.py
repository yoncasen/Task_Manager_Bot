import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import init_db, close_db, add_task_to_db,delete_task_from_db, get_all_tasks

TEST_DB_FILE = 'test_tasks.db'

def reset_db():
    
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)

def test_delete_task():
    
    reset_db()
    init_db(TEST_DB_FILE)

    author = "Test User"
    task_description = "Test task"
    add_task_to_db(author, task_description)
    tasks = get_all_tasks()
    task_id = tasks[0][0]

    delete_task_from_db(task_id,author)

    tasks = get_all_tasks()
    
    print("Deleting a task by the owner is being tested.")
    if len(tasks) == 0:
        print(f"Test passed: the '{task_description}' task successfully deleted by the owner {author}.")
    else:
        print("Test failed: the task can not be deleted.")

    close_db()


if __name__ == "__main__":
    test_delete_task()

