#stack
stack=[]
size=5
def push(item):
    if len(stack)==size:
        print("stack is full")
    else:
        stack.append(item)
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        item=stack.pop()
        print(f"{item} is deleted")
def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack)

while (True):
    print("1-push")
    print("2-pop")
    print("3-display")
    print("4-exit")

    ch=int(input("enter your choice"))
    if ch==1:
        item=int(input("enter element"))
        push(item)
    elif ch==2:
        pop()
    elif ch==3:
        display()
    else:
        break