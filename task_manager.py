import datetime
import uuid

class Task:
    __task_list = []
    __incompleted_list = []
    __completed_list = []


    def __init__(self, name):
        self.name = name
        self.created_time = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
        self.updated_time = None
        self.completed_time = None
        self.task_done = False
        self.id = uuid.uuid4()


        Task.__task_list.append(self)
        Task.__incompleted_list.append(self)


    def update_task():
        if Task.__incompleted_list.count == 0:
            print("No task to update!")
        else:
            print("Select which task to update\n\n")


            for i, e in enumerate(Task.__incompleted_list):
                print("Task no - " + str(i + 1))
                print("ID - " + str(e.id))
                print("Task - " + e.name)
                print("Created time - " + str(e.created_time))
                print("Updated time - " + str(e.updated_time))
                print("Completed - " + str(e.task_done))
                print("Completed time - " + str(e.completed_time))
                print("\n")


            x = int(input("Enter task no: "))
            for i, e in enumerate(Task.__incompleted_list):
                if x == i + 1:
                    new_task = input("Enter new task: ")
                    e.name = new_task
                    e.updated_time = datetime.datetime.now().strftime(
                        "%m/%d/%y %H:%M:%S"
                    )
                    print("Task updated successfully")
                    return


            print("Task not found!")


    def complete_task():
        if Task.__incompleted_list.count == 0:
            print("No task to complete!")
        else:
            print("Select which task to complete\n\n")


            for i, e in enumerate(Task.__incompleted_list):
                print("Task no - " + str(i + 1))
                print("ID - " + str(e.id))
                print("Task - " + e.name)
                print("Created time - " + str(e.created_time))
                print("Updated time - " + str(e.updated_time))
                print("Completed - " + str(e.task_done))
                print("Completed time - " + str(e.completed_time))
                print("\n")


            x = int(input("Enter task no: "))
            for i, e in enumerate(Task.__incompleted_list):
                if x == i + 1:
                    e.task_done = True
                    e.completed_time = datetime.datetime.now().strftime(
                        "%m/%d/%y %H:%M:%S"
                    )
                    Task.__completed_list.append(e)
                    Task.__incompleted_list.remove(e)
                    print("Task completed successfully")
                    return


            print("Task not found!")


    def view_tasks():
        for i in Task.__task_list:
            print("ID - " + str(i.id))
            print("Task - " + i.name)
            print("Created time - " + str(i.created_time))
            print("Updated time - " + str(i.updated_time))
            print("Completed - " + str(i.task_done))
            print("Completed time - " + str(i.completed_time))
            print("\n")


    def view_incomplete():
        if len(Task.__incompleted_list) == 0:
            print("No incomplete task")
        else:
            for i in Task.__incompleted_list:
                print("ID - " + str(i.id))
                print("Task - " + i.name)
                print("Created time - " + str(i.created_time))
                print("Updated time - " + str(i.updated_time))
                print("Completed - " + str(i.task_done))
                print("Completed time - " + str(i.completed_time))
                print("\n")


    def view_complete():
        if len(Task.__completed_list) == 0:
            print("No completed task")
        else:
            for i in Task.__completed_list:
                print("ID - " + str(i.id))
                print("Task - " + i.name)
                print("Created time - " + str(i.created_time))
                print("Updated time - " + str(i.updated_time))
                print("Completed - " + str(i.task_done))
                print("Completed time - " + str(i.completed_time))
                print("\n")




def run():
    print("\n")
    print("1. Add new task")
    print("2. Show all tasks")
    print("3. Show incomplete tasks")
    print("4. Show completed tasks")
    print("5. Update task")
    print("6. Mark a task completed\n")
    x = int(input("Enter option: "))


    if x == 1:
        print("\n")
        name = input("Enter name of task: ")
        task = Task(name)
        print("\nTask created successfully")
        run()
    elif x == 2:
        print("\nShowing all tasks\n")
        Task.view_tasks()
        run()


    elif x == 3:
        print("\nShowing incomplete tasks\n")
        Task.view_incomplete()
        run()


    elif x == 4:
        print("\nShowing completed tasks\n")
        Task.view_complete()
        run()


    elif x == 5:
        print("\n")
        Task.update_task()
        run()


    elif x == 6:
        print("\n")
        Task.complete_task()
        run()


    else:
        print("Please select a correct option!\n")
        run()




run()



