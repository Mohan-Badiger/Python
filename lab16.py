#python program to demonstrate GUI using tkinter
import tkinter as tk
import tkinter.messagebox as msgbox
form=tk.Tk()
form.geometry('600x500')

lbluno=tk.Label(form,text="UUCMS NO")
lbluno.grid(row=0,column=0,sticky=tk.W)

etuno=tk.Entry(form,width=40)
etuno.grid(row=0,column=1,padx=10,pady=5)

lblname=tk.Label(form,text="NAME")
lblname.grid(row=1,column=0,sticky=tk.W)

etname=tk.Entry(form,width=40)
etname.grid(row=1,column=1,padx=10,pady=5)

lblgender=tk.Label(form,text="GENDER")
lblgender.grid(row=2,column=0,sticky=tk.W)

gendervar=tk.StringVar()
gendervar.set("male")

rdbmale=tk.Radiobutton(form,variable=gendervar,value="male",text="male")
rdbfemale=tk.Radiobutton(form,variable=gendervar,value="female",text="female")
rdbmale.grid(row=2,column=1,padx=10,pady=5)
rdbfemale.grid(row=2,column=2,padx=20,pady=5)

lblnotify=tk.Label(form,text="Notification want to recive through")
lblnotify.grid(row=3,column=0,sticky=tk.W)

wappvar=tk.BooleanVar()
chkbwapp=tk.Checkbutton(form,text="Whatsapp",variable=wappvar)

emailvar=tk.BooleanVar()
chkbemail=tk.Checkbutton(form,text="Email",variable=emailvar)

chkbwapp.grid(row=3,column=1,padx=10,pady=5)
chkbemail.grid(row=3,column=2,padx=10,pady=5)

def save():
    uno=etuno.get()
    name=etname.get()
    gender=gendervar.get()
    wapp=wappvar.get()
    email=emailvar.get()
    row=f"UUCMSNO={uno} Name={name} Gender={gender}"
    if wapp:
        row=row+" Notification through whatsapp"
        if email:
            row=row+"and Email"
    file=open("student1.csv","a")
    file.write(row)
    file.close()
    msgbox.showinfo("Message","Data saved successfully")
btnsave=tk.Button(form,text="SAVE",command=save)
btnsave.grid(row=4,column=0,columnspan=2,padx=50,pady=20)
form.mainloop()
