import tkinter
from PIL import Image, ImageTk
import customtkinter
from tkinter import messagebox
from cProfile import label
import tkinter.messagebox
from subprocess import call
from tkinter import ttk,Tk
from tkinter import *
import mysql.connector
from PIL import Image,ImageTk


menu=customtkinter.CTk()
menu.title("Declaration annuelle")
menu.geometry("1400x900+200+50")
menu.resizable(False,False)
menu.configure(background="#190924")

##heading
lbltitle=customtkinter.CTkLabel(menu,text="Declarations annuelles ",width=1400,height=60,corner_radius=8,
                                fg_color="#0f4859",text_color="white",text_font=("Cambria",20))

lbltitle.grid()
def returnn():
    menu.destroy()
    call(["python","choix.py"])
btnreturn=customtkinter.CTkButton(text_font=("Cambria",15),master=lbltitle,height=40,width=10,fg_color="black",hover_color='#6a74f7',corner_radius=10,text="retour",command=returnn)
btnreturn.place(x=15, y=8)


frame = customtkinter.CTkFrame(menu,
fg_color="#0a2742",width=500,height=810, corner_radius=20)
frame.place(x=20,y=70)
frametitle = customtkinter.CTkFrame(frame,fg_color="#004e69",width=280,height=50, corner_radius=10)
frametitle.place(x=110,y=10)
label_title=Label(frametitle,text="   Formulaire :",font=("Cambria",18),bg="#004e69",fg="white")
label_title.place(x=58,y=10)
frame3 = customtkinter.CTkFrame(menu,fg_color="#363c42",width=860,height=810, corner_radius=20)
frame3.place(x=530,y=70)


frame2=customtkinter.CTkFrame(master=frame,width=450,height=700,corner_radius=20,fg_color='#3D3C42')
frame2.place(x=20,y=80)
framee= customtkinter.CTkFrame(frame2,width=352, height=5, corner_radius=40,fg_color="grey")
framee.place(x=40, y=94)
frameline= customtkinter.CTkFrame(frame2,width=450, height=5, corner_radius=40,fg_color="#476b6b")
frameline.place(x=0, y=316)
frameline2= customtkinter.CTkFrame(frame2,width=450, height=5, corner_radius=40,fg_color="#476b6b")
frameline2.place(x=0, y=450)

frame13 = customtkinter.CTkFrame(frame3,fg_color="white",width=860,height=540, corner_radius=20)
frame13.place(x=0,y=70)

frame4=customtkinter.CTkFrame(frame3,fg_color="#004e69",width=840,height=50, corner_radius=20)
frame4.place(x=10,y=10)

labell= customtkinter.CTkLabel(frame4,text="Tableau des Declarations :",width=10,height=25,
text_font=("Cambria",20),corner_radius=8)
labell.place(x=250, y=10)
#####formulaire_donnees:
label1= customtkinter.CTkLabel(frame2,text="ID :",width=10,height=25,
text_font=("Cambria",18),corner_radius=8)

label1.place(x=10, y=15)
id=customtkinter.CTkEntry(text_font=("Cambria",19),master=frame2,height=36,width=250,border_width=0,placeholder_text="ID unique ",corner_radius=8,fg_color="grey")
id.place(x=140, y=10)

label2= customtkinter.CTkLabel(frame2,text="Denomination/Raison Sociale :",width=80,height=5,text_font=("Cambria",20),corner_radius=8,text_color="white")
label2.place(x=30, y=60)


denomination=customtkinter.CTkEntry(text_font=("ARIAL BOLD",18),master=frame2,height=36,width=450,border_width=0,placeholder_text="Obligatoire",corner_radius=2,fg_color="#8fe0f0",text_color="#295c7a",justify='center')
denomination.place(x=0, y=120)





label4= customtkinter.CTkLabel(frame2,text="  Bilan :",width=80,height=15,text_font=("Cambria",19),corner_radius=8)
label4.place(x=0, y=163)
bilan =StringVar()
def radiobutton_event1():
     print(bilan.get())
     if (bilan.get()=="NON"):
        switch_2.configure(state="disabled")
        switch_2.configure(fg_color="black",button_color="grey")
     else:
        switch_2.configure(state="standard",fg_color="white",button_color="cyan")
radiobutton_1 = customtkinter.CTkRadioButton(master=frame2, text="Oui",command=radiobutton_event1, variable=bilan, value="Oui",height=20,width=20,hover_color="#b2b2d9",fg_color="#7576bd",text_color="#b5b5b2",text_font=("cambria",12))
radiobutton_2 = customtkinter.CTkRadioButton(master=frame2, text="Non",command=radiobutton_event1, variable=bilan, value="Non",height=20,width=20,hover_color="#b2b2d9",fg_color="#7576bd",text_color="#b5b5b2",text_font=("cambria",12))

