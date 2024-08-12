#python program to find the addition of two numbers and demonstrate the exception handling
try:
    x=int(input("Enter first value "))
    y=int(input("Enter second number "))
    z=x+y
    print(f"sum is : {z}")
except ValueError:
    print("Data is Invalid")
finally:
    print("Thank you for using")