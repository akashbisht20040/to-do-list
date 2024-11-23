import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_listbox.insert(tk.END, f"{task} (Added on: {timestamp})")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove the selected task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Function to clear all tasks
def clear_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# Function to mark a task as done
def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✔️ {task}")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Initialize the main application window
app = tk.Tk()
app.title("To-Do List")
app.geometry("500x600")
app.resizable(False, False)
app.configure(bg="#e6f7ff")

# Title Label
title_label = tk.Label(
    app,
    text="📝 To-Do List Application",
    font=("Helvetica", 24, "bold"),
    bg="#e6f7ff",
    fg="#007acc"
)
title_label.pack(pady=20)

# Entry for adding tasks
task_frame = tk.Frame(app, bg="#e6f7ff")
task_frame.pack(pady=10)

task_entry = ttk.Entry(task_frame, width=30, font=("Helvetica", 14))
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = ttk.Button(task_frame, text="➕ Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

# Listbox to display tasks with scrollbar
listbox_frame = tk.Frame(app, bg="#e6f7ff")
listbox_frame.pack(pady=10)

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(
    listbox_frame,
    width=50,
    height=15,
    font=("Helvetica", 12),
    bg="#f9fcff",
    fg="#333",
    bd=1,
    relief="solid",
    highlightthickness=1,
    highlightbackground="#007acc",
    yscrollcommand=scrollbar.set,
    selectbackground="#b3d9ff",
    selectforeground="#000"
)
task_listbox.pack(side=tk.LEFT, padx=5)
scrollbar.config(command=task_listbox.yview)

# Buttons for actions
button_frame = tk.Frame(app, bg="#e6f7ff")
button_frame.pack(pady=20)

remove_button = ttk.Button(button_frame, text="❌ Remove Selected", width=20, command=remove_task)
remove_button.grid(row=0, column=0, padx=5, pady=5)

done_button = ttk.Button(button_frame, text="✔️ Mark as Done", width=20, command=mark_done)
done_button.grid(row=0, column=1, padx=5, pady=5)

clear_button = ttk.Button(button_frame, text="🗑️ Clear All", width=20, command=clear_tasks)
clear_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

# Footer Label
footer_label = tk.Label(
    app,
    text="Created with ❤️ by [Your Name]",
    font=("Helvetica", 10, "italic"),
    bg="#e6f7ff",
    fg="#666"
)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the application
app.mainloop()