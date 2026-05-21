"""Storage handler for todos"""

import json
import os
from pathlib import Path
from typing import List, Dict

class TodoStorage:
    def __init__(self, filepath: str = "todos.json"):
        self.filepath = filepath
        self.ensure_file()
    
    def ensure_file(self):
        """Create todos.json if not exists"""
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)
    
    def load(self) -> List[Dict]:
        """Load todos from file"""
        with open(self.filepath, 'r') as f:
            return json.load(f)
    
    def save(self, todos: List[Dict]):
        """Save todos to file"""
        with open(self.filepath, 'w') as f:
            json.dump(todos, f, indent=2)
