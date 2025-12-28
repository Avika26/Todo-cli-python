import json # save and load data in json format
import os #used to interact with operating system
from colorama import init, Fore, Style #print colored text 
# init - initializes colorama so colors work properly 
# fore - used for text color
# style - used for text styles
init(autoreset=True)

class Task:
    def __init__(self, title, description="", priority="Medium", completed=False):
        self.title=title
        self.description=description
        self.priority=priority
        self.completed=completed

    def __str__(self):
        status= Fore.GREEN + "✓" if self.completed else Fore.RED + "✗"
        dscrp = f" -{self.description}" if self.description else "" # checks if the task has a decription
        return f"[{status}] {self.title}{dscrp} (Priority: {self.priority})" #uses f string to combine variables into a single string for display
          

class TodoList:
    def __init__(self):
        self.tasks=[]

    def add_task(self,task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self,index):
        if 0<=index< len(self.tasks):
            self.tasks.pop(index)
            print("Task Removed.")
        else:
            print("Invalid Index!")

    def mark_completed(self,index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid index!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        # sort tasks - pending first, completed afterwards
        sorted_tasks= sorted(self.tasks, key=lambda t: t.completed)
        # sorted() - sorts the list
        # every task t is checked for its .completed attribute
        #flase<true so false ones(pending) will come before true(completed)
        print("\n--- Todo List ---")
        for i, task in enumerate(sorted_tasks):
            print(f"{i}. {task}")
        #enumerate gives both index and task object
        #print(..) calls the str() of task
        print("-------------------")

    def save_tasks(self, filename="data.json"):
        data =[
            {
                "Title": t.title,
                "Description": t.description,
                "Priority": t.priority,
                "Completed": t.completed
            }
            for t in self.tasks
        ]
        #converts tasks to dictionaries 
        with open(filename,"w") as f:
            json.dump(data, f, indent=4)
        #json.dump() converts data to json format and saves it
        #indent=4 4 spaces each level

    def load_tasks(self, filename="data.json"):
        if not os.path.exists(filename):
            return
        if os.stat(filename).st_size == 0:  # check if file is empty
            return
        with open(filename,"r") as f:
            data = json.load(f)
            self.tasks = [
            Task(
                d["Title"],
                d.get("Description",""),
                d.get("Priority","Medium"),
                d.get("Completed",False)
            )
            for d in data
        ]

        









