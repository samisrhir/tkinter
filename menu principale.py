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
menu.title("menu principale")
menu.geometry("1400x900+200+50")
menu.resizable(False,False)
menu.configure(background="#190924")

##heading
lbltitle=customtkinter.CTkLabel(menu,text="Les Identifications  ",width=1400,height=60,corner_radius=8,
                                fg_color="#0f4859",text_color="white",text_font=("Cambria",20))
lbltitle.grid()

##retour
def returnn():
    menu.destroy()
    call(["python","choix.py"])

btnreturn=customtkinter.CTkButton(text_font=("Cambria",15),master=lbltitle,height=40,width=10,fg_color="black",hover_color='#6a74f7',corner_radius=10,text="retour",command=returnn)
btnreturn.place(x=15, y=8)



frame = customtkinter.CTkFrame(menu,fg_color="#0a2742",width=500,height=810, corner_radius=20)
frame.place(x=20,y=70)
frametitle = customtkinter.CTkFrame(frame,fg_color="#004e69",width=280,height=50, corner_radius=10)
frametitle.place(x=110,y=10)
label_title=Label(frametitle,text="    Formulaire :",font=("Cambria",18),bg="#004e69",fg="white")
label_title.place(x=55,y=10)
frame3 = customtkinter.CTkFrame(menu,fg_color="#38373d",width=860,height=810, corner_radius=20)
frame3.place(x=530,y=70)

frame13 = customtkinter.CTkFrame(frame3,fg_color="white",width=860,height=540, corner_radius=20)
frame13.place(x=0,y=70)

frame4=customtkinter.CTkFrame(frame3,fg_color="#004e69",width=840,height=50, corner_radius=20)
frame4.place(x=10,y=10)

labell= customtkinter.CTkLabel(frame4,text="Tableau des Identifications :",width=10,height=25,
text_font=("Cambria",20),corner_radius=8)
labell.place(x=250, y=10)


frame2=customtkinter.CTkFrame(master=frame,width=450,height=700,corner_radius=20,fg_color='#3D3C42')
frame2.place(x=20,y=70)

frame= customtkinter.CTkFrame(frame2,width=352, height=5, corner_radius=40,fg_color="#555250")
frame.place(x=40, y=94)

framse= customtkinter.CTkFrame(frame2,width=430, height=140, corner_radius=32,fg_color="#8fe0f0")
framse.place(x=10, y=540)
frameee=customtkinter.CTkFrame(framse,width=5, height=140, corner_radius=40,fg_color="#7aadc2")
frameee.place(x=215, y=0)
frameeee=customtkinter.CTkFrame(framse,width=5, height=140, corner_radius=40,fg_color="#7aadc2")
frameeee.place(x=220, y=0)
#CLIENT_label///client_entry
label1= customtkinter.CTkLabel(frame2,text="ID :",width=10,height=25,
text_font=("Cambria",18),corner_radius=8)

label1.place(x=10, y=15)
id=customtkinter.CTkEntry(text_font=("Cambria",19),master=frame2,height=36,width=250,border_width=0,placeholder_text="ID unique ",corner_radius=8,fg_color="grey")
id.place(x=140, y=10)


label2= customtkinter.CTkLabel(frame2,text="Denomination/Raison Sociale :",width=80,height=5,text_font=("Cambria",20),corner_radius=8,text_color="#2683d4")
label2.place(x=30, y=60)


denomination=customtkinter.CTkEntry(text_font=("ARIAL BOLD",18),master=frame2,height=36,width=450,border_width=0,placeholder_text="Obligatoire",text_color="#295c7a",corner_radius=2,fg_color="#8fe0f0",justify='center')
denomination.place(x=0, y=110)


label4= customtkinter.CTkLabel(frame2,text="TP :",width=80,height=15,text_font=("Cambria",19),corner_radius=8)
label4.place(x=0, y=163)
TP=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=250,border_width=0,placeholder_text="Taxe Professionelle",corner_radius=8,fg_color="grey")
TP.place(x=140, y=160)

