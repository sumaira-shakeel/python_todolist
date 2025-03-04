import os  # to check if the file exists
import json

import click  # to load and save tasks from JSON files

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []  # If file doesn't exist, return an empty list

    with open(TODO_FILE, "r") as file:
        try:
            return json.load(file)  # Load tasks from the file
        except json.JSONDecodeError:
            return []  # If JSON is invalid, return an empty list

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)  # Save tasks in a formatted way

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")


@click.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks available.")
        return
    for index, task in enumerate(tasks,1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} ({status})")
@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Complete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] ["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} completed successfully.")
    else:
        click.echo(f"Invalid task number: {task_number}")
@click.command()
@click.argument("task_number",type=int)
def delete(task_number):
    """Delete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        del_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Delete task: {del_task['task']}")
    else:
       click.echo(f"Invalid task number: {task_number}")




    
        

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)


if __name__ == "__main__":
    cli()
 
                