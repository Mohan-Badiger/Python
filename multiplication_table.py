#python program to read a number and print multiplication table from 2 to n 
n=int(input("Enter the number"))
for j in range(1,11,1):
    for i in range(2,n+1,1):
        e=i*j
        print(e,end=" ")
    print("\n")