radiobutton_1.place(x=150,y=170)
radiobutton_2.place(x=250,y=170)



label5= customtkinter.CTkLabel(frame2,text="Etat 9421:",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label5.place(x=10, y=200)
etat9421 =StringVar()
def radiobutton_event2():
     print(etat9421.get())


radiobutton_3 = customtkinter.CTkRadioButton(master=frame2, text="Oui",command=radiobutton_event2, variable= etat9421, value="Oui",height=20,width=20,hover_color="#b2b2d9",fg_color="#7576bd",text_color="#b5b5b2",text_font=("cambria",12))
radiobutton_4 = customtkinter.CTkRadioButton(master=frame2, text="Non",command=radiobutton_event2, variable= etat9421, value="Non",height=20,width=20,hover_color="#b2b2d9",fg_color="#7576bd",text_color="#b5b5b2",text_font=("cambria",12))

radiobutton_3.place(x=150,y=210)
radiobutton_4.place(x=250,y=210)



label6= customtkinter.CTkLabel(frame2,text="PV AGO:",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label6.place(x=10, y=240)

pvago =StringVar(value="Non")
def switch_event():
     print(pvago.get())

switch_1 = customtkinter.CTkSwitch(master=frame2, text="", command=switch_event,width=50,height=25,fg_color="white",button_hover_color="#6d6dab",text_font="arial",button_color="cyan",
                       variable=pvago, onvalue="Oui", offvalue="Non")
switch_1.place(x=150, y=245)



label7= customtkinter.CTkLabel(frame2,text="IS:",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label7.place(x=0, y=280)

iss = customtkinter.StringVar(value="Non")
def switch2_event():
    print(iss.get())


switch_2 = customtkinter.CTkSwitch(master=frame2, text="", command=switch2_event, width=50, height=25, fg_color="white",button_color="cyan",
                                   button_hover_color="#6d6dab", text_font="arial",
                                   variable=iss, onvalue="Oui", offvalue="Non")
switch_2.place(x=150, y=280)


label8= customtkinter.CTkLabel(frame2,text="Declar. des immobilisations :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label8.place(x=10, y=320)

d_immob = customtkinter.StringVar(value="Non")
def switch3_event():
    print(d_immob.get())

switch_3 = customtkinter.CTkSwitch(master=frame2, text="", command=switch3_event, width=50, height=25, fg_color="white",
                                   button_hover_color="#6d6dab", text_font="arial",
                                   variable=d_immob, onvalue="Oui", offvalue="Non")
switch_3.place(x=360, y=330)

label9= customtkinter.CTkLabel(frame2,text="Declar. des Gazoiles :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label9.place(x=10, y=350)

d_gaz = customtkinter.StringVar(value="Non")
def switch4_event():
    print(d_gaz.get())


switch_4 = customtkinter.CTkSwitch(master=frame2, text="", command=switch4_event, width=50, height=25, fg_color="white",
                                   button_hover_color="#6d6dab", text_font="arial",
                                   variable=d_gaz, onvalue="Oui", offvalue="Non")
switch_4.place(x=360, y=360)



label10= customtkinter.CTkLabel(frame2,text="Declar. des honoraires :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label10.place(x=10, y=380)

d_honor = customtkinter.StringVar(value="Non")
def switch5_event():
    print(d_honor.get())


switch_5 = customtkinter.CTkSwitch(master=frame2, text="", command=switch5_event, width=50, height=25, fg_color="white",
                                   button_hover_color="#6d6dab", text_font="arial",
                                   variable=d_honor, onvalue="Oui", offvalue="Non")
switch_5.place(x=360, y=390)









label11= customtkinter.CTkLabel(frame2,text="Cotisation min :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label11.place(x=10, y=413)

cm = customtkinter.StringVar(value="Non")
def switch6_event():
    print(cm.get())


switch_6 = customtkinter.CTkSwitch(master=frame2, text="", command=switch6_event, width=50, height=25, fg_color="white",
                                   button_hover_color="#6d6dab", text_font="arial",
                                   variable=cm, onvalue="Oui", offvalue="Non")
switch_6.place(x=360, y=419)


label88= customtkinter.CTkLabel(frame2,text="Date :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label88.place(x=10, y=470)
date=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=200,border_width=0,placeholder_text="format: YY-MM-DD",corner_radius=8,fg_color="grey")
date.place(x=140, y=470)

#style treevi
style=ttk.Style()

style.theme_use("vista")
style.configure("Treeview",foreground="black",background="white",borderwidth=0,rowheight=39)

style.map('Treeview',background=[('selected','#2A0944')])


###treeview

PatrolView=ttk.Treeview(frame3,style="Treeview")
PatrolView['columns']=(1,2,3,4,5,6,7,8,9,10,11)
PatrolView.place(x=30,y=90,width=820,height=500)
PatrolView.column("#0",width=0)
PatrolView.column(1,width=30,anchor=CENTER)
PatrolView.column(2,width=80,anchor=CENTER)
PatrolView.column(3,width=60,anchor=CENTER)
PatrolView.column(4,width=50,anchor=CENTER)
PatrolView.column(5,width=50,anchor=CENTER)
PatrolView.column(6,width=40,anchor=CENTER)
PatrolView.column(7,width=95,anchor=CENTER)
PatrolView.column(8,width=70,anchor=CENTER)
PatrolView.column(9,width=90,anchor=CENTER)
PatrolView.column(10,width=50,anchor=CENTER)
PatrolView.column(11,width=70,anchor=CENTER)




PatrolView.heading(1,text="ID",anchor=CENTER)
PatrolView.heading(2,text="Denomination",anchor=CENTER)
PatrolView.heading(3,text="Bilan",anchor=CENTER)
PatrolView.heading(4,text="etat 9421",anchor=CENTER)
PatrolView.heading(5,text="PV AGO",anchor=CENTER)
PatrolView.heading(6,text="IS",anchor=CENTER)
PatrolView.heading(7,text="D.immobilisations",anchor=CENTER)
PatrolView.heading(8,text="D.Gazoile",anchor=CENTER)
PatrolView.heading(9,text="D.honoraires",anchor=CENTER)
PatrolView.heading(10,text="C.M",anchor=CENTER)
PatrolView.heading(11,text="Date",anchor=CENTER)

yscrollbar=ttk.Scrollbar(frame13,orient="vertical",command=PatrolView.yview)
yscrollbar.place(x=10, y=20, height=500)
PatrolView.configure(yscrollcommand=yscrollbar.set)




###connexion base
mabase=mysql.connector.connect(host="localhost",user="root",password="",database="cgb_database")
####afffichage
meconnect=mabase.cursor()
meconnect.execute("select * from declaration_annuelle order by date desc ")
for row in meconnect:
    PatrolView.insert('',END,value=row)
mabase.close()





###modifier
def modifier():


        if (id.get() == "" or denomination.get() == ""):
              messagebox.showwarning("Erreur", "selectionez une declaration a modifier")
        else:
            a = messagebox.askokcancel("Confirmation", "vous etes sures de modifier cette declaration ?")

            if (a == True):
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='cgb_database')
                cur = conn.cursor()
                Denomination = str(denomination.get())
                Id = str(id.get())
                Bilan = str(bilan.get())
                etat_9421 = str(etat9421.get())
                pv_ago = str(pvago.get())
                i_s = str(iss.get())
                dec_imm = str(d_immob.get())
                dec_gaz = str(d_gaz.get())
                dec_hono = str(d_honor.get())
                c_m = str(cm.get())
                datee = date.get()

            try:

                sql1="UPDATE declaration_annuelle set `denomination`=%s,`bilan`=%s,`etat_9421`=%s,`pv_ago`=%s,`i_s`=%s,`d_immobilisations`=%s,`d_gaz`=%s,`d_honoraires`=%s,`c_m`=%s,`date`=%s WHERE ID=%s"

                val2 =(Denomination,Bilan,etat_9421,pv_ago,i_s,dec_imm,dec_gaz,dec_hono,c_m,datee,Id)
                cur.execute(sql1,val2)
                conn.commit()
                dernier = cur.lastrowid
                messagebox.showinfo("resultat","Modification faite avec Success !")
                menu.destroy()
                call(["python", "declaration_annuelle.py"])

            except Exception as e:
             print(e)

##ajout
def ajouter():
    if (id.get() == "" or denomination.get() == "" ):
        messagebox.showwarning("Erreur", "Veuillez remplir l'Identifiant,la Denomination!")
    else:
        Denomination = denomination.get()
        Id = id.get()
        Bilan =bilan.get()
        etat_9421 = etat9421.get()
        pv_ago = pvago.get()
        i_s = iss.get()
        dec_imm = d_immob.get()
        dec_gaz = str(d_gaz.get())
        dec_hono = str(d_honor.get())
        c_m = str(cm.get())
        Date = str(date.get())

    mabase = mysql.connector.connect(host="localhost", user="root", password="", database="cgb_database")
    meconnect = mabase.cursor()

    try:
        sql="INSERT into declaration_annuelle VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(Id,Denomination,Bilan,etat_9421,pv_ago,i_s,dec_imm,dec_gaz,dec_hono,c_m,Date)
        meconnect.execute(sql , val)
        mabase.commit()
        dernier=meconnect.lastrowid
        messagebox.showinfo("Ajout","ajout avec succes")
        menu.destroy()
        call(["python","declaration_annuelle.py"])



    except Exception as e:
        print(e)
        mabase.rollback()
        mabase.close()


framse= customtkinter.CTkFrame(frame2,width=430, height=140, corner_radius=32,fg_color="#8fe0f0")
framse.place(x=10, y=540)
frameee=customtkinter.CTkFrame(framse,width=5, height=140, corner_radius=40,fg_color="#7aadc2")
frameee.place(x=215, y=0)
frameeee=customtkinter.CTkFrame(framse,width=5, height=140, corner_radius=40,fg_color="#7aadc2")
frameeee.place(x=220, y=0)









###clear
def clear():
    id.delete(0, END)
    denomination.delete(0, END)
    bilan.set("")
    etat9421.set("")
    pvago.set("Non")
    iss.set("Non")
    d_immob.set("Non")
    d_gaz.set("Non")
    d_honor.set("Non")
    cm.set("Non")
    date.delete(0, END)

###collectfrom treeview

def collect(e):
    id.delete(0, END)
    denomination.delete(0, END)
    bilan.set("")
    etat9421.set("")
    pvago.set("Non")
    iss.set("Non")
    d_immob.set("Non")
    d_gaz.set("Non")
    d_honor.set("Non")
    cm.set("Non")
    date.delete(0, END)


    selected=PatrolView.focus()
    temp=PatrolView.item(selected,'values')

    id.insert(END, temp[0])
    denomination.insert(END, temp[1])
    bilan.set(temp[2])
    etat9421.set(temp[3])
    pvago.set(temp[4])
    iss.set(temp[5])
    d_immob.set(temp[6])
    d_gaz.set(temp[7])
    d_honor.set(temp[8])
    cm.set(temp[9])
    date.insert(END, temp[10])

PatrolView.bind("<ButtonRelease-1>",collect)

def supprimer():
    if (id.get() == "" or denomination.get() == ""):
        messagebox.showwarning("Erreur", "selectionez une declaration a supprimer")
    else:
        a=messagebox.askokcancel("Confirmation","vous etes sures de supprimer cette declaration ?")

        if (a == True):
            Denomination = denomination.get()
            Id = id.get()
            Bilan = bilan.get()
            etat_9421 = etat9421.get()
            pv_ago = pvago.get()
            i_s = iss.get()
            dec_imm = d_immob.get()
            dec_gaz = str(d_gaz.get())
            dec_hono = str(d_honor.get())
            c_m = str(cm.get())
            Date = str(date.get())


            conn = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='',
                                   database='cgb_database')
            con = conn.cursor()
            try:
                sql = "DELETE FROM declaration_annuelle WHERE Id=%s"
                val = (Id,)
                con.execute(sql, val)
                conn.commit()
                dernierid = con.lastrowid
                messagebox.showinfo("information", "declaration supprimee avec success !")
                menu.destroy()
                call(["python", "declaration_annuelle.py"])

            except Exception as e:
                print(e)


####iconeimage:

img= (Image.open("add.png"))
resized_image= img.resize((35,35), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

img2= (Image.open("edit.png"))
resized_image2= img2.resize((35,35), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)


img3= (Image.open("delete.png"))
resized_image3= img3.resize((35,35), Image.ANTIALIAS)
new_image3= ImageTk.PhotoImage(resized_image3)

img4= (Image.open("clear.png"))
resized_image4= img4.resize((30,30), Image.ANTIALIAS)
new_image4= ImageTk.PhotoImage(resized_image4)

btnajouter=customtkinter.CTkButton(text=" Ajouter ",text_font=("Cambria",23),master=framse,image=new_image,height=50,width=150,border_width=0,corner_radius=10,fg_color="#004e69",hover_color="#0099CC",command=ajouter)
btnajouter.place(x=235, y=10)

btnmodifier=customtkinter.CTkButton(text_font=("Cambria",22),image=new_image2,master=framse,width=150,height=50,border_width=0,fg_color='#666633',hover_color="#828241",corner_radius=8,text=" Modifier ",command=modifier)
btnmodifier.place(x=235, y=80)

btndel=customtkinter.CTkButton(text_font=("Cambria",22),image=new_image3,master=framse,width=100,height=50,border_width=0,fg_color="#780707",hover_color="#f51b1b",corner_radius=8,text="Supprimer",command=supprimer)
btndel.place(x=15, y=10)

btnclear=customtkinter.CTkButton(text_font=("Cambria",25),image=new_image4,master=framse,width=150,height=50,border_width=0,fg_color='#2b0202',hover_color="#962727",corner_radius=8,text=" Clear all ",command=clear)
btnclear.place(x=15, y=80)
menu.mainloop()