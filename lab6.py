#sequential search
n=int(input("enter the elements"))
x=[]
for i in range(0,n):
    v=int(input(f"enter {i} element"))
    x.append(v)
key=int(input("enter the element to be searched"))
pos=-1
for i in range(0,n):
    if x[i]==key:
        pos=i
        break
if pos==1:
    print(f"{key} element is found")
else:
    print(f"{key} element is found at the {pos} position")