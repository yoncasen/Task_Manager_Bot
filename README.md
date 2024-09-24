# Task Manager Bot

This is a Discord bot designed to help small teams manage tasks. It supports adding, deleting, listing, and updating tasks. All tasks are stored in an SQLite database. 

## Features

- **Add Task**: Add a task with a description.
- **Delete Task**: Delete a task by its ID.
- **Show Tasks**: Show a list of all tasks, including their status (completed or not).
- **Complete Task**: Mark a task as completed by its ID.

## Commands

| Command                       | Description                                      |
|--------------------------------|--------------------------------------------------|
| `!add_task <description>`      | Adds a task with the specified description.      |
| `!delete_task <task_id>`       | Deletes the task with the specified task ID.     |
| `!show_tasks`                  | Shows all tasks with their status.               |
| `!complete_task <task_id>`     | Marks the task with the specified task ID as completed. |


