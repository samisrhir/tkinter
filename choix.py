from tkinter import *
from subprocess import call
from tkinter import messagebox
import customtkinter
from PIL import Image,ImageTk
root = customtkinter.CTk()
root.title('CGB travail menu ')
root.geometry('1080x500+300+200')
root.configure(bg="black")

root.resizable(False, False)
root.iconbitmap('C:\\Users\\vansa\\Desktop\\tkinter\\o.ico')
Label(root, bg='black').place(x=10, y=30)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
####styleee
frame1 =customtkinter.CTkFrame(root,width=1040,height=450,corner_radius=30)
frame1.place(x=20, y=30)

frame2 = customtkinter.CTkFrame(frame1,width=180, height=340, corner_radius=30,fg_color="black")

frame2.place(x=10, y=20)

frame3= customtkinter.CTkFrame(frame1,width=820, height=410, corner_radius=30,fg_color="#347C98")
frame3.place(x=200, y=20)

frame4= customtkinter.CTkFrame(frame3,width=370, height=370, corner_radius=30,fg_color="#2F3D40")
frame4.place(x=30, y=20)
frame5= customtkinter.CTkFrame(frame3,width=370, height=370, corner_radius=30,fg_color="#2F3D40")
frame5.place(x=420, y=20)

frame6= customtkinter.CTkFrame(frame1,width=160, height=10, corner_radius=30,fg_color="#CC8D1A")
frame6.place(x=20, y=160)
frame7= customtkinter.CTkFrame(frame4,width=330, height=60, corner_radius=30,fg_color="#2F3D40")
frame7.place(x=20, y=150)


frame8=customtkinter.CTkFrame(frame5,width=330, height=130, corner_radius=10,fg_color="#182625")
frame8.place(x=20, y=220)

frame9=customtkinter.CTkFrame(frame4,width=330, height=100, corner_radius=10,fg_color="#182625")
frame9.place(x=20, y=220)
frame0=customtkinter.CTkFrame(frame4,width=330, height=10, corner_radius=30,fg_color="#009999")
frame0.place(x=20, y=330)

#######functions
####btn_identification
def open_id():
    root.destroy()
    call(["python", "menu principale.py"])
    print("identification")

def open_dec_mo():
    root.destroy()
    call(["python", "declaration_mens.py"])
    print("monsuelle")
#btnn mensuelle-------
def open_dec_an():
    root.destroy()
    call(["python", "declaration_annuelle.py"])
    print("annuelle")
#btnn mensuelle-------

btnamois=customtkinter.CTkButton(text_font=("Cambria",25),master=frame8,width=310,height=50,fg_color="#1d3857",corner_radius=18,text="Mensuelle",command=open_dec_mo)
btnamois.place(x=10, y=10)
#btnn annuelles-------

btn=customtkinter.CTkButton(text_font=("Cambria",25),master=frame8,width=310,height=50,fg_color="#1d3857",corner_radius=18,text="Annuelle",command=open_dec_an)
btn.place(x=10, y=70)
##btn_identif
btnid=customtkinter.CTkButton(text_font=("Cambria",25),master=frame9,width=310,height=50,fg_color="#1d3857",corner_radius=18,text="acceder",command=open_id)
btnid.place(x=10, y=25)

###titles
heading = customtkinter.CTkLabel(master=frame7, text='IDentification',text_font=("Cambria", 30),text_color="#347C98")
heading.place(x=45, y=15)

heading = customtkinter.CTkLabel(master=frame5, text='Declarations',text_font=("Cambria", 30),text_color="#347C98")
heading.place(x=74, y=163)


####logo and icones
img= (Image.open("oo.png"))
resized_image= img.resize((160,120), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
Label( frame1,image=new_image, bg='black').place(x=16, y=30)

img2= (Image.open("home.png"))
resized_image2= img2.resize((130,120), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)
Label( frame1,image=new_image2, bg='black').place(x=30, y=200)

img3= (Image.open("identification.png"))
resized_image33= img3.resize((150,150), Image.ANTIALIAS)
new_image33= ImageTk.PhotoImage(resized_image33)
Label( frame4,image=new_image33,bg="#2F3D40").place(x=110, y=10)

img4= (Image.open("declar.png"))
resized_image4= img4.resize((150,148), Image.ANTIALIAS)

new_image4= ImageTk.PhotoImage(resized_image4)
Label( frame5,image=new_image4,bg="#2F3D40").place(x=110, y=10)

def exiit():
    root.destroy()
    call(["python","login.py"])

img2= (Image.open("exit.png"))
resized_image2= img2.resize((50,45), Image.ANTIALIAS)
new_image3= ImageTk.PhotoImage(resized_image2)

leave = customtkinter.CTkButton(master=frame1,image=new_image3,corner_radius=15,text="",text_font=("arial bold",21),fg_color="#181818",hover_color="cyan",text_color="black",width=180,height=60,command=exiit)
leave.place(x=10, y=370)




root.mainloop()