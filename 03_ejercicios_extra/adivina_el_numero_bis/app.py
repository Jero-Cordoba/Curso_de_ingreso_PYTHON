import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado
el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “usted es un Psíquico”.
	2° intento: “excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	Más de 6 intentos: “afortunado en el amor!!”.

de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.numero_secreto = random.randint(1, 100)
        self.numero_intento = 0
        print(f'La maquina eligio el numero {self.numero_secreto}')

    def btn_mostrar_on_click(self):
        intentos = self.numero_intento + 1
        match intentos:
            case 1:
                "Usted es un Psíquico"
            case 2:
                "Excelente percepción"
            case 3:
                "Esto es suerte"
            case 4 | 5 | 6:
                "Excelente técnica"
            case _:
                "Afortunado en el amor!!"
        numero_ingresado = self.txt_numero.get()

        if numero_ingresado.isdigit():
            numero_ingresado = int(numero_ingresado)

            if numero_ingresado == self.numero_secreto:
                mensaje_ganador = (f"Ganaste en {self.numero_intento} intentos. {self.evaluar_aptitudes(self.numero_intento)}")
                alert(mensaje_ganador)

            elif numero_ingresado < self.numero_secreto:
                alert("Falta para llegar al número secreto")

            else:
                alert("Se pasó del número secreto")
        else:
            alert("Ingresa un número válido")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
