tasks = []

def add_task(task):
    """Add a new task to the list"""
    tasks.append(task)
    print(f'Added task: {task}')

def remove_task(task):
    """Remove a task from the list if it exists, otherwise report an error."""
    if task in tasks:
        tasks.remove(task)
        print(f'Removed task: {task}')
    else:
        print("Error: Task not found")

def view_task():
    """Print out all tasks in the list"""
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task}')

def update_task():
    """Update a task in the list"""
    tskno = int(input('Which task number would you like to update?: '))
    if 1 <= tskno <= len(tasks):
        old_task = tasks[tskno - 1]
        new_task = input('What would you like to change it to?: ')
        tasks[tskno - 1] = new_task
        print(f'Updated task: {old_task} to {new_task}')
    else:
        print("Invalid task number")

def mark_as_completed():
    """Mark a task as completed"""
    num = int(input('Which task number would you like to mark as complete?: '))
    if 1 <= num <= len(tasks):
        completed_task = tasks.pop(num - 1)
        print(f'Marked task as completed: {completed_task}')
    else:
        print("Invalid task number")

name = input('Please enter your Name: ')
while True:
    print('---------------------------------------------------------------------')
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View All Tasks")
    print("4. Update Task")
    print('5. View All Completed Tasks')
    print("6. Mark as Completed")
    print("7. Logout")
    print('---------------------------------------------------------------------')
    choice = int(input(f'Hii {name}, please choose the task you want to do: '))
    if choice == 1:
        task = input('Enter Your Task:\n')
        add_task(task)
    elif choice == 2:
        task = input('Enter the task you want to delete:\n')
        remove_task(task)
    elif choice == 3:
        view_task()
    elif choice == 4:
        update_task()
    elif choice == 5:
        print('\nCompleted Tasks:')
        view_task()
    elif choice == 6:
        mark_as_completed()
    elif choice == 7:
        break

print(f'\n----- Thank you! Have a great day, {name} -----')
