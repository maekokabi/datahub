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

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task) for task in data["tasks"]]
        except FileNotFoundError:
            raise ValueError("No saved file found.")
        except json.JSONDecodeError:
            raise ValueError("Json file is corrupted.")
        except KeyError:
            raise ValueError("Json structure missing.")

    def display_tasks(self):
        if not self.tasks:
            raise ValueError("No task entries.")
        return self.tasks

    def add_task(self, id:int, task, description="", deadline="No Deadline", done="Not done"):
        task_object = Task(id, task, description, deadline, done)

        if any(task.id == task_object.id for task in self.tasks):
            raise ValueError("This id already exists.")
        else:
            task_object.validate_all()
            self.tasks.append(task_object)
            self.save_to_file()

    def delete_task_by_id(self, task_id):
        if not any(t.id == task_id for t in self.tasks):
            raise ValueError("No task by this id.")
        else:
            matched_task = next((t for t in self.tasks if t.id == task_id), None)
            self.tasks.remove(matched_task)
            self.save_to_file()

    def search_by_attribute(self, attr_name, value):
        results = [e for e in self.tasks if getattr(e, attr_name) == value]
        if not results:
            raise ValueError(f"No entries found for {attr_name} = {value}")
        return results

    def all_done_tasks(self):
        results = [t for t in self.tasks if t.status == "Done"]
        if not results:
            raise ValueError("No completed task.")
        return results

    def all_not_done_tasks(self):
        results = [t for t in self.tasks if t.status == "Not done"]
        if not results:
            raise ValueError("All tasks are completed.")
        return results 

    def mark_task_done(self, task_id):
        matched_task = next((t for t in self.tasks if t.id == task_id), None)
        if not matched_task:
            raise ValueError("Task doesn't exist.")
        else:
            matched_task.mark_done()
            self.save_to_file()

    def mark_task_undone(self, task_id):
        matched_task = next((t for t in self.tasks if t.id == task_id), None)
        if not matched_task:
            raise ValueError("Task doesn't exist.")
        else:
            matched_task.mark_undone()
            self.save_to_file()

class Task:
    def __init__(self, id:int, task, description=None, deadline=None, status="Not done"):
        self.id = id
        self.task = task
        self.description = "" if description is None else description
        self.deadline = None if deadline in (None, "", "No Deadline") else deadline
        self.status = "Not done" if status is None else status

    def __repr__(self):
        return f"ID: {self.id}, Task: {self.task}, Description: {self.description}, Deadline: {self.deadline}, Status: {self.status}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "description": self.description,
            "deadline": self.deadline,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["task"],
            data["description"],
            data["deadline"],
            data["status"]
        )
    
    def validate_all(self):
        errors = []

        for validator in [
            self.validate_id,
            self.validate_task,
            self.validate_description,
            self.validate_deadline,
            self.validate_status,
        ]:
            result = validator()
            if result:
                errors.append(result)

        return errors


    def validate_id(self):
        if not isinstance(self.id, int):
            return "ID must be a number."
        return None
    
    def validate_task(self):
        if not isinstance(self.task, str) or not self.task.strip():
            return "Task must be a non-empty string."
        return None
    
    def validate_description(self):
        if self.description is None:
            self.description = ""
            return None

        if not isinstance(self.description, str):
            return "Description must be a string."

        return None
    
    def validate_deadline(self):
        if self.deadline in (None, ""):
            return None

        if not isinstance(self.deadline, str):
            return "Deadline must be a string in YYYY-MM-DD format."

        try:
            datetime.strptime(self.deadline, "%Y-%m-%d")
        except ValueError:
            return "Date must be in YYYY-MM-DD format."

        return None
    
    def validate_status(self):
        if self.status is None:
            self.status = "Not done"
            return None

        if not isinstance(self.status, str):
            return "Status must be 'Done' or 'Not done'."

        normalized = self.status.strip().lower()

        if normalized == "done":
            self.status = "Done"
            return None

        if normalized in ("not done", "notdone"):
            self.status = "Not done"
            return None

        return "Status must be 'Done' or 'Not done'."


    
    def mark_done(self):
        self.status = "Done"

    def mark_undone(self):
        if self.status == "Not done":
            raise ValueError("Task is already marked as undone.")
        else:
            self.status = "Not done"

    