label5= customtkinter.CTkLabel(frame2,text="N° RC :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label5.place(x=10, y=210)
RC=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=250,border_width=0,placeholder_text="N° registre de commerce",corner_radius=8,fg_color="grey")
RC.place(x=140, y=210)

label6= customtkinter.CTkLabel(frame2,text="N° CNSS :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label6.place(x=10, y=260)
num_cnss=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=250,border_width=0,placeholder_text="Numero CNSS",corner_radius=8,fg_color="grey")
num_cnss.place(x=140, y=260)


label3= customtkinter.CTkLabel(frame2,text="IF :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label3.place(x=0, y=310)
iff=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=250,border_width=0,placeholder_text="Identifiant Fiscal",corner_radius=8,fg_color="grey")
iff.place(x=140, y=310)



label8= customtkinter.CTkLabel(frame2,text="ICE :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label8.place(x=10, y=360)
email=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=250,border_width=0,placeholder_text="Id. commun des entreprise",corner_radius=8,fg_color="grey")
email.place(x=140, y=358)


label7= customtkinter.CTkLabel(frame2,text="Contact :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label7.place(x=10, y=405)
tel=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=250,border_width=0,placeholder_text="tele/email",corner_radius=8,fg_color="grey")
tel.place(x=140, y=405)

label9= customtkinter.CTkLabel(frame2,text="Date :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
label9.place(x=10, y=454)
annee=customtkinter.CTkEntry(text_font=("Cambria",15),master=frame2,height=36,width=250,border_width=0,placeholder_text="format :YY-MM-DD",corner_radius=8,fg_color="grey")
annee.place(x=140, y=454)
###combogender=customtkinter.StringVar(value="SERVICE")
##def combobox_callback(choice):
  ##  print(choice)

##combobox = customtkinter.CTkComboBox(frame2,values=["Assistance","Creation d'entreprise", "Conseille Juridiques"],
    ##                            command=combobox_callback,
    ##                           width=250,height=35,
##                               fg_color="#036b9c",
    ##                                  button_hover_color="#4fb1b8",
##dropdown_color="#4fb1b8",
##                         text_font=("Cambria",15),
##                         text_color="white")
##combobox.place(x=140, y=260)
######CHECKBOX------------
##var1=StringVar()

##def checkbox_event():
## print(var1.get())

##checkbox = customtkinter.CTkCheckBox(master=frame2, text="PAYMENT", command=checkbox_event,
##             variable=var1, onvalue="yes", offvalue="no")
##checkbox.place(x=140, y=320)


##var2=StringVar()

##def checkbox_eventt():
    ##   print(var2.get())

##checkbox = customtkinter.CTkCheckBox(master=frame2, text="PAYPAL", command=checkbox_eventt,
    ##                               variable=var2, onvalue="yes", offvalue="no")
##checkbox.place(x=250, y=320)



#-------radio-------------

##label6= customtkinter.CTkLabel(frame2,text="choix :",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
##label6.place(x=0, y=360)
##radio_var =StringVar()
##def radiobutton_event():
    ## print(radio_var.get())

##radiobutton_1 = customtkinter.CTkRadioButton(master=frame2, text="Option 3",command=radiobutton_event, variable= radio_var, value="faux",height=20,width=20,fg_color="green",text_font=("cambria",12))
##radiobutton_2 = customtkinter.CTkRadioButton(master=frame2, text="Option 2",command=radiobutton_event, variable= radio_var, value="vraie",height=20,width=20,fg_color="green",text_font=("cambria",12))
##radiobutton_3 = customtkinter.CTkRadioButton(master=frame2, text="Option 1",command=radiobutton_event, variable= radio_var, value="rien",height=20,width=20,fg_color="green",text_font=("cambria",12))

##radiobutton_1.place(x=300,y=370)
##radiobutton_2.place(x=210,y=370)
##radiobutton_3.place(x=120,y=370)



##slider = customtkinter.CTkSlider(master=frame2, from_=0, to=100, command=slider_event)
##slider.place(x=130, y=500)
###switchbar##########
##label7= customtkinter.CTkLabel(frame2,text="type:",width=80,height=5,text_font=("Cambria",20),corner_radius=8)
##label7.place(x=0, y=400)

##switch_var = customtkinter.StringVar(value="on")

##def switch_event():
    ## print(switch_var.get())

##switch_1 = customtkinter.CTkSwitch(master=frame2, text="Credit", command=switch_event,width=40,height=20,fg_color="black",button_hover_color="green",text_font="arial",
    ##                     variable=switch_var, onvalue="oui", offvalue="non",button_color="blue")
##switch_1.place(x=130, y=410)
##########bbtns

###treeview


style=ttk.Style()

style.theme_use("vista")
style.configure("Treeview",foreground="black",background="white",borderwidth=0,rowheight=39)

style.map('Treeview',background=[('selected','#2A0944')])



PatrolView=ttk.Treeview(frame3,style="Treeview")
PatrolView['columns']=(1,2,3,4,5,6,7,8,9)
PatrolView.place(x=30,y=90,width=820,height=500)
PatrolView.column("#0",width=0)
PatrolView.column(1,width=30,anchor=CENTER)
PatrolView.column(2,width=110,anchor=CENTER)
PatrolView.column(3,width=50,anchor=CENTER)
PatrolView.column(4,width=50,anchor=CENTER)
PatrolView.column(5,width=50,anchor=CENTER)
PatrolView.column(6,width=50,anchor=CENTER)
PatrolView.column(7,width=120,anchor=CENTER)
PatrolView.column(8,width=50,anchor=CENTER)
PatrolView.column(9,width=50,anchor=CENTER)


PatrolView.heading(1,text="ID",anchor=CENTER)
PatrolView.heading(2,text="Denomination",anchor=CENTER)
PatrolView.heading(3,text="TP",anchor=CENTER)
PatrolView.heading(4,text="N° RC",anchor=CENTER)
PatrolView.heading(5,text="N° CNSS",anchor=CENTER)
PatrolView.heading(6,text="IF",anchor=CENTER)
PatrolView.heading(7,text="ICE",anchor=CENTER)
PatrolView.heading(8,text="Contact",anchor=CENTER)
PatrolView.heading(9,text="Date",anchor=CENTER)

yscrollbar=ttk.Scrollbar(frame13,orient="vertical",command=PatrolView.yview)
yscrollbar.place(x=10, y=20, height=500)
PatrolView.configure(yscrollcommand=yscrollbar.set)











###connexion base
mabase=mysql.connector.connect(host="localhost",user="root",password="",database="cgb_database")
####afffichage
meconnect=mabase.cursor()
meconnect.execute("select * from identification order by Date desc ")
for row in meconnect:
    PatrolView.insert('',END,value=row)
mabase.close()

###modifier
def modifier():


        if (id.get() == "" or denomination.get() == ""):
              messagebox.showwarning("Erreur", "selectionez une identification a modifier")
        else:
            a = messagebox.askokcancel("Confirmation", "vous etes sures de modifier cet identifcation ?")

            if (a == True):
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='cgb_database')
                cur = conn.cursor()
                Id = str(id.get())
                Denomination = str(denomination.get())
                Tp = str(TP.get())
                nRC = str(RC.get())
                Ncnss = str(num_cnss.get())
                Iff = str(iff.get())
                Email = str(email.get())
                Tele = str(tel.get())
                Annee = str(annee.get())

            try:

                sql1="UPDATE identification set `Denomination`=%s,`TP`=%s,`N° RC`=%s,`N° CNSS`=%s,`IF`=%s,`Date`=%s,`ice`=%s,`Date`=%s WHERE ID=%s"

                val2 =(Denomination,Tp,nRC,Ncnss,Iff,Email,Tele,Annee,Id)

                cur.execute(sql1,val2)
                conn.commit()
                dernier = cur.lastrowid
                messagebox.showinfo("resultat","Modification faite avec Success !")
                menu.destroy()
                call(["python", "menu principale.py"])

            except Exception as e:
             print(e)




