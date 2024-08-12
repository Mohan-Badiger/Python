#list with selection sorting
n=int(input("enter a no of elements"))
x=[]
for i in range(0,n):
    v=int(input(f"enter the {i} element"))
    x.append(v)
for i in range(0,n):
    min=x[i]
    position=i
    for j in range(i+1,n):
        if x[j]<min:
            min=x[j]
            position=j

    temp=x[i]
    x[i]=x[position]
    x[position]=temp
print(f"sorted elements are")
for e in x:
    print(e)