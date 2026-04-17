from models import Task
from manager import TaskManager
from validators import InvalidNameError, InvalidDateError, InvalidPriorityError, validate_date, validate_name_task, validate_priority
from database import init_db
#maaain
def ask_task():
    while True:
        name = input("Enter a name of task: ").strip()
        try:
            validate_name_task(name)
            break
        except InvalidNameError as e:
            print(e)
    while True:
        priority = input("Enter a priority(low/medium/high): ").lower().strip()
        try:
            validate_priority(priority)
            break
        except InvalidPriorityError as e:
            print(e)
    while True:
        deadline = input("Enter a deadline YYYY-MM-DD: ").strip()
        try:
            validate_date(deadline)
            break
        except InvalidDateError as e:
            print(e)
    return Task(name, priority, deadline)

def mark_task(manager):
    tasks = manager.get_all()
    if not tasks:
            print("No tasks yet")
            return
    manager.show_tasks()
    while True:
        try:
            index = (int(input("Enter task number: ")) - 1)
            if 0 <= index < len(tasks):
                return index
            else:
                print("Number of task is out of range")
        except ValueError:
            print("Must be a number")
def rem_task(manager):
    tasks = manager.get_all()
    if not tasks:
        print("No tasks yet")
        return
    manager.show_tasks()
    while True:
        try:
            index = (int(input("Enter task number: ")) - 1)
            if 0 <= index < len(tasks):
                manager.remove(index)
                print("Task deleted")
                break
            else:
                print("Number is out of range of tasks")
        except ValueError:
            print("Must be a number")

def main():
    init_db()
    manager = TaskManager()
    while True:
        action = input("Enter an action(add/show/mark/rem/exit): ").lower().strip()
        if action == "add":
            manager.add(ask_task())
        elif action == "show":
            manager.show_tasks()
        elif action == "mark":
            index = mark_task(manager)
            if index is not None:
                manager.toggle_done(index)
                print("Status updated")
        elif action == "rem":
            rem_task(manager)
        elif action == "exit":
            break
        else:
            print("Wrong input")

if __name__ == "__main__":
    main()
