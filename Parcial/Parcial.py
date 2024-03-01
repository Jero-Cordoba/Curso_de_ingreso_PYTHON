import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
Turno Mañana
DNI: 43083726
Profesor: Esteban
---
Ejercicio: Parcial 
---
Parcial Turno Mañana:
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso (entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas
Condiciones de aprobación:
Se debe realizar el ingreso de datos de manera correcta con las validaciones correspondientes siguiendo las
reglas de estilo de la cátedra y al menos uno de los informes solicitados de manera perfecta para obtener una
nota 6(seis)
Cada informe adicional logrado correctamente suma un punto más hasta obtener nota 10(diez)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]

    def btn_mostrar_on_click(self):
        mascotas = 5
        sexo_menor = 0; 
        edad_mascota = 0; mas_joven = 0
        porcentaje_perro = 0; porcentaje_gato = 0; porcentaje_exotico = 0
        promedio_peso = 0; menos_pesada = 0
        
        
        for i in range(mascotas):
            print(f"Ingrese los datos de la mascota {i+1}:")
            nombre = prompt("Ingrese el nombre de tu mascota")
            while not nombre:
                print ("El nombre no puede estar vacío")
                nombre = prompt("Ingrese el nombre de tu mascota")
                
            tipo = prompt("Ingrese el tipo de mascota que tiene: (Ejemplo: perro, gato, exotico)")
            while tipo != "perro" or tipo != "gato" or tipo != "exotico":
                print ("El tipo no puede estar vacío")
                tipo = prompt("Ingrese el tipo de mascota que sea valido: perro, gato o exotico")
            
            peso = float(prompt("Ingrese el peso de su mascota - debe estar entre 10 y 80 kilos"))
            while not peso or peso < 10 or peso > 80:
                print ("El peso no puede estar vacío")
                peso = float(prompt("Ingrese el peso de su mascota - debe estar entre 10 y 80 kilos"))
            
            sexo = input(f"Ingrese el sexo de {nombre} (F, M): ")
            while sexo != "F" and sexo != "M":
                sexo = input("Sexo inválido. Ingrese el sexo (F, M): ")

            edad = int(input(f"Ingrese la edad de {nombre}: "))
            while edad <= 0:
                edad = int(input("Edad inválida. Ingrese la edad: "))        
            
#A- Cuál fue el sexo menos ingresado (F o M)
            if sexo == "M":
                
                
                
                
    if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
