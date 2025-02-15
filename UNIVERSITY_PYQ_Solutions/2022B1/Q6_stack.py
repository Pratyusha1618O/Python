#Stack data structure
#push(), pop(), peek(), empty()

def isEmpty():
    return len(stack) == 0

def push(data):
    stack.append(data)

def pop():
    if(isEmpty()):
        print("Stack Underflow")
    else:
        return stack.pop()

def peek():
    if(isEmpty()):
        print("Stack is empty")
    else:
        return stack[-1]

def display():
    print(stack)

stack = []

def main():
    while(1):
        print("\n")
        print("1.Push")
        print("2.POP")
        print("3.Print the topmost element")
        print("4.Print stack")
        print("5.Exit")
        ch = int(input("=>Enter your choice: "))

        if(ch == 1):
            data = input("Enter the element to be pushed: ")
            push(data)
        elif(ch == 2):
            data = pop()
            print("Popped element is: ",data)
        elif(ch == 3):
            print("The topmost element is: ", peek())
        elif(ch == 4):
            display()
        elif(ch == 5):
            exit(1)
        else:
            print("Wrong choice!!")

if __name__ == "__main__":
    main()
        






        
