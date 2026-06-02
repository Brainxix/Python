tasks = []
while True:
    print("\n to do list")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")

    choice= input(" choose an option: ")
    if choice == "1":
        task = input("enter task: ")
        tasks.append(task)
        print("task added")

    elif choice == "2":
        print("\n your task") 
        if len(tasks)==0:
            print("no task yet")
        else:
            for i, task in enumerate(tasks, start=1):
                print(1, task)
    elif choice == 3:
        print("\n your task:")
        for i, task in enumerate(task, start =1):
            print(i, task)
        num = int(input("Enter task number to remove: "))
        if 0 <num <= len(tasks):
            removed = tasks.pop(num -1)
            print("removed:", removed)
        else:
            print("invalid number")


    elif choice == 4:
        print("goodbye")
        break
    else:
        print("invalid choice")
