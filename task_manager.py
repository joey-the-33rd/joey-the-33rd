# Fully functional task manager with date, time, and alerts.

import tkinter as tk
from tkinter import messagebox
import datetime
import threading
import time

class Task:
    def __init__(self, name, date, time, alert_time):
        self.name = name
        self.date = date
        self.time = time
        self.alert_time = alert_time

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.root = tk.Tk()
        self.root.title("Task Manager")
        self.create_widgets()

    def create_widgets(self):
        self.task_name_label = tk.Label(self.root, text="Task Name:")
        self.task_name_label.grid(row=0, column=0)
        self.task_name_entry = tk.Entry(self.root)
        self.task_name_entry.grid(row=0, column=1)

        self.task_date_label = tk.Label(self.root, text="Task Date (YYYY-MM-DD):")
        self.task_date_label.grid(row=1, column=0)
        self.task_date_entry = tk.Entry(self.root)
        self.task_date_entry.grid(row=1, column=1)

        self.task_time_label = tk.Label(self.root, text="Task Time (HH:MM):")
        self.task_time_label.grid(row=2, column=0)
        self.task_time_entry = tk.Entry(self.root)
        self.task_time_entry.grid(row=2, column=1)

        self.alert_time_label = tk.Label(self.root, text="Alert Time (YYYY-MM-DD HH:MM):")
        self.alert_time_label.grid(row=3, column=0)
        self.alert_time_entry = tk.Entry(self.root)
        self.alert_time_entry.grid(row=3, column=1)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=4, column=0)

        self.view_tasks_button = tk.Button(self.root, text="View Tasks", command=self.view_tasks)
        self.view_tasks_button.grid(row=4, column=1)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=5, column=0)

        self.schedule_alerts_button = tk.Button(self.root, text="Schedule Alerts", command=self.schedule_alerts)
        self.schedule_alerts_button.grid(row=5, column=1)

        self.tasks_text = tk.Text(self.root)
        self.tasks_text.grid(row=6, column=0, columnspan=2)

    def add_task(self):
        name = self.task_name_entry.get()
        date = self.task_date_entry.get()
        time = self.task_time_entry.get()
        alert_time = self.alert_time_entry.get()
        task = Task(name, date, time, alert_time)
        self.tasks.append(task)
        self.tasks_text.insert(tk.END, f"Task '{name}' added successfully.\n")

    def view_tasks(self):
        self.tasks_text.delete(1.0, tk.END)
        for task in self.tasks:
            self.tasks_text.insert(tk.END, f"Task: {task.name}, Date: {task.date}, Time: {task.time}, Alert Time: {task.alert_time}\n")

    def delete_task(self):
        task_name = self.task_name_entry.get()
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                self.tasks_text.insert(tk.END, f"Task '{task_name}' deleted successfully.\n")
                return
        self.tasks_text.insert(tk.END, f"Task '{task_name}' not found.\n")

    def schedule_alerts(self):
        for task in self.tasks:
            alert_time = datetime.datetime.strptime(task.alert_time, "%Y-%m-%d %H:%M")
            current_time = datetime.datetime.now()
            time_diff = (alert_time - current_time).total_seconds()
            if time_diff > 0:
                threading.Timer(time_diff, self.send_alert, args=(task,)).start()
            else:
                self.tasks_text.insert(tk.END, f"Alert time for task '{task.name}' has already passed.\n")

    def send_alert(self, task):
        messagebox.showinfo("Alert", f"Task '{task.name}' is due on {task.date} at {task.time}.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()