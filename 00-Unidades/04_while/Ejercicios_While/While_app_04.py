import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Jerónimo
apellido: Córdoba
---
Ejercicio: while_04
---
Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
        numero = int(prompt("While-04", "Ingresar un número entre 0 y 9"))
        while numero <= 0 or numero >= 9:
            numero = int(prompt("While-04", "Ingresar un número entre 0 y 9"))
            break
        while not (numero >= 0 and numero <= 9):
            numero = int(prompt("While-04", "Ingresar un número entre 0 y 9"))
            break
        alert("While-04", f"El numero ingresado es: {numero}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
