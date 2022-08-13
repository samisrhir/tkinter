import customtkinter
import tkinter.messagebox
from tkinter import *

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")

menu= customtkinter.CTk()
menu.geometry('1200x800+500+500')
menu.title("menu principale")

#functions:

def fct1():
    print('button pressed')

menu.resizable(False,False)

fr1 =customtkinter.CTkFrame(width=300,height=200,corner_radius=10,fg_color="red")
fr1.place(x=10,y=10)
fr2 = customtkinter.CTkFrame(width=600,height=800)
fr2.bg_color='red'
fr2.place(x=600,y=0)


##variable= tool(master,option)
bt1=customtkinter.CTkButton(master=fr2, text="submit",command=fct1,text_font="Cambria")
bt1.place(x=250, y=20)
bt2=button = customtkinter.CTkButton(fr2, fg_color="red",hover_color="green")
bt2.place(x=20, y=20)
menu.mainloop()