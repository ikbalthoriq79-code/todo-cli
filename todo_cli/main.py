"""Main CLI interface"""

import sys
from todo_cli.storage import TodoStorage
from todo_cli.todo import TodoManager

def main():
    storage = TodoStorage("todos.json")
    manager = TodoManager(storage)
    
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Title required")
            return
        title = " ".join(sys.argv[2:])
        todo = manager.add(title)
        print(f"✓ Added: {todo.title} (ID: {todo.id})")
    
    elif command == "list":
        todos = manager.list_all()
        if not todos:
            print("No todos yet")
            return
        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"{status} [{todo.id}] {todo.title} ({todo.priority})")
    
    elif command == "complete":
        if len(sys.argv) < 3:
            print("Error: Todo ID required")
            return
        todo_id = int(sys.argv[2])
        todo = manager.complete(todo_id)
        if todo:
            print(f"✓ Completed: {todo.title}")
        else:
            print(f"Error: Todo {todo_id} not found")
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Todo ID required")
            return
        todo_id = int(sys.argv[2])
        if manager.delete(todo_id):
            print(f"✓ Deleted todo {todo_id}")
        else:
            print(f"Error: Todo {todo_id} not found")
    
    elif command == "help":
        print_help()
    
    else:
        print(f"Unknown command: {command}")
        print_help()

def print_help():
    print("""
Todo CLI - Simple command-line todo manager

Usage:
  todo-cli add <title>        Add new todo
  todo-cli list               List all todos
  todo-cli complete <id>      Mark todo as complete
  todo-cli delete <id>        Delete todo
  todo-cli help               Show this help
""")

if __name__ == "__main__":
    main()
