#Initialize empty list
tasks = []
#Add tasks
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added to the list.')

# viewing tasks
def view_tasks():
    if tasks:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")

#main menu
def main():
    while True:
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        choice = input ("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Code. Try again.")

if __name__== "__main__":
    main()