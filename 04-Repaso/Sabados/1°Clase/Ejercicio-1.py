import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo 
apellido: Córdoba
---
Ejercicio: Repaso 1 - Ejercicio 1
---
Enunciado:
Ingresar el valor del dólar oficial y el valor del dólar blue.
Mostrar la diferencia expresada en porcentaje entre una cotización y otra.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        dolar_oficial = 825 
        dolar_blue = 1125
        diferencia = (dolar_blue - dolar_oficial) / dolar_oficial * 100
        alert("Repaso 1 - Ejercicio 1", f"La diferencia es de {diferencia:.2f}%")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
