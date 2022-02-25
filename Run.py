from tkinter import *
import backend
#===============================setting==============================
root = Tk()
root.title("contact app")
root.geometry("650x500")
root.resizable(False,False)
root.configure(bg="lightblue")
frame1 = LabelFrame(root,text="Register pannel",padx=70,pady=80,bg="lightblue")
frame2 = LabelFrame(root,text="Login pannel",padx=70,pady=80,bg="lightblue")
frame3 = LabelFrame(root,text="Admin pannel",padx=99,pady=43,bg="lightblue")
#===============================root-page==============================

l1 = Label(root,text="**Welcome to contact app**",bg="lightblue")
l1.grid(padx=235,pady=40)
l2 = Label(root,text="First page",bg="lightblue")
l2.grid(pady=5)
l3 = Label(root,text="Guide : your contact's can be save in this app. ",bg="lightblue")
l3.grid(pady=10)
l4 = Label(root,text="Please Register!",bg="lightblue")
l4.grid(pady=10)

btn1 = Button(root,text="register",width=7,bg="lightgreen",command=lambda:registerbuttoncomm())
btn1.grid(pady=10)

l5 = Label(root,text="LOGIN IS ESSENTIAL!",bg="lightblue")
l5.grid(pady=10)

btn2 = Button(root,text="login",width=7,bg="lightgreen",command=lambda:loginbuttoncomm())
btn2.grid()

l6 = Label(root,text="Warning : Choose Carfully You Can't Get Back Here!!!",bg="lightblue")
l6.grid(pady=20)

#===============================Functions==============================

#register button root page
def registerbuttoncomm():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
    btn1.destroy()
    btn2.destroy()
    frame1.pack(padx=125,pady=90)

#frame1 register and next
def regi_s():
    if len(username_text.get()) != 0:
        if len(password_text.get()) >= 4:
            users = backend.search_user(username_text.get(),password_text.get())
            if users != []:
                frame1.destroy()
                frame2.pack(padx=125,pady=90)
            else:
                backend.insert_user(username_text.get(),password_text.get())
                frame1.destroy()
                frame2.pack(padx=125,pady=90)

#login button root page
def loginbuttoncomm():
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
    btn1.destroy()
    btn2.destroy()
    frame2.pack(padx=125,pady=90)

#frame2 button login
def log_s():
    users = backend.search_user(username_log_text.get(),password_log_text.get())
    if users != []: 
        frame3.pack(fill='both',expand=1)   
        frame2.forget()
        
def clear():
    list1.delete(0,END)

def fill_list(contacts):
    for contact in contacts:
        list1.insert(END,contact)

#click in the listbox
def get_selected_row(event):
    global selected_contact
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_contact = list1.get(index)
    
       
        e5.delete(0,END)
        e5.insert(END,selected_contact[2])
        e6.delete(0,END)
        e6.insert(END,selected_contact[3])
        e7.delete(0,END)
        e7.insert(END,selected_contact[4])    

#view button
def view_command():
    clear()
    contacts = backend.view(username_log_text.get())
    fill_list(contacts)

#search button
def search():
    clear()    
    contacts = backend.search(username_log_text.get(),name_c.get(),lastname_c.get(),ph_c.get())
    fill_list(contacts)

#Add button
def add():
    if len(name_c.get()) or len(lastname_c.get()) or len(ph_c.get()):
        backend.insert(username_log_text.get(),name_c.get(),lastname_c.get(),ph_c.get())
        view_command()

#Delete button
def Delete():
    backend.delete(selected_contact[0])
    view_command()

#Edit button
def edit():
    if len(name_c.get()) or len(lastname_c.get()) or len(ph_c.get()):
        backend.update(selected_contact[0],username_log_text.get(),name_c.get(),lastname_c.get(),ph_c.get())
        view_command()

#logout button
def logout():
    frame2.pack(fill='both',padx=125,pady=90)
    frame3.forget()
  
#===============================Frame-one==============================

l7 = Label(frame1,text="username",bg="lightblue")
l7.grid()

username_text = StringVar()
e1 = Entry(frame1,textvariable=username_text)
e1.grid(row=0,column=1)

l8 = Label(frame1,text="password",bg="lightblue")
l8.grid(row=1,column=0)

password_text = StringVar()
e2 = Entry(frame1,textvariable=password_text)
e2.grid(row=1,column=1)

btn3 = Button(frame1,text="save",width=7,bg="lightgreen",command=lambda:regi_s())
btn3.grid(row=2,column=1,pady=20)

#===============================Frame-two==============================

l9 = Label(frame2,text="username",bg="lightblue")
l9.grid(row=0,column=0)

username_log_text = StringVar()
e3 = Entry(frame2,textvariable=username_log_text)
e3.grid(row=0,column=1)

l10 = Label(frame2,text="password",bg="lightblue")
l10.grid(row=1,column=0)

password_log_text = StringVar()
e4 = Entry(frame2,textvariable=password_log_text)
e4.grid(row=1,column=1)

btn5 = Button(frame2,text="login",width=7,bg="lightgreen",command=lambda:log_s())
btn5.grid(row=2,column=1,pady=20)

btn_8 = Button(frame2,text="Exit",width=7,height=2,bg="lightgreen",command=root.destroy)
btn_8.grid(row=4,column=2,pady=20)

#===============================Frame-three==============================

#lable and entry
l_2 = Label(frame3,text="NAME ",bg="lightblue")
l_2.grid(row=0,column=0)

name_c = StringVar()
e5 = Entry(frame3,textvariable=name_c,bg="white")
e5.grid(row=0,column=1)

l_3 = Label(frame3,text="LASTNAME",bg="lightblue")
l_3.grid(row=0,column=3)

lastname_c = StringVar()
e6 = Entry(frame3,textvariable=lastname_c,bg="white")
e6.grid(row=0,column=4)

l_4 = Label(frame3,text="Phone_N ",bg="lightblue")
l_4.grid(row=1,column=0,pady=5)

ph_c = StringVar()
e7 = Entry(frame3,textvariable=ph_c,bg="white")
e7.grid(row=1,column=1)

#listbox & scroll
list1 = Listbox(frame3,width=35,height=19,bg="white")
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(frame3)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",get_selected_row)

#side buttons
btn_1 = Button(frame3,text="view all",width=11,height=2,bg="lightgreen",command=lambda:view_command())
btn_1.grid(row=2,column=4)

btn_2 = Button(frame3,text="Add",width=11,height=2,bg="lightgreen",command=lambda:add())
btn_2.grid(row=3,column=4)

btn_3 = Button(frame3,text="Edit",width=11,height=2,bg="lightgreen",command=edit)
btn_3.grid(row=4,column=4)

btn_4 = Button(frame3,text="Search",width=11,height=2,bg="lightgreen",command=lambda:search())
btn_4.grid(row=5,column=4)

btn_5 = Button(frame3,text="Delete",width=11,height=2,bg="lightgreen",command=lambda:Delete())
btn_5.grid(row=6,column=4)

btn_6 = Button(frame3,text="Logout",width=11,height=2,bg="lightgreen",command=logout)
btn_6.grid(row=7,column=4)

#=============================== END ==============================

root.mainloop()