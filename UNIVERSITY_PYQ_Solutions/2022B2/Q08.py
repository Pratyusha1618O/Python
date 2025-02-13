# Write a program in Python to simulate stack operations using list (PUSH, POP, PEEP). Also check for
# overflow, underflow conditions available in a regular stack.


def isEmpty():
    return len(stack) == 0

def isFull():
    return len(stack) >= max

def push(data):
    if(isFull()):
        print("Stack overflow, no insertion")
        return
    for i in range(max): #let stack size is 5
        stack.append(data)
        return

def pop():
    if(isEmpty()):
        print("Stack underflow, no item to pop")
    else:
        return stack.pop()
    
def peek():
    if(isEmpty()):
        print("Stack underflow")
        return
    else:
        return stack[-1]
    
def display():
    if(isEmpty()):
        print("Stack is empty")
        return
    print(stack)


max = int(input("Enter stack size: "))
stack = []
while(True):
    print("\n")
    print("1.Push")
    print("2.pop")
    print("3.peek")
    print("4.display")
    print("5.Exit")
    ch = int(input("Enter your choise: "))

    if(ch == 1):
        data = input("Enter the element to push: ")
        push(data)
    elif(ch == 2):
        print("Popped element: ", pop())
    elif(ch == 3):
        print("Topmost element: ", peek())
    elif(ch == 4):
        display()
    elif(ch == 5):
        exit()
    else:
        print("wrong choise!!")
    