###clear
def clear():
    id.delete(0, END)
    denomination.delete(0, END)
    TP.delete(0, END)
    RC.delete(0, END)
    num_cnss.delete(0, END)
    iff.delete(0, END)
    email.delete(0, END)
    tel.delete(0, END)
    annee.delete(0, END)
####ajouter
def ajouter():
    if (id.get() == "" or denomination.get() == "" or annee.get() == ""):
        messagebox.showwarning("Erreur", "Veuillez remplir l'Identifiant,Denomination et l'annee !")
    else:
     Id=id.get()
     Denomination=denomination.get()
     Tp=TP.get()
     nRC=RC.get()
     Ncnss=num_cnss.get()
     Iff=iff.get()
     Email=email.get()
     Tele=tel.get()
     Annee=annee.get()

    mabase = mysql.connector.connect(host="localhost", user="root", password="", database="cgb_database")
    meconnect = mabase.cursor()

    try:
        sql="INSERT into identification VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(Id,Denomination,Tp,nRC,Ncnss,Iff,Email,Tele,Annee)
        meconnect.execute(sql,val)
        mabase.commit()
        dernier=meconnect.lastrowid
        messagebox.showinfo("Ajout","ajout avec succes")
        menu.destroy()
        call(["python","menu principale.py"])



    except Exception as e:
        print(e)
        mabase.rollback()
        mabase.close()

