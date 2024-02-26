import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
Ejercicio: Simulacro de parcial 
---
Simulacro Turno Mañana:
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

-Nombre del votante

-Edad del votante (debe ser mayor a 13)

-Género del votante (Masculino, Femenino, Otro)

-El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

-No se sabe cuántos votos entrarán durante la gala.

-Se debe informar al usuario:

-El promedio de edad de las votantes de género Femenino 

-Del votante más viejo, su nombre.

-Nombre del votante más joven qué votó a Gianni.

-Nombre de cada participante y porcentaje de los votos qué recibió.

-El nombre del participante que debe dejar la casa (El que tiene más votos)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        masculino = 0; femenino = 0; otro = 0
        votos_giovani = 0; votos_gianni = 0; votos_esteban = 0; votos_totales = 0
        nombre_viejo = ""; edad_viejo = 0
        nombre_mas_joven_gianni = ""; edad_mas_joven_gianni = float("inf")
        contador_femenino = 0; suma_edad_femenino = 0
        
        placa = ["Giovanni", "Gianni", "Esteban"]
        genero = ["Masculino", "Femenino", "Otro"]
        re_votar = True
        
        while re_votar:
            nombre = prompt("Ingrese su nombre:").capitalize
            while True:
                try:
                    edad = int(prompt("Ingresa su edad:"))
                    if edad <= 13:
                        break
                    else:
                        print("Por favor, ingrese una edad mayor a 13")
                except:
                    print("Por favor, ingrese una edad")
        
            while True:
                genero = prompt("Ingresa el genero del votante:").capitalize
                match genero:
                    case "Masculino":
                        masculino += 1
                    case "Femenino":
                        femenino += 1; contador_femenino += 1; suma_edad_femenino += edad
                    case "Otro":
                        otro += 1
                    case _:
                        print("Por favor, ingrese un genero valido")
                        break
            
            while True:
                participante = prompt("Ingresa el nombre del participante:").capitalize
                if participante in placa:
                    if participante == "Giovanni":
                        votos_giovani += 1
                    elif participante == "Gianni":
                        votos_gianni += 1
                    elif participante == "Esteban":
                        votos_esteban += 1
                    votos_totales += 1
                    break
                else:
                    print("Por favor, ingrese un nombre de participante")
                    
            if edad > edad_viejo:
                nombre_viejo = nombre
                edad_viejo = edad
                
            if participante == "Gianni" and edad < edad_mas_joven_gianni:
                nombre_mas_joven_gianni = nombre
                edad_mas_joven_gianni = edad
                
            re_votar = question("¿Desea votar de nuevo?")
            
            promedio_edad_femenino = suma_edad_femenino / contador_femenino
            votos_totales = votos_giovani + votos_gianni + votos_esteban
            
            porcentaje_giovani = (votos_giovani / votos_totales) * 100
            porcentaje_gianni = (votos_gianni / votos_totales) * 100
            porcentaje_esteban = (votos_esteban / votos_totales) * 100
            
            alert(f"Promedio de edad de los votantes de género femenino: {promedio_edad_femenino:.2f}")
            alert(f"Votante más viejo: {nombre_viejo} con {edad_viejo} años")
            alert(f"Votante más joven: {nombre_mas_joven_gianni} con {edad_mas_joven_gianni} años")
            alert(f"Porcentaje de votos de Giovanni: {porcentaje_giovani}%")
            alert(f"Porcentaje de votos de Gianni: {porcentaje_gianni}%")
            alert(f"Porcentaje de votos de Esteban: {porcentaje_esteban}%")
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
