#python program to demonstrate list operation and method 
#function to add stock items to inventory
stocklst=[]
def add():
    global stocklst
    item=input("enter stock item name ")
    stocklst.append(item)
    print(f"{item} has been added to stock list")
    print("stock list is as follows")
    print(stocklst)
    print(f"the no of items present in the stock list={len(stocklst)}")

#function to remove stock item
def delete():
    global stocklst
    item=input("enter the stock item to be deleted ")
    if item in stocklst:
        stocklst.remove(item)
        print(f"{item} has been removed from the stock lst")
    else:
        print(f"{item} has no found in the stock list")

#function to count stock item
def count():
    global stocklst
    item=input("enter the item to be continued")
    c=stocklst.count(item)
    print(f"{item} has found {c} times in stock list")

#function to list top N items
def display():
    global stocklst
    n=int(input("enter the nth no"))
    x=stocklst[:n]
    print(f"the first {n} items from stock list are as follows")
    for e in x:
        print(e)
    
#function to perform list filteration
def filter():
    global stocklst
    item=input("enter the item stock item which you want to create list")
    filterlst=[e for e in stocklst if e==item]
    print("the filtered list is as follows")
    print(filterlst)
while True:
    print("List Operations")
    print("1.Add stock item")
    print("2.Delete stock item")
    print("3.count the stock item")
    print("4.Display first N stock items")
    print("5.Filter the stock list")
    print("6.exit")
    ch=int(input("enter the choice"))
    if ch==1:
        add()
    elif ch==2:
        delete()
    elif ch==3:
        count()
    elif ch==4:
        display()
    elif ch==5:
        filter()
    elif ch==6:
        break
    else:
        print("enter correct choice")
