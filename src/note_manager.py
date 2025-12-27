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

    def load_from_file(self, filename="notes.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.notes = [Note.from_dict(note) for note in data["Notes"]]
        except FileNotFoundError:
            raise ValueError("No saved file found.")
        except json.JSONDecodeError:
            raise ValueError("Json file is corrupted.")
        except KeyError:
            raise ValueError("Json structure missing.")
    
    def display_all_notes(self):
        if not self.notes:
            raise ValueError("No note entries.")
        return self.notes

    def add_note(self, id:int, category, date, topic="Nameless.", note=""):
        note_object = Note(id, category, date, topic, note)
        if any(n.id == note_object.id for n in self.notes):
            raise ValueError("This id already exists.")
        else:
            note_object.validate_all()
            self.notes.append(note_object)
            self.save_to_file()

    def delete_note_by_id(self, note_id):
        if not any(n.id == note_id for n in self.notes):
            raise ValueError("No note entry with this id.")
        else:
            matched_note = next((n for n in self.notes if n.id == note_id), None)
            self.notes.remove(matched_note)
            self.save_to_file()

    def search_by_attribute(self, attr_name, value):
        results = [e for e in self.notes if getattr(e, attr_name) == value]
        if not results:
            raise ValueError(f"No entries found for {attr_name} = {value}")
        return results

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