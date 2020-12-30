import tkinter
from doctest import master
from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


#--------------------------------------------------------FUNCIONES--------------------------------------------------------#
def centrar_ventana():
    x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)

#--------------------------------------------------------LOGIN--------------------------------------------------------#
ventana = Tk()
ancho_ventana = 300
alto_ventana = 450
ventana.resizable(0,0)
ventana.geometry(centrar_ventana())
ventana.title("Bienvenido")
ventana.iconbitmap(r"C:\Users\HP\PycharmProjects\Videoclub\img\logo.ico")

image = Image.open(r"C:\Users\HP\PycharmProjects\Videoclub\img\fondoLogin2.jpg")
photo = ImageTk.PhotoImage(image)
background_label = Label(master, image=photo)
background_label.photo = photo
background_label.place(x=0, y=0, height=450, width=300)

#Label(text="Acceso al sistema", bg="Gray", fg="white", width="300", height="2", font=("Calibrí", 15)).pack()
#Label(text="").pack()

btn_ingresar  = Button(text="Ingresar", height="3", width="30").place(x=42, y=290)
btn_registrar = Button(text="Registrar", height="3", width="30").place(x=42, y=360)


lbl_usuario = Label(ventana,text="Usuario: ", bg="white")
lbl_usuario.place(x=42, y=150, width=69, height=25)

txt_usuario = StringVar()
caja = Entry(ventana, textvariable=txt_usuario)
caja.place(x=110, y=150, width=150, height=25)

lbl_contraseña = Label(ventana,text="Contraseña: ", bg="white")
lbl_contraseña.place(x=42, y=190, width=69, height=25)

txt_contraseña = StringVar()
caja = Entry(ventana, textvariable=txt_contraseña)
caja.place(x=110, y=190, width=150, height=25)


ventana.mainloop()
