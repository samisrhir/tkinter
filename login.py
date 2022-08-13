from tkinter import *
from subprocess import call
from tkinter import messagebox
import customtkinter
root = customtkinter.CTk()
root.title('CGB LOGIN')
root.geometry('1080x500+300+200')
root.configure(bg="black")
root.resizable(False, False)
root.iconbitmap('C:\\Users\\vansa\\Desktop\\tkinter\\o.ico')

#--------------methode-------------------
def login():
    username = user.get()
    password = code.get()
    if username == 'reda' and password == '123':
            messagebox.showinfo("BIENVENUE",'connexion reussie')
            root.destroy()
            call(["python","choix.py"])
    elif username == '' or password == '' :
            messagebox.showerror("EMPTY", 'please fill both fields')
    else :
            messagebox.showerror("INVALIDE", 'login or password incorrect')
#image
img = PhotoImage(file="oo.png")
Label(root, image=img, bg='black').place(x=10, y=30)

frame =customtkinter.CTkFrame(width=330,height=300,corner_radius=30)

frame.place(x=650, y=80)

heading = customtkinter.CTkLabel(master=frame, text='Administrator',text_font=("Cambria", 30))
heading.place(x=45, y=15)
#ligne decoree
Frame(frame, width=289, height=3, bg='yellow').place(x=23, y=109)
Frame(frame, width=289, height=3, bg='yellow').place(x=23, y=180)
#user and code
user=customtkinter.CTkEntry(text_font=("Cambria",10),master=frame,width=290,placeholder_text="Username",border_width=0,border_color='blue',corner_radius=0.5)
user.place(x=22, y=80)


code = customtkinter.CTkEntry(text_font=("Cambria",10),master=frame,width=290,border_width=0,show="*",placeholder_text="Password",corner_radius=0.5)

code.place(x=22, y=150)


##button login
login_butt=customtkinter.CTkButton(frame,text="login", width=290,border_width=0,corner_radius=8,fg_color='yellow',hover_color='#69f542',text_color='BLACK',height=40,
                                   command=login,text_font=' Cambria').place(x=20, y=204)







root.mainloop()
