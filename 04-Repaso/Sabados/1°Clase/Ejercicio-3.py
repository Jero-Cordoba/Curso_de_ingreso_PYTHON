import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo 
apellido: Córdoba
---
Ejercicio: Repaso 1 - Ejercicio 3
---
Enunciado:
La juguetería El MUNDO DE OCTAVIO nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

COMETA: 

AB = Diágonal mayor
DC = Diágonal menor
BD y BC = lados menores
AD y AC = lados mayores

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

COMETA BICOLOR

Ahora necesitamos saber cuánto papel de cada color necesitamos. Las entradas son las mismas.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        AB = int(prompt("Diagonal mayor (AB)"))
        DC = int(prompt("Diagonal menor (DC)"))
        BD = int(prompt("Lado menor (BD)"))
        BC = int(prompt("Lado mayor (BC)"))
        AD = int(prompt("Lado menor (AD)"))
        AC = int(prompt("Lado mayor (AC)"))
        
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
