#calc file is attached to lab6 
#first calc file second lab6 
import calc as c
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
result=c.add(x,y)
print(f"Addition= {result}")
result=c.sub(x,y)
print(f"Substraction= {result}")
result=c.mul(x,y)
print(f"Multification= {result}")
result=c.div(x,y)
print(f"Division= {result}")