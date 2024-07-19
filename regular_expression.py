#write a python program to read date of birth find that weather it is a valid date or not the format should be dd-mm-yyyy
import re
dob=input("Enter the date of birth ")
if re.match(r"^\d{2,2}\-\d{2,2}\-\d{4,4}$",dob):
    print(f"{dob} is valid date of birth")
else:
    print(f"{dob} is not valid date of birth \n please enter valid date of birth")
    
