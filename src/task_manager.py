from datetime import datetime
import json

class TaskManager:
    def __init__(self):
        self.tasks = []

    def save_to_file(self, filename="tasks.json"):
        data = {
            "tasks": [task.to_dict() for task in self.tasks]
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved.")

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task) for task in data["tasks"]]
        except FileNotFoundError:
            print("No saved file found.")
        except json.JSONDecodeError:
            print("Json file is corrupted.")
        except KeyError:
            print("Json structure missing.")

    def display_tasks(self):
        if self.tasks == []:
            print("No task entries.")
        else:
            for task in self.tasks:
                print(task)

    def add_task(self, task_object):
        if any(task.id == task_object.id for task in self.tasks):
            print("This id already exists.")
        else:
            try:
                task_object.validate_all()
                self.tasks.append(task_object)
                print("Task added.")
            except ValueError as e:
                print(f"{e}")

class Task:
    def __init__(self, id:int, task, description="", deadline="No Deadline", done=False):
        self.id = id
        self.task = task
        self.description = description
        self.deadline = deadline
        self.done = done
        # categorize 

    def __repr__(self):
        return f"ID: {self.id}, Task: {self.task}, Description: {self.description}, Deadline: {self.deadline}, Status: {self.done}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "description": self.description,
            "deadline": self.deadline,
            "done": self.done
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["task"],
            data["description"],
            data["deadline"],
            data["done"]
        )
    
    def validate_all(self):
        errors = []

        for validator in [
            self.validate_id,
            self.validate_task,
            self.validate_deadline,
        ]:
            result = validator()
            if result is not None:
                errors.append(result)
            
        if errors:
            message= " | ".join(errors)
            raise ValueError(f"Invalid Entry: {message}")

    def validate_id(self):
        if not isinstance(self.id, int):
            return "ID must be a number."
        return None
    
    def validate_task(self):
        if not isinstance(self.task, str) or not self.task.strip():
            return "Task must be a non-empty string."
        return None
    
    def validate_deadline(self):
        try:
            datetime.strptime(self.deadline, "%Y-%m-%d")
        except ValueError:
            return "Date must be in YYYY-MM-DD format."
        return None
    