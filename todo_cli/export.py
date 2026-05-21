"""Export/Import functionality for todos"""

import csv
import json
from typing import List, Dict

class TodoExporter:
    @staticmethod
    def to_csv(todos: List[Dict], filepath: str):
        """Export todos to CSV"""
        if not todos:
            return
        
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'completed', 'priority', 'category', 'due_date', 'created_at'])
            writer.writeheader()
            writer.writerows(todos)
    
    @staticmethod
    def to_json(todos: List[Dict], filepath: str):
        """Export todos to JSON"""
        with open(filepath, 'w') as f:
            json.dump(todos, f, indent=2)
    
    @staticmethod
    def from_csv(filepath: str) -> List[Dict]:
        """Import todos from CSV"""
        todos = []
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['completed'] = row['completed'].lower() == 'true'
                todos.append(row)
        return todos
    
    @staticmethod
    def from_json(filepath: str) -> List[Dict]:
        """Import todos from JSON"""
        with open(filepath, 'r') as f:
            return json.load(f)
