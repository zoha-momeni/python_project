from tkinter import*
from tkinter import messagebox
import database 
win=Tk()
win.geometry("405x430")
win_color="#e4a0f7"
win.configure(background=win_color)
db=database.database("D:/پایتون/zoha-file/zoha/database.db")
#=================function
def add():
   name=ent_name.get()
   lname=ent_lname.get()
   namee=ent_nameee.get()
   password=ent_password.get()
   db.insert_record(name,lname,namee,password)
   messagebox.showinfo("add","record add")


def remove():
    global record
    index = lst.curselection()
    name = db.select_record()
    record = name[index[0]]
    db.remove_item(record[0])
    show()

def clear():
    ent_name.delete(0,END)
    ent_lname.delete(0,END)
    ent_pass.delete(0,END)
    ent_password.delete(0,END)
    ent_nameee.delete(0,END)



def exittt():
    result=messagebox.askquestion('ask',"are ypu shure exit?")
    if result =="yes":
        win.destroy()

def show():
     lst.delete(0 , END)
     records = db.select_record()
    
     for record in records:
          lst.insert(END , record)


def search():
    password = ent_pass.get().strip()
    lst.delete(0, END)
    record = db.search(password)
    if record:
        messagebox.showinfo("vorod","KHOSH AMADID")
    else:
        messagebox.showerror("error","ETELAT SAHIH NIST")

def select():
    global record
    index = lst.curselection()

    index = index[0]
    names = db.select_record()
    record = names[index]

    ent_name.delete(0, END)
    ent_lname.delete(0, END)
    ent_password.delete(0, END)
    ent_nameee.delete(0, END)

    ent_name.insert(0, record[1])
    ent_lname.insert(0, record[2])
    ent_password.insert(0, record[3])
    ent_nameee.insert(0, record[4])
#==================widget
#==label
lbl_name=Label(win,text="name :",font="maler",bg="#e4a0f7")
lbl_name.place(x=5,y=5)
lbl_star=Label(win,text="*",font="maler 25",bg="#e4a0f7",fg="#6f2da8")
lbl_star.place(x=130,y=7)

lbl_lname=Label(win,text="L name :",font="maler",bg="#e4a0f7")
lbl_lname.place(x=5,y=35)
lbl_starr=Label(win,text="*",font="maler 25",bg="#e4a0f7",fg="#6f2da8")
lbl_starr.place(x=130,y=37)

lbl_password=Label(win,text="password :",font="maler",bg="#e4a0f7")
lbl_password.place(x=5,y=65)
lbl_starrr=Label(win,text="*",font="maler 25",bg="#e4a0f7",fg="#6f2da8")
lbl_starrr.place(x=130,y=66)

lbl_nameee=Label(win,text="corse name :",font="maler",bg="#e4a0f7")
lbl_nameee.place(x=5,y=100)

lbl_pass=Label(win,text="password :",font="maler",bg="#e4a0f7")
lbl_pass.place(x=5,y=390)
#====entry
ent_name=Entry(win,width=37,bg="#b660cd")
ent_name.place(x=160,y=12)

ent_lname=Entry(win,width=37,bg="#b660cd")
ent_lname.place(x=160,y=42)

ent_password=Entry(win,width=37,bg="#b660cd")
ent_password.place(x=160,y=70)

ent_nameee=Entry(win,width=37,bg="#b660cd")
ent_nameee.place(x=160,y=100)

ent_pass=Entry(win,width=45,bg="#b660cd")
ent_pass.place(x=110,y=395)
#====list
lst=Listbox(win,width=37,bg="#b660cd")
lst.place(x=160,y=150)

#====button
btn_add=Button(win,text="add",font="maler 10",bg="#b660cd",width=10,command=add)
btn_add.place(x=5,y=150)

btn_clear=Button(win,text="clear",font="maler 10",bg="#b660cd",width=10,command=clear)
btn_clear.place(x=5,y=180)

btn_delet=Button(win,text="delet",font="maler 10",bg="#b660cd",width=10,command=remove)
btn_delet.place(x=5,y=210)

btn_select=Button(win,text="select",font="maler 10",bg="#b660cd",width=10,command=select)
btn_select.place(x=5,y=240)

btn_exit=Button(win,text="exit",font="maler 10",bg="#b660cd",width=46,command=exittt)
btn_exit.place(x=5,y=350)

btn_see=Button(win,text="see all",font="maler 10",width=10,bg="#b660cd",command=show)
btn_see.place(x=5,y=270)

btn_search=Button(win,text="login",font="maler 10",width=10,bg="#b660cd",command=search)
btn_search.place(x=5,y=300)
#====scrollbar
scrol=Scrollbar(win,orient=VERTICAL)
scrol.place(x=380,y=150,height=164)

win.mainloop()
