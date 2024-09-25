import os

print("Running test_add_task.py")
os.system("python3 tests/test_add_task.py")
print("----------------------------")

print("Running test_delete_task.py")
os.system("python3 tests/test_delete_task.py")
print("----------------------------")

print("Running test_delete_task.py")
os.system("python3 tests/test_delete_task_unauthorized.py")
print("----------------------------")

print("Running test_show_tasks.py")
os.system("python3 tests/test_get_all_tasks.py")
print("----------------------------")

print("Running test_complete_task.py")
os.system("python3 tests/test_complete_task.py")
print("----------------------------")