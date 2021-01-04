from doctest import master
import tkinter as tk
from PIL import ImageTk, Image

#--------------------------------------------------------FUNCIONES--------------------------------------------------------#
def centrar_ventanaPrincipal():#Esta función hace que la ventana se situe justo al centro de cualquier pantalla.
    x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana_principal.geometry(posicion)

def ventana_Signin():
    def centrar_ventanaIngresar():  # Esta función hace que la ventana se situe justo al centro de cualquier pantalla.
        x_ventana = ventana_ingresar.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana_ingresar.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana_ingresar.geometry(posicion)

    ventana_ingresar = tk.Toplevel(ventana_principal)
    ventana_ingresar.title("Ingresar")
    ventana_ingresar.geometry(centrar_ventanaIngresar())

def ventana_login():#Funcion que contiene la interfaz con la que interactua el usuario
    image = Image.open(r"C:\Users\HP\PycharmProjects\Videoclub\img\fondoLogin2.jpg")
    photo = ImageTk.PhotoImage(image)
    background_label = tk.Label(master, image=photo)
    background_label.photo = photo
    background_label.place(x=0, y=0, height=450, width=300)

    tk.Button(ventana_principal, text="Ingresar", height="3", width="30").place(x=42, y=290)
    tk.Button(ventana_principal, text="Registrar", height="3", width="30", command = ventana_Signin).place(x=42, y=360)

    tk.Label(ventana_principal, text="Usuario: ", bg="white").place(x=42, y=150, width=69, height=25)

    txt_usuario = tk.StringVar()
    tk.Entry(ventana_principal, textvariable=txt_usuario).place(x=110, y=150, width=150, height=25)

    tk.Label(ventana_principal, text="Contraseña: ", bg="white").place(x=42, y=190, width=69, height=25)

    txt_contraseña = tk.StringVar()
    tk.Entry(ventana_principal, textvariable=txt_contraseña).place(x=110, y=190, width=150, height=25)

#--------------------------------------------------------Ventana--------------------------------------------------------#
ventana_principal = tk.Tk()
ancho_ventana = 300
alto_ventana = 450
ventana_principal.resizable(0,0)
ventana_principal.geometry(centrar_ventanaPrincipal())
ventana_principal.title("Bienvenido")
ventana_principal.iconbitmap(r"C:\Users\HP\PycharmProjects\Videoclub\img\logo.ico")

ventana_login()
ventana_principal.mainloop()

#contacto = Funcion()
#contacto.insertar("2","Alexis","Mejias","alex12","9933256272","alex18@gmail.com","1234")
#input()