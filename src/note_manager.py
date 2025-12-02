from datetime import datetime
import json

class NoteManager:
    def __init__(self):
        self.notes = []

    def save_to_file(self, filename="notes.json"):
        data = {
            "Notes" : [note.to_dict() for note in self.notes]
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved.")

    def load_from_file(self, filename="notes.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.notes = [Note.from_dict(note) for note in data["Notes"]]
        except FileNotFoundError:
            print("No saved file found.")
        except json.JSONDecodeError:
            print("Json file is corrupted.")
        except KeyError:
            print("Json structure missing.")
    
    def display_all_notes(self):
        if self.notes == []:
            print("No note entries yet.")
        else:
            for note in self.notes:
                print(note)

    def add_note(self, note_object):
        if any(n.id == note_object.id for n in self.notes):
            print("This id already exists.")
        else:
            try:
                note_object.validate_all()
                self.notes.append(note_object)
                print("Note added.")
            except ValueError as e:
                print({e})

    def delete_note(self, note_object):
        if not any (n == note_object for n in self.notes):
            print("This note entry does not exist.")
        else:
            try:
                self.notes.remove(note_object)
                print("Note removed.")
            except ValueError as e:
                print(f"{e}")

    def delete_note_by_id(self, note_id):
        if not any(n.id == note_id for n in self.notes):
            print("No note entry with this id.")
        else:
            try:
                matched_note = next((n for n in self.notes if n.id == note_id), None)
                self.notes.remove(matched_note)
                print("Note entry removed.")
            except ValueError as e:
                print(f"{e}")

class Note:
    def __init__(self, id:int, category, date, topic="Nameless.", note=""):
        self.id = id
        self.category = category
        self.date = date
        self.topic = topic
        self.note = note     

    def __repr__(self):
        return f"ID: {self.id}, Category: {self.category}, Date: {self.date}, Topic: {self.topic}, Note: {self.note}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "date": self.date,
            "topic": self.topic,
            "note": self.note,        
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["category"],
            data["date"],
            data["topic"],
            data["note"]
        )
    
    def validate_all(self):
        errors = []

        for validator in [
            self.validate_category,
            self.validate_date,
            self.validate_id
        ]:
            result = validator()
            if result is not None:
                errors.append(result)
            
        if errors:
            message = " | ".join(errors)
            raise ValueError(f"Invalid note entry: {message}")


    def validate_id(self):
        if not isinstance(self.id, int):
            return "ID must be a number"
        return None

    def validate_category(self):
        if not self.category.strip():
            return "Topic must be a non-empty string."
        return None

    def validate_date(self):
        try:
            datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            return "Date must be in YYYY-MM-DD format."
        return None