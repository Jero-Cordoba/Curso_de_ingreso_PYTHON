import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    G. Minimo numero y que sea positivo
    H. Maximo numero y que sea negativo
    I. Promedio de los negativos y Promedio de los positivos
    J. Cantidad de numeros ingresados
Informar los resultados mediante alert()
'''
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        bandera_primer_ingreso = True
        maximo = 0
        minimo = 0
        while True:
            numero = int(prompt("While-10", "Ingresar un número"))
            if numero != None:
                if bandera_primer_ingreso:
                    maximo = numero
                    minimo = numero
                    bandera_primer_ingreso = False
                else:
                    if maximo < numero:
                        maximo = numero
                    if minimo > numero:
                        minimo = numero
            else:
                break
            
            diferencia = maximo - minimo
            promedio_negativo = 0
            promedio_positivo = 0
            
            if maximo < 0:
                promedio_negativo = maximo
            if minimo > 0:
                promedio_positivo = minimo
            
        mensaje = f"Maximo: {maximo}\nMinimo: {minimo}\nDiferencia: {diferencia}\nPromedio negativo: 
        {promedio_negativo}\nPromedio positivo: {promedio_positivo}"
    
        alert("While-10", mensaje)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
