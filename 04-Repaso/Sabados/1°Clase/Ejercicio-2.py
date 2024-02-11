import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
TEjercicio: Repaso 1 - Ejercicio 2
---
Enunciado:
Para saber el costo de un viaje necesitamos el siguiente algoritmo, sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT, los datos a solicitar de dos personas son, nombre, edad y peso
se pide  armar el siguiente mensaje:"hola german y marina , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos"
'''

class App (customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Nombre 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre1 = customtkinter.CTkEntry(master=self)
        self.txt_nombre1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Nombre 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_nombre2 = customtkinter.CTkEntry(master=self)
        self.txt_nombre2.grid(row=1, column=1)
        
        self.label_3 = customtkinter.CTkLabel(master=self, text="Peso 1")
        self.label_3.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_peso1 = customtkinter.CTkEntry(master=self)
        self.txt_peso1.grid(row=0, column=1)

        self.label_4 = customtkinter.CTkLabel(master=self, text="Peso 2")
        self.label_4.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_peso2 = customtkinter.CTkEntry(master=self)
        self.txt_peso2.grid(row=1, column=1)
        
        self.label_5 = customtkinter.CTkLabel(master=self, text="Edad 1")
        self.label_5.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad_1 = customtkinter.CTkEntry(master=self)
        self.txt_edad_1.grid(row=0, column=1)

        self.label_6 = customtkinter.CTkLabel(master=self, text="Edad 2")
        self.label_6.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_edad_2 = customtkinter.CTkEntry(master=self)
        self.txt_edad_2.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        nombre1 = self.txt_nombre1.get()
        nombre2 = self.txt_nombre2.get()
        edad1 = int(self.txt_edad_1.get())
        edad2 = int(self.txt_edad_2.get())
        promedio_edad = (edad1 + edad2) / 2
        peso1 = float(self.txt_peso1.get())
        peso2 = float(self.txt_peso2.get())
        peso_total = peso1 + peso2
        
        alert("Repaso 1 - Ejercicio 2", f"Hola{nombre1} y {nombre2}, sus pesos son {peso1} y {peso2} kilos respectivamente,
            sumados da {peso_total} kilos, el promedio de edad es {promedio_edad} y su viaje vale {peso_total * 1000} pesos")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
#Me pueden decir donde esta el error?