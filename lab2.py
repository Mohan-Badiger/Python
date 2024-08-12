#python program to solve the quadratic equation
import cmath as m
a=int(input("enter 1st cofficient"))
b=int(input("enter 2nd cofficient"))
c=int(input("enter 3rd cofficient"))
d=b*b-4*a*c
if d>0:
    root1=-b+m.sqrt(d)/2*a
    root2=-b-m.sqrt(d)/2*a
    print("Roots are real")
    print(f"Root1={root1} and root2={root2}")
elif d==0:
    root1=root2=-b/2*a
    print("Both roots are equal")
    print(f"Root1={root1} and root2={root2}")
else:
    real1=-b/2*a
    img1=m.sqrt(d)/2*a
    real2=-b/2*a
    img2=-m.sqrt(d)/2*a
    print("Roots are imaginary")
    print(f"Root1={real1}+{img1}")
    print(f"Root2={real2}+{img2}")