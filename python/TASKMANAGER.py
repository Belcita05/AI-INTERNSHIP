tasks = []
def add_task():
    name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    time = int(input("Enter time required (hours): "))
    
    task={
        "name":name,
        "priority":priority,
        "time":time,
        "status":"pending"
        
    }
    tasks.append(task)
    print("Task added successfully!\n")
    
    # 🔹 View Tasks
def view_tasks():
    if not tasks:
        print("No tasks available\n")
        return
    for i in range(len(tasks)):
        print(i, tasks[i])



# 🔹 Mark Task Completed
def mark_completed():
    view_tasks()
    index = int(input("Enter task index to mark completed: "))

    if 0 <= index < len(tasks):
        tasks[index]["status"] = "completed"
        print("Task marked as completed!\n")
    else:
        print("Invalid index\n")


# 🔹 Analyze Tasks
def analyze_tasks():
    total_time = 0
    high_priority = 0
    completed = 0
    pending = 0

    for task in tasks:
        total_time += task["time"]

        if task["priority"] == "high":
            high_priority += 1

        if task["status"] == "completed":
            completed += 1
        else:
            pending += 1

    print("Total tasks:", len(tasks))
    print("Total time:", total_time)
    print("High priority tasks:", high_priority)

    print("\nTasks taking more than 3 hours:")
    for task in tasks:
        if task["time"] > 3:
            print(task)

    # 🔹 Productivity Warning
    if total_time > 8:
        print("\n⚠ Warning: Too much workload!")

    if completed > pending:
        print("👍 Good job! You're productive!")

    print()


# 🔹 Main Menu
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Completed")
    print("4. Analyze Tasks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        analyze_tasks()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")
    
    
    

    