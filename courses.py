import customtkinter
import database
from tkinter import *
from tkinter import messagebox
app = customtkinter.CTk()
app.title("Courses")
app.geometry("700x600")
app.resizable(False,False)
app.config(bg="#131314")

font1 = ("Arial",30,"bold")
font2 = ("Arial",20,"bold")
font3 = ("Arial",15,"bold")

def updtcblist():
    list = idcom()
    seic['values'] = list

def search():
    selec = v3.get()
    if selec != "Select":
        row = database.search(selec)
        idll2.configure(text=row[0])
        namell.configure(text=row[1])
        duratll.configure(text=row[2])
        formatll.configure(text=row[3])
        langll.configure(text=row[4])
        pricell.configure(text=row[5])
    else:
        messagebox.showerror("Error","Select An ID.")
def idcom():
    ids = database.fetchids()
    ids_op = seic.configure(values = ids)
def submit():
    idd = ide.get()
    name = cne.get()
    dur = v1.get()
    format = v2.get()
    lan = lne.get()
    price = pre.get()
    try:
        if not(idd and name and dur and format and lan and price):
            messagebox.showerror("Error","Enter All Fields.")
        elif database.id_exists(idd):
            messagebox.showerror("Error","id Already Exists.")
        else:
            pricev = int(price)
            database.insert(idd,name,dur,format,lan,pricev)
            messagebox.showinfo("Success","Data Has Been Inserted")
    except ValueError:
        messagebox.showerror("Error","price Should Be Integer")
    except:
        messagebox.showerror("Error","Error occured")

def new():
    ide.delete(0,END)
    cne.delete(0,END)
    v1.set("1 Hour")
    v2.set("")
    lne.delete(0,END)
    pre.delete(0,END)



title = customtkinter.CTkLabel(app,font=font1,text="Course Data Entry:",text_color="#fff",bg_color="#131314")
title.place(x=25,y=20)

fr1 = customtkinter.CTkFrame(app,bg_color="#131314",fg_color="#292933",corner_radius=10,border_width=2,border_color="#0f0",width=650,height=230)
fr1.place(x=25,y=70)

fr2 = customtkinter.CTkFrame(app,bg_color="#131314",fg_color="#292933",corner_radius=10,border_width=2,border_color="#0f0",width=650,height=230)
fr2.place(x=25,y=350)


idl = customtkinter.CTkLabel(fr1,text="id:",font=font2,text_color="#fff")
idl.place(x=50,y=15)
ide = customtkinter.CTkEntry(fr1,font=font2,text_color="#000",fg_color="#fff",border_color="#B2016C",border_width=2,width=150)
ide.place(x=50,y=45)

cnl = customtkinter.CTkLabel(fr1,text="Course Name:",font=font2,text_color="#fff")
cnl.place(x=245,y=15)
cne = customtkinter.CTkEntry(fr1,font=font2,text_color="#000",fg_color="#fff",border_color="#B2016C",border_width=2,width=150)
cne.place(x=245,y=45)

cdl = customtkinter.CTkLabel(fr1,text="Course Duration:",font=font2,text_color="#fff")
cdl.place(x=445,y=15)
v1 = StringVar()
options = ["1 Hour","2 Hour","3 Hour"]
cde = customtkinter.CTkComboBox(fr1,font=font2,text_color="#fff",state="readonly",fg_color="#000",dropdown_hover_color="#B2016C",button_color="#B2016C",button_hover_color="#B2016C",border_color="#B2016C",values=options,variable=v1,width=150)
cde.set("1 Hour")
cde.place(x=445,y=45)

fol = customtkinter.CTkLabel(fr1,text="Format:",font=font2,text_color="#fff")
fol.place(x=40,y=90)

v2 = StringVar()
fo1 = customtkinter.CTkRadioButton(fr1,text="Online",fg_color="#B2016C",text_color="#fff",font=font2,hover_color="#B2016C",variable=v2,value="Online")
fo2 = customtkinter.CTkRadioButton(fr1,text="Class",fg_color="#B2016C",font=font2,hover_color="#B2016C",text_color="#fff",variable=v2,value="Class")
fo1.place(x=40,y=125)
fo2.place(x=140,y=125)


