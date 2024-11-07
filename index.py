class ToDoList:
    def __init__(self):
        self.tasks = []


    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")


    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['task']} - {status}")


    def update_task(self):
        self.view_tasks()
        try:
            task_number = int(input("\nEnter the task number to update: "))
            if 1 <= task_number <= len(self.tasks):
                new_task = input("Enter the updated task: ")
                self.tasks[task_number - 1]["task"] = new_task
                print(f"Task {task_number} updated to '{new_task}'!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


    def delete_task(self):
        self.view_tasks()
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


    def mark_completed(self):
        self.view_tasks()
        try:
            task_number = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_number <= len(self.tasks):
                self.tasks[task_number - 1]["completed"] = True
                print(f"Task {task_number} marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


    def menu(self):
        while True:
            print("\n--- To-Do List Menu ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Mark Task as Completed")
            print("6. Exit")
            choice = input("Choose an option: ")


            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_completed()
            elif choice == "6":
                print("Exiting To-Do List. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Initialize and run the To-Do List application
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.menu()
