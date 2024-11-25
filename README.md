# To-Do List Application

## Description

This To-Do List application allows you to manage your tasks with ease. It provides features to add, remove, mark as done, and clear all tasks. Each task is timestamped when added, and you can mark a task as completed with a checkmark (✔️).

The application is built using Python’s `Tkinter` library, providing a simple and intuitive graphical user interface (GUI).

## Features

- **Add Task**: Enter a task and click the "➕ Add Task" button to add it to the list.
- **Remove Task**: Select a task from the list and click "❌ Remove Selected" to remove it.
- **Mark as Done**: Select a task and click "✔️ Mark as Done" to mark it as completed.
- **Clear All Tasks**: Click the "🗑️ Clear All" button to remove all tasks from the list (with a confirmation prompt).
- **Timestamp**: Each task is timestamped with the date and time when it is added.

## Installation

To run this application, you need Python 3.x and the `Tkinter` library (usually pre-installed with Python).

### Steps to Install:

1. Install Python from [python.org](https://www.python.org/downloads/), if you haven't already.
2. Make sure you have `Tkinter` installed. If you are using Python 3.x, `Tkinter` is included by default.

### Running the Application:

1. Save the provided Python code in a file named `todo_list_app.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the following command:
5. The To-Do List application window will open, and you can start adding tasks.

## Code Explanation

- **GUI Components**:
- `tk.Label`: Displays labels such as the title and footer.
- `tk.Entry`: Input field for entering new tasks.
- `ttk.Button`: Buttons for actions like adding, removing, marking as done, and clearing tasks.
- `tk.Listbox`: Displays the list of tasks.
- `tk.Scrollbar`: Provides scrolling functionality for the task list.

- **Functions**:
- `add_task()`: Adds a new task with a timestamp to the list.
- `remove_task()`: Removes the selected task from the list.
- `mark_done()`: Marks the selected task as done by adding a checkmark in front of it.
- `clear_tasks()`: Clears all tasks after user confirmation.

## Dependencies

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Screenshots
![Screenshot 2024-11-25 210257](https://github.com/user-attachments/assets/14c66684-69e5-4de3-beb3-c4d87544e331)
![Screenshot 2024-11-25 210439](https://github.com/user-attachments/assets/0d401c17-11c3-40dd-b48d-2d16547ad0c5)
![Screenshot 2024-11-25 210453](https://github.com/user-attachments/assets/7bf8a63e-b84b-48f1-9ab6-4487490c17d0)
![Screenshot 2024-11-25 210512](https://github.com/user-attachments/assets/55c14763-9c0e-4c05-b900-8875f0c5e31a)
