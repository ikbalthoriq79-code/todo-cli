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
        priority = "medium"
        category = "general"
        # Check for --priority and --category flags
        if "--priority" in sys.argv:
            idx = sys.argv.index("--priority")
            if idx + 1 < len(sys.argv):
                priority = sys.argv[idx + 1]
        if "--category" in sys.argv:
            idx = sys.argv.index("--category")
            if idx + 1 < len(sys.argv):
                category = sys.argv[idx + 1]
        todo = manager.add(title, priority)
        print(f"✓ Added: {todo.title} (ID: {todo.id}, Priority: {priority}, Category: {category})")
    
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
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("Error: Search query required")
            return
        query = " ".join(sys.argv[2:])
        results = manager.search(query)
        if not results:
            print(f"No todos found matching '{query}'")
            return
        print(f"Search results for '{query}':")
        for todo in results:
            status = "✓" if todo.completed else "○"
            print(f"{status} [{todo.id}] {todo.title} ({todo.priority}) - {todo.category}")
    
    elif command == "filter":
        if len(sys.argv) < 3:
            print("Error: Category required")
            return
        category = sys.argv[2]
        results = manager.filter_by_category(category)
        if not results:
            print(f"No todos in category '{category}'")
            return
        print(f"Todos in category '{category}':")
        for todo in results:
            status = "✓" if todo.completed else "○"
            print(f"{status} [{todo.id}] {todo.title} ({todo.priority})")
    
    else:
        print(f"Unknown command: {command}")
        print_help()

def print_help():
    print("""
Todo CLI - Simple command-line todo manager

Usage:
  todo-cli add <title>                    Add new todo
  todo-cli add <title> --priority high    Add with priority
  todo-cli add <title> --category work    Add with category
  todo-cli list                           List all todos
  todo-cli complete <id>                  Mark todo as complete
  todo-cli delete <id>                    Delete todo
  todo-cli search <query>                 Search todos
  todo-cli filter <category>              Filter by category
  todo-cli help                           Show this help

Examples:
  todo-cli add "Buy milk" --priority high --category shopping
  todo-cli search "milk"
  todo-cli filter shopping
""")

if __name__ == "__main__":
    main()