####supprimer
def supprimer():
    if (id.get() == "" or denomination.get() == "" or annee.get() == ""):
        messagebox.showwarning("Erreur", "selectionez une identification a supprimer")
    else:
        a=messagebox.askokcancel("Confirmation","vous etes sures de supprimer cet identifcation ?")

        if (a == True):
            Id = id.get()
            Denomination = denomination.get()
            Tp = TP.get()
            nRC = RC.get()
            Ncnss = num_cnss.get()
            Iff = iff.get()
            Email = email.get()
            Tele = tel.get()
            Annee = annee.get()


            conn = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='',
                                   database='cgb_database')
            con = conn.cursor()
            try:
                sql = "DELETE FROM identification WHERE id=%s"
                val = (Id,)
                con.execute(sql, val)
                conn.commit()
                dernierid = con.lastrowid
                messagebox.showinfo("information", "identification supprimee avec success !")
                menu.destroy()
                call(["python", "menu principale.py"])

            except Exception as e:
                print(e)
def collect(e):
    id.delete(0,END)
    denomination.delete(0, END)
    TP.delete(0, END)
    RC.delete(0, END)
    num_cnss.delete(0, END)
    iff.delete(0, END)
    email.delete(0, END)
    tel.delete(0, END)
    annee.delete(0, END)

    id.insert(END, "")
    denomination.insert(END, "")
    TP.insert(END, "")
    RC.insert(END, "")
    num_cnss.insert(END, "")
    iff.insert(END, "")
    email.insert(END, "")
    tel.insert(END, "")
    annee.insert(END, "")

    selected=PatrolView.focus()
    temp=PatrolView.item(selected,'values')

    id.insert(END, temp[0])
    denomination.insert(END, temp[1])
    TP.insert(END, temp[2])
    RC.insert(END, temp[3])
    num_cnss.insert(END, temp[4])
    iff.insert(END, temp[5])
    email.insert(END, temp[6])
    tel.insert(END, temp[7])
    annee.insert(END, temp[8])
PatrolView.bind("<ButtonRelease-1>",collect)



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

##Execution
menu.mainloop()


