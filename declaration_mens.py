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
menu.title("Declaration mensuelle")
menu.geometry("1400x900+200+50")
menu.resizable(False,False)
menu.configure(background="#190924")

##heading
lbltitle=customtkinter.CTkLabel(menu,text="Declarations mensuelles ",width=1400,height=60,corner_radius=8,
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

label7= customtkinter.CTkLabel(frame2,text="TVA trimistrielle :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label7.place(x=10, y=310)

switch2_var = customtkinter.StringVar(value="mensuelle")
def switch2_event():
    print(switch2_var.get())


switch_2 = customtkinter.CTkSwitch(master=frame2, text="", command=switch2_event, width=50, height=25, fg_color="white",
                                   button_hover_color="#6d6dab", text_font="arial",
                                   variable=switch2_var, onvalue="trimistrielle", offvalue="mensuelle")
switch_2.place(x=340, y=320)




label4= customtkinter.CTkLabel(frame2,text="  TVA :",width=80,height=15,text_font=("Cambria",19),corner_radius=8)
label4.place(x=0, y=163)
radio_var =StringVar()
def radiobutton_event():
     print(radio_var.get())
     if (radio_var.get()=="NON"):
        switch_2.configure(state="disabled")
        switch_2.configure(fg_color="black",button_color="grey")
     else:
        switch_2.configure(state="standard",fg_color="white")
radiobutton_1 = customtkinter.CTkRadioButton(master=frame2, text="OUI",command=radiobutton_event, variable= radio_var, value="OUI",height=20,width=20,hover_color="#b2b2d9",fg_color="#7576bd",text_color="#b5b5b2",text_font=("cambria",12))
radiobutton_2 = customtkinter.CTkRadioButton(master=frame2, text="NON",command=radiobutton_event, variable= radio_var, value="NON",height=20,width=20,hover_color="#b2b2d9",fg_color="#7576bd",text_color="#b5b5b2",text_font=("cambria",12))

radiobutton_1.place(x=140,y=170)
radiobutton_2.place(x=240,y=170)



label5= customtkinter.CTkLabel(frame2,text="CNSS :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label5.place(x=10, y=210)
radio_var2 =StringVar()
def radiobutton_event2():
     print(radio_var2.get())


radiobutton_3 = customtkinter.CTkRadioButton(master=frame2, text="OUI",command=radiobutton_event2, variable= radio_var2, value="OUI",height=20,width=20,hover_color="#b2b2d9",fg_color="#7576bd",text_color="#b5b5b2",text_font=("cambria",12))
radiobutton_4 = customtkinter.CTkRadioButton(master=frame2, text="NON",command=radiobutton_event2, variable= radio_var2, value="NON",height=20,width=20,hover_color="#b2b2d9",fg_color="#7576bd",text_color="#b5b5b2",text_font=("cambria",12))

radiobutton_3.place(x=140,y=220)
radiobutton_4.place(x=240,y=220)



label6= customtkinter.CTkLabel(frame2,text="Declaration trimistrielle :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label6.place(x=10, y=260)
switch_var =StringVar(value="mensuelle")

def switch_event():
     print(switch_var.get())

switch_1 = customtkinter.CTkSwitch(master=frame2, text="", command=switch_event,width=50,height=25,fg_color="white",button_hover_color="#6d6dab",text_font="arial",
                       variable=switch_var, onvalue="trimistrielle", offvalue="mensuelle")
switch_1.place(x=340, y=268)







label8= customtkinter.CTkLabel(frame2,text="Date :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label8.place(x=10, y=370)
annee=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=200,border_width=0,placeholder_text="format: YY-MM-DD",corner_radius=8,fg_color="grey")
annee.place(x=140, y=370)
#style treevi
style=ttk.Style()

style.theme_use("vista")
style.configure("Treeview",foreground="black",background="white",borderwidth=0,rowheight=39)

style.map('Treeview',background=[('selected','#2A0944')])


###treeview

PatrolView=ttk.Treeview(frame3,style="Treeview")
PatrolView['columns']=(1,2,3,4,5,6,7)
PatrolView.place(x=30,y=90,width=820,height=500)
PatrolView.column("#0",width=0)
PatrolView.column(1,width=30,anchor=CENTER)
PatrolView.column(2,width=110,anchor=CENTER)
PatrolView.column(3,width=100,anchor=CENTER)
PatrolView.column(4,width=50,anchor=CENTER)
PatrolView.column(5,width=50,anchor=CENTER)
PatrolView.column(6,width=50,anchor=CENTER)
PatrolView.column(7,width=50,anchor=CENTER)


PatrolView.heading(1,text="ID",anchor=CENTER)
PatrolView.heading(2,text="Denomination",anchor=CENTER)
PatrolView.heading(3,text="Type de Declaration",anchor=CENTER)
PatrolView.heading(4,text="TVA",anchor=CENTER)
PatrolView.heading(5,text="Type de TVA",anchor=CENTER)
PatrolView.heading(6,text="CNSS",anchor=CENTER)
PatrolView.heading(7,text="Date",anchor=CENTER)


yscrollbar=ttk.Scrollbar(frame13,orient="vertical",command=PatrolView.yview)
yscrollbar.place(x=10, y=20, height=500)
PatrolView.configure(yscrollcommand=yscrollbar.set)




###connexion base
mabase=mysql.connector.connect(host="localhost",user="root",password="",database="cgb_database")
####afffichage
meconnect=mabase.cursor()
meconnect.execute("select * from declaration_mensuelle order by Date desc ")
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
                type_declaration = str(switch_var.get())
                tva = str(radio_var.get())
                type_tva = str(switch2_var.get())
                cnss = str(radio_var2.get())
                Annee = str(annee.get())

            try:

                sql1="UPDATE declaration_mensuelle set `Denomination`=%s,`type_declaration`=%s,`tva`=%s,`type_de_tva`=%s,`cnss`=%s,`Date`=%s WHERE ID=%s"

                val2 =(Denomination,type_declaration,tva,type_tva,cnss,Annee,Id)
                cur.execute(sql1,val2)
                conn.commit()
                dernier = cur.lastrowid
                messagebox.showinfo("resultat","Modification faite avec Success !")
                menu.destroy()
                call(["python", "declaration_mens.py"])

            except Exception as e:
             print(e)

##ajout
def ajouter():
    if (id.get() == "" or denomination.get() == "" ):
        messagebox.showwarning("Erreur", "Veuillez remplir l'Identifiant,la Denomination!")
    else:
     Id=id.get()
     Denomination=denomination.get()
     type_declaration=switch_var.get()
     tva=radio_var.get()
     type_tva=switch2_var.get()
     cnss=radio_var2.get()
     Annee=annee.get()

    mabase = mysql.connector.connect(host="localhost", user="root", password="", database="cgb_database")
    meconnect = mabase.cursor()

    try:
        sql="INSERT into declaration_mensuelle (ID,denomination,type_declaration,tva,type_de_tva,cnss,Date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val=(Id,Denomination,type_declaration,tva,type_tva,cnss,Annee)
        meconnect.execute(sql , val)
        mabase.commit()
        dernier=meconnect.lastrowid
        messagebox.showinfo("Ajout","ajout avec succes")
        menu.destroy()
        call(["python","declaration_mens.py"])



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
    radio_var.set("")
    radio_var2.set("")
    switch_var.set("mensuelle")
    switch2_var.set("mensuelle")
    annee.delete(0, END)

###collectfrom treeview

def collect(e):
    id.delete(0,END)
    denomination.delete(0, END)
    radio_var.set("")
    radio_var2.set("")
    switch_var.set("")
    switch2_var.set("")
    annee.delete(0, END)

    selected=PatrolView.focus()
    temp=PatrolView.item(selected,'values')
    print("hi",temp)
    id.insert(END, temp[0])
    denomination.insert(END, temp[1])
    radio_var.set(temp[3])
    radio_var2.set(temp[5])
    switch_var.set(temp[2])
    switch2_var.set(temp[4])
    annee.insert(END, temp[6])



PatrolView.bind("<ButtonRelease-1>",collect)

def supprimer():
    if (id.get() == "" or denomination.get() == ""):
        messagebox.showwarning("Erreur", "selectionez une declaration a supprimer")
    else:
        a=messagebox.askokcancel("Confirmation","vous etes sures de supprimer cette declaration ?")

        if (a == True):
            Id = id.get()
            Denomination = denomination.get()
            tva = radio_var.get()
            cnss = radio_var2.get()
            decla_trim = switch_var.get()
            tva_trim= switch2_var.get()
            Annee = annee.get()


            conn = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='',
                                   database='cgb_database')
            con = conn.cursor()
            try:
                sql = "DELETE FROM declaration_mensuelle WHERE id=%s"
                val = (Id,)
                con.execute(sql, val)
                conn.commit()
                dernierid = con.lastrowid
                messagebox.showinfo("information", "declaration supprimee avec success !")
                menu.destroy()
                call(["python", "declaration_mens.py"])

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

btnclear=customtkinter.CTkButton(text_font=("Cambria",25),image=new_image4,master=framse,width=150,height=50,border_width=0,fg_color='#2b0202',hover_color="#962727",corner_radius=8,text=" Clear all  ",command=clear)
btnclear.place(x=15, y=80)
menu.mainloop()