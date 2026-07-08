
def add_task(tasks):
    task=input("Input tasks :")
    marks='False'
    task={
        "task":task,
        "mark":marks
    }
    tasks.append(task)
    print("Task added completed")
    return tasks

def delete_task(tasks):
    del_task = input("Enter task to be deleted: ")

    for task in tasks:
        if del_task.lower() == task["task"].lower():
            tasks.remove(task)
            print("Task removed successfully.")
            return

    print("Task not found.")

def mark_task(tasks):
    task2=input("Enter task name to be marked as completed.")
    for task in tasks:
        if task["task"]==task2.lower():
            task['mark']="True"
            print("Task Completed.")
    return tasks

def display_tasks(tasks):
    print(tasks)

def menu():
    print("\n=====List Manager Details=====")
    print("1.Add task")
    print("2.Delete task")  
    print("3.Mark task")
    print("4.Display task")
    print("5.Exit")

def main():
    tasks=[]
    while True:
        menu()
        ch=int(input("Enter your choice :"))
        if ch==1:
            add_task(tasks)
        elif ch==2:
            delete_task(tasks)
        elif ch==3:
            mark_task(tasks)
        elif ch==4:
            display_tasks(tasks)
        elif ch==5:
            print("Thank you ")
            break
        else:
            print("Invalid options")

main()