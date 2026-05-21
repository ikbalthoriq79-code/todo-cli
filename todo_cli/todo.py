"""Todo class and logic"""

from datetime import datetime
from typing import List, Dict, Optional

class Todo:
    def __init__(self, id: int, title: str, completed: bool = False, priority: str = "medium", due_date: Optional[str] = None, category: str = "general"):
        self.id = id
        self.title = title
        self.completed = completed
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "priority": self.priority,
            "due_date": self.due_date,
            "category": self.category,
            "created_at": self.created_at
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Todo':
        todo = Todo(data["id"], data["title"], data["completed"], data.get("priority", "medium"), data.get("due_date"), data.get("category", "general"))
        todo.created_at = data.get("created_at", todo.created_at)
        return todo

class TodoManager:
    def __init__(self, storage):
        self.storage = storage
    
    def add(self, title: str, priority: str = "medium") -> Todo:
        """Add new todo"""
        todos = self.storage.load()
        new_id = max([t["id"] for t in todos], default=0) + 1
        todo = Todo(new_id, title, priority=priority)
        todos.append(todo.to_dict())
        self.storage.save(todos)
        return todo
    
    def list_all(self) -> List[Todo]:
        """List all todos"""
        todos = self.storage.load()
        return [Todo.from_dict(t) for t in todos]
    
    def complete(self, todo_id: int) -> Optional[Todo]:
        """Mark todo as complete"""
        todos = self.storage.load()
        for todo in todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                self.storage.save(todos)
                return Todo.from_dict(todo)
        return None
    
    def delete(self, todo_id: int) -> bool:
        """Delete todo"""
        todos = self.storage.load()
        filtered = [t for t in todos if t["id"] != todo_id]
        if len(filtered) < len(todos):
            self.storage.save(filtered)
            return True
        return False
    
    def search(self, query: str) -> List[Todo]:
        """Search todos by title or category"""
        todos = self.storage.load()
        results = []
        query_lower = query.lower()
        for todo in todos:
            if query_lower in todo["title"].lower() or query_lower in todo.get("category", "").lower():
                results.append(Todo.from_dict(todo))
        return results
    
    def filter_by_category(self, category: str) -> List[Todo]:
        """Filter todos by category"""
        todos = self.storage.load()
        return [Todo.from_dict(t) for t in todos if t.get("category", "general") == category]
