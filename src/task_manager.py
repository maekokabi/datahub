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

    def add_task(self, id:int, task, description="", deadline="No Deadline", done="Not done"):
        task_object = Task(id, task, description, deadline, done)

        if any(task.id == task_object.id for task in self.tasks):
            print("This id already exists.")
        else:
            try:
                task_object.validate_all()
                self.tasks.append(task_object)
                print("Task added.")
                self.save_to_file()
            except ValueError as e:
                print(f"{e}")

    def delete_task(self, id:int, task, description="", deadline="No Deadline", done="Not done"):
        task_object = Task(id, task, description, deadline, done)

        if not any(task_object == t for t in self.tasks):
            print("Task not found.")
        else:
            try:
                self.tasks.remove(task_object)
                print("Task removed.")
                self.save_to_file()
            except ValueError as e:
                print(f"{e}")

    def delete_task_by_id(self, task_id):
        if not any(t.id == task_id for t in self.tasks):
            print("No task by this id.")
        else:
            try:
                matched_task = next((t for t in self.tasks if t.id == task_id), None)
                self.tasks.remove(matched_task)
                print("Task removed.")
            except ValueError as e:
                print(f"{e}")

    def search_by_task(self, task):
        if not any(t.task == task for t in self.tasks):
            print("No exisiting task entries with this name.")
        else:
            try:
                [print(t) for t in self.tasks if t.task == task]
            except ValueError as e:
                print(f"{e}")

    def search_by_deadline(self, deadline):
        if not any(t.deadline == deadline for t in self.tasks):
            print("No task entries with this deadline.")
        else:
            try:
                [print(t) for t in self.tasks if t.deadline == deadline]
            except ValueError as e:
                print(f"{e}")

    def all_done_tasks(self):
        if not any(t.status == "Done" for t in self.tasks):
            print("No finished tasks.")
        else:
            try:
                print("All finished tasks: ")
                [print(t) for t in self.tasks if t.status == "Done"]
            except ValueError as e:
                print(f"{e}")

    def all_not_done_tasks(self):
        if not any(t.status == "Not done" for t in self.tasks):
            print("All tasks are completed.")
        else:
            try:
                print("All unfinished tasks: ")
                [print(t) for t in self.tasks if t.status == "Not done"]
            except ValueError as e:
                print(f"{e}")

    def mark_task_done(self, task_id):
        if not any(t.id == task_id for t in self.tasks):
            print("Task doesn't exist.")
        else:
            try:
                matched_task = next((t for t in self.tasks if t.id == task_id), None)
                matched_task.mark_done()
                print("Task is completed.")
                self.save_to_file()
            except ValueError as e:
                print(f"{e}")

    def mark_task_undone(self, task_id):
        if not any(t.id == task_id for t in self.tasks):
            print("Task doesn't exist.")
        else:
            try:
                matched_task = next((t for t in self.tasks if t.id == task_id), None)
                matched_task.mark_undone()
                print("Task is marked undone.")
                self.save_to_file()
            except ValueError as e:
                print(f"{e}")

class Task:
    def __init__(self, id:int, task, description="", deadline="No Deadline", status="Not done"):
        self.id = id
        self.task = task
        self.description = description
        self.deadline = deadline
        self.status = status
        # categorize 

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
    
    def mark_done(self):
        self.status = "Done"
        print("Marked as done.")

    def mark_undone(self):
        if self.status == "Not done":
            print("Task is already marked as undone.")
        else:
            try:
                self.status = "Not done"
                print("Marked as undone.")
            except ValueError as e:
                print(f"{e}")
    