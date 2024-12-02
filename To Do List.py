# This is a simple T0-Do-List Application 
# Where user can Add, update, view and delete tasks.

tasks = []

def add_task ():
  # where user can add task
  
  task = input ("Enter a new task: ")
  tasks.append(task)
  print ("task added successfully.")

 # where user can view task
def view_task():
  if len(tasks) == 0:
    print("no task.")
  else:
    print("List of task")
  for  task in enumerate(tasks):
      print(f'{1==1 }, {task}') 

def update_task():
  if len (tasks) == 0:
    print 

def delete_task():
  if len(tasks) == 0:
    print("no task to delete.")
  else:
    print("tasks: ")
    for  task in enumerate(tasks):
     print(f'{1==1}, {task}')
    choice = int(input("Enter the task number to delete: "))
    if 0 < choice <= len(tasks):
       del tasks[choice - 1]
       print("task deleted successfully.")
    else:
       print("Ivalid task number.")
       
  
 
def main ():
  while True:
    print("\n To_Do-List Application")
    print("1, Add task")
    print("2, View task")
    print("3, Delete")
    print("4, Quit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
      add_task()
    elif choice == 2:
      view_task()
    elif choice == 3:
      delete_task()
    elif choice == 4:
      print("Thank you for using the To-Do-List Application.")
      break
    else:
      print("Invalid choice. Please try again")
      
if __name__ == "__main__":
 main()
 # by Musa A. Bility
