#python program to read a number n and find sum of n natural numbers
n=int(input("Enter a number"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(f"sum={sum}")