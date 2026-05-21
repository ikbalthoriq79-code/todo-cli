"""Tests for todo-cli"""

import unittest
import os
import json
from todo_cli.storage import TodoStorage
from todo_cli.todo import TodoManager, Todo

class TestTodoStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_todos.json"
        self.storage = TodoStorage(self.test_file)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_create_file(self):
        self.assertTrue(os.path.exists(self.test_file))
    
    def test_save_and_load(self):
        todos = [{"id": 1, "title": "Test", "completed": False, "priority": "high", "created_at": "2026-05-21T00:00:00"}]
        self.storage.save(todos)
        loaded = self.storage.load()
        self.assertEqual(loaded, todos)

class TestTodoManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_todos.json"
        self.storage = TodoStorage(self.test_file)
        self.manager = TodoManager(self.storage)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_todo(self):
        todo = self.manager.add("Buy milk")
        self.assertEqual(todo.title, "Buy milk")
        self.assertFalse(todo.completed)
    
    def test_list_todos(self):
        self.manager.add("Task 1")
        self.manager.add("Task 2")
        todos = self.manager.list_all()
        self.assertEqual(len(todos), 2)
    
    def test_complete_todo(self):
        todo = self.manager.add("Task")
        completed = self.manager.complete(todo.id)
        self.assertTrue(completed.completed)
    
    def test_delete_todo(self):
        todo = self.manager.add("Task")
        deleted = self.manager.delete(todo.id)
        self.assertTrue(deleted)
        todos = self.manager.list_all()
        self.assertEqual(len(todos), 0)

if __name__ == "__main__":
    unittest.main()
