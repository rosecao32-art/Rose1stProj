def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")    

def show_menu():
    print("\nTo-Do List")            
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Exit")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("No taks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
    elif choice == "3":
        num = int(input("Enter task number to complet: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Taks completed!")
        else:
            print("Invalid task number.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")