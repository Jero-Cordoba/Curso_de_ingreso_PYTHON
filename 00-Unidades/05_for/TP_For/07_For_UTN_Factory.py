import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)
'''
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):    
        cant_nb_ssr_edad_25_40 = 0
        nombre_jr_menor_edad = None
        edades_por_genero = {'F': [], 'M': [], 'NB': []}
        tecnologias = {'PYTHON': 0, 'JS': 0, 'ASP.NET': 0}
        cant_genero = {'F': 0, 'M': 0, 'NB': 0}
        for i in range(10):
            nombre = prompt("Ingrese su nombre")
            edad = int(prompt("Ingrese su edad"))
            genero = prompt("Ingrese su genero")
            tecnologia = prompt("Ingrese su tecnologia")
            puesto = prompt("Ingrese su puesto")
            
        
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
