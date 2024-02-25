import tkinter, random
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt 
y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_secreto = random.randint(1, 100)
        intentos = 0
        max_intentos = 10
        
        def numero_intentos():
            if intentos == 1:
                mensaje = ("Usted es un psiquico")
            if intentos == 2:
                mensaje = ("Excelente percepción")
            if intentos == 3:
                mensaje = ("Esto es suerte")
            if intentos == 4 or intentos == 5 or intentos == 6:
                mensaje = ("Excelente técnica")
            if intentos == 7:
                mensaje = ("Perdiste, suerte para la sgunda")
            return mensaje
        
        for i in range(max_intentos):
            intentos += 1
            numero = int(prompt("Ingrese un numero"))
            if numero == numero_secreto:
                mensaje = (numero_intentos())
                break
            elif numero < numero_secreto:
                mensaje = ("Falta")
            elif numero > numero_secreto:
                mensaje = ("Se paso")
            if intentos == max_intentos:
                mensaje = ("Perdiste, suerte para la siguiente")
                break
            
            alert("IF-Ejercicio 9", mensaje)
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
