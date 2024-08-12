import re
x=input("enter a string")
m=re.search(r"bldea college",x)
if m!=None:
    print(m)
else:
    print("blde students not found")
mobiles=re.findall(r"\d{10,10}",x)
print(mobiles)
y=re.sub(r"bldea college","Monu",x)
print(y)