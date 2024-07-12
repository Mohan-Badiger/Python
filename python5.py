#python program to read a number and find weather it is prime or not
n=int(input("enter the no"))
i=2
flag=False
while i<=n//2:
    r=n%i
    if r==0:
        flag=True
        break
    i=i+1
if flag==True:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")