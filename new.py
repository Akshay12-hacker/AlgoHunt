queue = []

def enqueue():
    element = input("Enter element to insert: ")
    queue.append(element)
    print(f"{element} is inserted into the queue.")
    
def delqueue():
    if not queue:
        print("Queue is empty! Cannot remove element.")
    else:
        removed = queue.pop(0)
        print(f"{removed} is removed from the queue.")
        
def display():
    if not queue:
        print("Queue is empty.")
    else:
        print("Current queue: ",queue)
        
while True:
    print("\n---Queue Operations---")
    print("1. Enqueue (Insert)")
    print("2. Delqueue (Remove)")
    print("3. Display ")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice =='1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice =='4':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! PLease enter between 1-4.")
