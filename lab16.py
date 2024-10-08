#python program to demonstrate database using sqlite3
import sqlite3 as sql
con=sql.connect("example.db")
cur=con.cursor()
sql="""
create table if not exists student
(
rno varchar(10),
name varchar(10),
primary key(rno)
)
"""
cur.executescript(sql)
con.commit
print("Table Created")
for i in range(1,6):
    rno=input(f"Enter roll no of {i} student")
    name=input(f"Enter name {i} student")
    cur.execute("insert into student(rno,name) values(?,?)",(rno,name))
con.commit()
print("data Inserted")

def display():
    global cur
    cur.execute("select * from student")
    rows=cur.fetchall()
    print("Student data as follows")
    print("Rollno\t|Name\t|")
    for row in rows:
        rno=row[0]
        name=row[1]
        print(f"{rno}\t|{name}\t|")
display()
rno=input("Enter the roll no you want to update")
name=input("Enter the correct name")
cur.execute("update student set name=? where rno=?",(name,rno))
con.commit()
print("data updated")
display()
rno=input("enter the roll no you want to delete")
cur.execute("delete from student where rno=?",(rno,))
con.commit()
print("data deleted")
display()
con.close()