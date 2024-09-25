# Task Manager Bot

This is a Discord bot designed to help small teams manage tasks. It supports adding, deleting, listing, and updating tasks. All tasks are stored in an SQLite database. 

## Features

- **Add Task**: Add a task with a description.
- **Delete Task**: Delete a task by its ID.
- **List Tasks**: Show a list of all tasks, including their status (completed or not).
- **Change Task Status**: Mark a task as completed by its ID.

## Commands

| Command                       | Description                                      |
|--------------------------------|--------------------------------------------------|
| `!add_task <description>`      | Adds a task with the specified description.      |
| `!delete_task <task_id>`       | Deletes the task with the specified task ID.     |
| `!show_tasks`                  | Shows all tasks with their status.               |
| `!complete_task <task_id>`     | Marks the task with the specified task ID as completed. |


## Requirements

To run this project, you'll need the following:

- Python 3.8 or later
- SQLite
- Discord Bot and its token
  
## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/task_manager_bot.git
cd task_manager_bot
```

2. **Install pipenv (if you don't have it installed)**

```bash
pip install pipenv
```

3. **Create a virtual environment install dependencies**

```bash
pipenv install
```

4. **Activate the virtual environment**

```bash
pipenv shell
```

5. **Set up your bot token**

- Create a file named bot_token.py in the root directory and add your bot token as follows:

```python
token = "YOUR_DISCORD_BOT_TOKEN"
```

6. **Run the bot**

```bash
python main.py
```

- or

```bash
python3 main.py
```

7. **Test the bot commands**

- Open Discord and use the bot commands in any server/channel where the bot is present.

## Database

Tasks are stored in an SQLite database named tasks.db. A separate test database (test_tasks.db) is used for unit tests.

## Running Tests

Tests are located in the tests/ directory. Each test file tests different functionalities of the bot:

- **test_add_task.py**: Tests adding tasks.
- **test_delete_task.py**: Tests deleting tasks by the owner.
- **test_delete_task_unauthorized.py**: Tests deleting tasks by non-owner.
- **test_get_all_tasks**: Tests displaying tasks.
- **test_complete_task**: Tests completing tasks by the owner.

To run the tests, use the following command:

```bash
python run_tests.py
```

or 

```bash
python3 run_tests.py
```
