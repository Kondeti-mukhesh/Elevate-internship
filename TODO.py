todo_list=[]

try:
    with open('todo.txt', 'r') as file:
        todo_list= [line.strip() for line in file]

except FileNotFoundError:
    print("todo.txt not found. empty list created")

def save_task():
    with open('todo.txt', 'w') as file:
        for task in todo_list:
            file.write(task+ "\n")

while True:
    print("\n📝 welcome to the To-Do menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice= input("enter your choice(1-4): ").strip()

    
    if choice=="1":
        add_new=input("enter the task:")
        todo_list.append(add_new)
        save_task()
        print("🎉 Task added!")
        

    elif choice=="2":
        if not todo_list:
            print("no tasks found")
        
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}.{task}")
    
    elif choice=="3":
        if not todo_list:
            print("no task removed")
        
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}.{task}")
                
            try:
                removed=int(input("enter the task number to remove: "))
                if 0< removed<=len(todo_list):
                    removed_task=todo_list.pop(removed-1)
                    save_task()
                    print("revome task:",removed_task)
                
                else:
                    print("invalid task number")
            
            except ValueError:
                print("invalid input. plese enter valid number")
    
    elif choice == "4":
        print("🙏 Thanks for using the To-Do App!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
