#tkinter module
import tkinter as tk
import tkinter.messagebox as msgbox
form=tk.Tk()
form.geometry("500x500")
#label username
lbluname=tk.Label(form,text="Username",font=("Arial",16,"bold"))
lbluname.grid(row=0,column=0)
#entry username
etuname=tk.Entry(form,width=20,font=("Arial",16,'bold'))
etuname.grid(row=0,column=1)
#label password
lblpas=tk.Label(form,text="Password",font=("Arial",16,"bold"))
lblpas.grid(row=1,column=0)
#entry password
etpas=tk.Entry(form,width=20,font=("Areal",16,"bold"))
etpas.grid(row=1,column=1)
#display function 
def disp():
    u=etuname.get()
    p=etpas.get()
    if u=="Admin" and p=="123":
        msgbox.showinfo("Message","Loged in successfully...")
    else:
        msgbox.showinfo("Message","Invalid Username/Password...")
btnadd=tk.Button(form,text="Login",fg='red',font=("Areal",16,"bold"),command=disp)
btnadd.grid(row=2,column=1)
form.mainloop()