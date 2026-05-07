students = []

# Add Student
def add_student():
    name = input("Enter name: ")

    for s in students:
        if s['name'] == name:
            print("Student already exists!")
            return

    marks = []
    n = int(input("How many subjects: "))

    for i in range(n):
        m = int(input("Enter mark: "))
        marks.append(m)

    students.append({'name': name, 'marks': marks})
    print("Student added successfully!")


# Display Students
def display_students():
    if not students:
        print("No students found.")
        return

    for s in students:
        print("Name:", s['name'], "Marks:", s['marks'])


# Calculate Total & Average
def calculate_total_average(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg


# Find Topper
def find_topper():
    if not students:
        print("No data available.")
        return

    topper = max(students, key=lambda s: sum(s['marks'])/len(s['marks']))
    print("Topper:", topper['name'])


# Search Student
def search_student():
    name = input("Enter name to search: ")

    for s in students:
        if s['name'] == name:
            print("Found:", s)
            return

    print("Student not found.")


# Pass/Fail Check
def check_pass_fail():
    for s in students:
        total, avg = calculate_total_average(s['marks'])
        if avg >= 50:
            print(s['name'], "- Pass")
        else:
            print(s['name'], "- Fail")


# Remove Student
def remove_student():
    name = input("Enter name to remove: ")

    for s in students:
        if s['name'] == name:
            students.remove(s)
            print("Student removed.")
            return

    print("Student not found.")


# Sort Students
def sort_students():
    students.sort(key=lambda s: sum(s['marks'])/len(s['marks']), reverse=True)
    print("Students sorted.")


# Count Students
def count_students():
    print("Total students:", len(students))


# Show Passed Students
def show_passed():
    for s in students:
        avg = sum(s['marks']) / len(s['marks'])
        if avg >= 50:
            print(s['name'])


# Menu
while True:
    print("\n--- Smart Student Manager ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Search Student")
    print("5. Pass/Fail Check")
    print("6. Remove Student")
    print("7. Sort Students")
    print("8. Count Students")
    print("9. Show Passed Students")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        find_topper()
    elif choice == 4:
        search_student()
    elif choice == 5:
        check_pass_fail()
    elif choice == 6:
        remove_student()
    elif choice == 7:
        sort_students()
    elif choice == 8:
        count_students()
    elif choice == 9:
        show_passed()
    elif choice == 10:
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")