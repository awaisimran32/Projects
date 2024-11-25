def task():
    tasks=[]
    print("------------------------Welcome to the TaskManager--------------------------\n------------------------How can I Manage your Tasks--------------------------")
    
    
    total_task=int(input("How Many Tasks are you Planing to do today :"))   
    for i in range(1,total_task+1):
        task_name=input(f"Enter the Task {i} : ")
        tasks.append(task_name)
    print(f"Todays Tasks are \n {tasks}")

    while True:
        operation = int(input("Enter 1 to ADD\n2 to Update\n3 to delete\n4 to view\n5 to exit\nChoose one : "))
        if operation==1:
            add=input("Give the task to add : ")
            tasks.append(add)
            print(f"Task {add} is added")
        elif operation==2:
            update=input("Enter the task you want to update : ")
            if update.lower() in tasks:
                new=input("What do you want to add : ")
                tasks.append(new)
            else:
                print("There is no Such task in the list.")
        elif operation==3:
            de=input("Which task do you like to remove : ")
            if de in tasks:
                tasks.remove(de)
            else:
                print("There is No such task in your list")
        elif operation==4:
            print(f"Total Tasks={tasks}")
        elif operation==5:
            print("You exited the task manager:)")
            break
        else:
            print("Invalid input")

task()