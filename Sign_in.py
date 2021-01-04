from doctest import master
import tkinter as tk
from PIL import ImageTk, Image

#--------------------------------------------------------FUNCIONES--------------------------------------------------------#
#def centrar_ventanaPrincipal():#Esta función hace que la ventana se situe justo al centro de cualquier pantalla.
#    x_ventana = ventana_ingresar.winfo_screenwidth() // 2 - ancho_ventana // 2
#   y_ventana = ventana_ingresar.winfo_screenheight() // 2 - alto_ventana // 2

#    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
#    ventana_ingresar.geometry(posicion)

class ventana():
    def ingresar(self):
        ventana_ingresar = tk.Tk()
        ancho_ventana = 300
        alto_ventana = 450
        ventana_ingresar.resizable(0,0)
        ventana_ingresar.geometry("500x500")
        ventana_ingresar.title("Hola")
        ventana_ingresar.iconbitmap(r"C:\Users\HP\PycharmProjects\Videoclub\img\logo.ico")

        ventana_ingresar.mainloop()
