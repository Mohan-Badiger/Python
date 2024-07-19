#python program to demonstrate the file read and write operation
def read():
    file=open("student.csv","r")
    data=file.readlines()
    print("the student data is as follow as")
    for line in data:
        print(line)
    file.close()
def write():
    uno=input("enter uucms no")
    name=input("enter the name")
    line=f"{uno},{name}\n"
    file=open("student.csv","a")
    file.write(line)
    file.close()
    print("student data written successsfully")
while True:
    print("File Operations")
    print("1.Add new Student")
    print("2.Read student")
    print("3.exit")

    ch=int(input("enter your choice"))
    if ch==1:
        write()
    elif ch==2:
        read()
    else:
        break
