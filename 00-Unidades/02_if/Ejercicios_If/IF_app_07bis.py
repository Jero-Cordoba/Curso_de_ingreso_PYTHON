import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo 
apellido: Córdoba
---
Ejercicio: if_07 bis
---
Enunciado: El siguiente ejercicio debe tener un solo alert escrito en el código.SI SI , uno solo.
Si es menor de 13, mostrar el mensaje “feliz día”.
Si es adolescente el mensaje es “usted es adolescente”
Si tiene 17 años además mostrar el mensaje “último año!!!”
Si es mayor de edad mostrar el mensaje “tenes edad de laburar”.
Si tiene 33 años, además mostrar el mensaje “como cristo”
Si tiene más de 60 años, además mostrar el mensaje “A jubilarse”.
Si tiene 88, además mostrar el mensaje “lindo número''
Si la edad es par, además mostrar, “sos par!!”.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
        edad = int(self.txt_edad.get())
        
        mensaje = ""

        if edad < 13:
            mensaje = "Feliz día"
        elif 14 <= edad < 16:
            mensaje = "Usted es adolescente"
        elif edad == 17:
            mensaje = "\n¡Último año!"
        elif edad == 18:
            mensaje = "Tenés edad de laburar"
        elif edad == 33:
            mensaje = "\nComo Cristo"
        elif edad == 60:
            mensaje = "\nA jubilarse"
        elif edad == 88:
            mensaje = "\nLindo número"
        elif edad % 2 == 0:
            mensaje = "\nSos par!!"
        
        alert("IF-Ejercicio 7 bis", f"{mensaje}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
    