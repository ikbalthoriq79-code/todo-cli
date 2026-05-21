# Todo CLI

Simple command-line todo manager written in Python.

## Features

- Add, list, complete, and delete todos
- Priority levels (high, medium, low)
- JSON-based storage
- Simple and intuitive CLI interface

## Installation

```bash
git clone https://github.com/ikbalthoriq79-code/todo-cli.git
cd todo-cli
pip install -r requirements.txt
```

## Usage

```bash
# Add a new todo
python -m todo_cli.main add "Buy groceries"

# List all todos
python -m todo_cli.main list

# Mark todo as complete
python -m todo_cli.main complete 1

# Delete todo
python -m todo_cli.main delete 1

# Show help
python -m todo_cli.main help
```

## Running Tests

```bash
python -m pytest tests/
```

## License

MIT
