## Queue

queue = []
front = 0
rear = 0
max = int(input("Enter maximum size of queue: "))

def isFull():
    return len(queue) >= max

def isEmpty():
    return len(queue) == 0

def enqueue(data):
    global rear
    if(isFull()):
        print("Queue overflow, no insertion.")
        return
    else:
        queue.append(data)
        rear += 1

def dequeue():
    global front, rear
    if(isEmpty()):
        print("Queue underflow, no element to delete.")
        return
    else:
        val = queue.pop(0) # remove first element
        rear -= 1 # adjust rear
        return val

def display():
    if(isEmpty()):
        print("Queue is empty")
    else:
        print(queue)




while(True):
    print("\n")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    ch = int(input("Enter your choise: "))

    if(ch == 1):
        data = int(input("Enter the elem to insert: "))
        enqueue(data)
    elif(ch == 2):
        val = dequeue()
        if val is not None:
            print("Dequeued element is: ", val)
    elif(ch == 3):
        display()
    elif(ch == 4):
        exit()
    else:
        print("Wrong choise!!")

        
