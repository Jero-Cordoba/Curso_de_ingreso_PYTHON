import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert
'''
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre = str(prompt("Ingreso de dato", "Ingrese su nombre:"))
        edad = int(prompt("Ingreso de dato", "Ingrese su edad:"))
        votos = int(prompt("Ingreso de dato", "Ingrese la cantidad de votos:"))
        
        contador = 0
        max_votos = 0
        min_votos = votos
        suma_votos = 0
        while contador < 3:
            if votos > max_votos:
                max_votos = votos
            if votos < min_votos:
                min_votos = votos
            votos = int(prompt("Ingreso de dato", "Ingrese la cantidad de votos:"))
            suma_votos += votos
            contador += 1
            break
        promedio = suma_votos / 3
        alert("Elecciones paso", "El candidato con mas votos es: " + str(max_votos) + 
            "\nEl candidato con menos votos es: " + str(min_votos) + "\nEl promedio de votos es: " + str(promedio))
            
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
