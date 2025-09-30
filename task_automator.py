from datetime import datetime

TASKS = 'C:/Users/aaron/OneDrive/Desktop/Coding/Python/CLI/CLI_Task_automator/tasks.txt'
DONE_TASKS = 'C:/Users/aaron/OneDrive/Desktop/Coding/Python/CLI/CLI_Task_automator/done_tasks.txt'

print("Your current list:")
print()

def read_tasks(list):
    for task_num in range(0,len(list)):
        print(str(task_num + 1) + ". " + list[task_num])
    #Prints each task along with its index (the index is incremented by 1 for readability)

def write_task():
    #Append new task to tasks file and list
    
    print()
            
    new_task = input("What is the new task?")
        
    with open(TASKS, 'a') as tasks:
        tasks.writelines(new_task + '\n')
        
    with open(TASKS) as tasks:
        task_list = []

        for task in tasks:
            task_list.append(task.strip())
        #Sorts each task in the tasks.txt file into a list  
            
    print("Your new list:")
    print()
     

def finish_task():
    #Remove a task from both list and tasks file whilst adding it to the created done_tasks file 
    
    with open(TASKS) as tasks:
        task_list = []

        for task in tasks:
            task_list.append(task.strip())
        #Sorts each task in the tasks.txt file into a list  
    
    print()
    
    read_tasks(task_list)
            
    print()

    while True:
        completed_task = input("Enter the number of the task you've completed: ")
        try:
            completed_task = int(completed_task)
            if 1 <= completed_task <= len(task_list):
                break
            print("Invalid input! Please enter an available number")
            print()
        except ValueError:
            print("Invalid input! Please enter a valid number")
            print()
    print()
    #Asks the user what task is completed and ensures no input error
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
                
    with open(DONE_TASKS, 'a') as done_tasks:
        done_tasks.write(task_list[completed_task - 1] + ' - Completed at:' + current_time + '\n')
        #Creates a text file called done_tasks and adds the completed task to it
                
    del task_list[completed_task - 1]
    #Deletes the completed task from the list
            
    with open(TASKS, 'w') as tasks:
        for task_num in range(1,len(task_list) + 1):
            tasks.write(task_list[task_num - 1] + '\n')
        #Overwrites tasks.txt leaving only the unfinished tasks
            
    print("Good job!")
    print()
    print("Your new list:")
    print()
            
  
def menu_loop():
    
    while True:
        with open(TASKS) as tasks:
            task_list = []
                
            for task in tasks:
                task_list.append(task.strip())
            #Sorts each task in the tasks.txt file into a list  
            
        read_tasks(task_list) 
            
        print()
            
        read_write = input("Would you like to add a new task (1) , to tick one off (2) or quit (q) ? ")
            
        while read_write not in ('1','2','q'):
            print()
            print("Invalid input! Please enter a 1 , 2 or q!")
            print()
            read_write = input("Would you like to add a new task (1) , to tick one off (2) or quit (q) ? ")
            print()
        #Asks user what is desired and ensures no input error
        
        if read_write == '1':
            write_task()
        elif read_write == '2':
            finish_task()
        else:
            print("Thanks for using Task Automator!")
            break
        
menu_loop()