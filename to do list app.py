import time
tasks=[]
def addtasks():
    task=input("Enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list")
def listTasks():
    if not tasks:
        print("There is no tasks currently.")
    else:
        print("Currant task")
        for index,task in enumerate(tasks):
            print(f"Task #{index}.{task}")
            
def deletetasks():
    listTasks()
    try:
        tasktodelete=int(input("choose the number to delete"))
        if tasktodelete >=0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"Task '{tasks}'Successfully Deleted.")
        else:
            print("task to delete not found.")
    except:
        print("invalid input")
    
if __name__ =="__main__":
    ###Create a loop to run the app
    print("Welcome to the To-do list app")
    while True:
        print("What would you like to do")
        while True:
            print("Please select an option from the following")
            time.sleep(3)#add 3 seconds pause for the user to read
            print("1.Add a new task")
            print("2.Delete a task")
            print("3.List all task")
            print("4. Quit")
            choice=(input("kindly enter you choice"))
            if choice=='1':
                addtasks()
            elif choice=='2':
                deletetasks()
            elif choice=='3':
                listTasks()
            
            elif choice=='4':
                break
            else:
                print("Invalid input, please try again.")
                print("Goodbye")

            




















                 