lnl= customtkinter.CTkLabel(fr1,text="Course Language:",font=font2,text_color="#fff")
lnl.place(x=245,y=90)
lne = customtkinter.CTkEntry(fr1,font=font2,text_color="#000",fg_color="#fff",border_color="#B2016C",border_width=2,width=150)
lne.place(x=245,y=120)

prl= customtkinter.CTkLabel(fr1,text="Course Price:",font=font2,text_color="#fff")
prl.place(x=445,y=90)
pre = customtkinter.CTkEntry(fr1,font=font2,text_color="#000",fg_color="#fff",border_color="#B2016C",border_width=2,width=150)
pre.place(x=445,y=120)

submitb = customtkinter.CTkButton(fr1,command=submit,font=font2,text="Submit",text_color="#fff",fg_color="#02ab10",hover_color="#029D20",bg_color="#292933", cursor = "hand2",corner_radius=5,width=100)
submitb.place(x=200,y=170)

clearb = customtkinter.CTkButton(fr1,command=new,font=font2,text="New Course",text_color="#fff",fg_color="#F45E02",hover_color="#F45E02",bg_color="#292933", cursor = "hand2",corner_radius=5,width=100)
clearb.place(x=330,y=170)


sel = customtkinter.CTkLabel(app,text="Search By ID:",font=font2,text_color="#fff",bg_color="#131314",)
sel.place(x=25,y=312)


v3 = StringVar()

seic = customtkinter.CTkComboBox(app,font=font2,text_color="#000",bg_color="#131314",fg_color="#fff",dropdown_hover_color="#B2016C",button_color="#B2016C",button_hover_color="#B2016C",border_color="#B2016C",width=150,variable=v3,state="readonly")
seic.set("Select")
seic.place(x=220,y=312)

seb = customtkinter.CTkButton(app,font=font2,command=search,text_color="#fff",text="Search",fg_color="#1345F9",hover_color="#0029BE",bg_color="#292933",cursor = "hand2",corner_radius=5,width=100)
seb.place(x=420,y=312)

seeb = customtkinter.CTkButton(app,font=font2,command=updtcblist,text_color="#fff",text="Update",fg_color="#F45E02",hover_color="#029D20",bg_color="#292933",cursor = "hand2",corner_radius=5,width=100)
seeb.place(x=550,y=312)


idl2 = customtkinter.CTkLabel(fr2,fg_color="#292933",text="Course ID",text_color="#fff",font=font3)
idl2.place(x=50,y=15)

idll2 = customtkinter.CTkLabel(fr2,fg_color="#292933",text="",text_color="#0f0",font=font3)
idll2.place(x=50,y=45)


namel = customtkinter.CTkLabel(fr2,fg_color="#292933",text="Course Name",text_color="#fff",font=font3)
namel.place(x=245,y=15)

namell = customtkinter.CTkLabel(fr2,fg_color="#292933",text="",text_color="#0f0",font=font3)
namell.place(x=245,y=45)

duratl = customtkinter.CTkLabel(fr2,fg_color="#292933",text="Course Duration",text_color="#fff",font=font3)
duratl.place(x=445,y=15)

duratll = customtkinter.CTkLabel(fr2,fg_color="#292933",text="",text_color="#0f0",font=font3)
duratll.place(x=445,y=45)

formatl = customtkinter.CTkLabel(fr2,fg_color="#292933",text="Course Format",text_color="#fff",font=font3)
formatl.place(x=40,y=90)

formatll = customtkinter.CTkLabel(fr2,fg_color="#292933",text="",text_color="#0f0",font=font3)
formatll.place(x=40,y=135)

langl = customtkinter.CTkLabel(fr2,fg_color="#292933",text="Course Language",text_color="#fff",font=font3)
langl.place(x=245,y=90)

langll = customtkinter.CTkLabel(fr2,fg_color="#292933",text="",text_color="#0f0",font=font3)
langll.place(x=245,y=135)

pricel = customtkinter.CTkLabel(fr2,fg_color="#292933",text="Course Price",text_color="#fff",font=font3)
pricel.place(x=445,y=90)

pricell = customtkinter.CTkLabel(fr2,fg_color="#292933",text="",text_color="#0f0",font=font3)
pricell.place(x=445,y=135)


idcom()



app.mainloop()