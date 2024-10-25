from dis import disco


def print_menu():
    print("To-do list menu: ")
    print("0. View task")
    print("1. Add task")
    print("2. Remove task")
    print("3. Exit")


def get_choice():
    choices=( 0, 1, 2, 3)
    try:
        while True:
            choice =int(input(" Enter your choice: "))
            if (choice not in choices):
                print("Invalid choice, Try again. ")
                continue
            return choice
    except ValueError:
        print("Invalid choice, Try again. ")

def view_tasks(tasks):
    print(" The tasks are : ")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks to display.")
    print("")


def add_task(tasks):
    while True:
        new_task = input("Enter new task: ").strip()
        if new_task == "":
            print("Invalid task, Try again. ")
            continue
        else:
            return tasks.append(new_task)


def remove_task(tasks):
    view_tasks(tasks)
    while True:
        task_num=int(input("Enter task to remove: "))
        if 0< task_num <= len(tasks) :
            tasks.pop(task_num-1)
            break
        else:
            print("Invalid task, Try again. ")


def main():
    tasks=[]
    while True:
        print_menu()
        print("")
        choice = get_choice()
        if choice == 0:
            view_tasks(tasks)
        elif choice == 1:
            add_task(tasks)
        elif choice == 2:
            remove_task(tasks)
        else:
            break

if __name__ == "__main__":
    main()