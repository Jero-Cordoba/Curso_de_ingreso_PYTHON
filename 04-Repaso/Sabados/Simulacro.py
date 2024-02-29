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
        votantes_giovani = 0
        votantes_giani = 0
        votantes_esteban = 0 
        genero_masculino = 0
        genero_femenino = 0
        genero_otro = 0
        total_votos = 0     
        suma_edades = 0
        edad_masviejo = 0 
        edad_femenino = 0
        nombre_gianni = ""
        re_votar = True
        edad_gianni = float('inf')
        #Se q ya envie el codigo pero me di cuenta de un error importante, si ya tengo el "re_votar" en true, no es necesario q lo iguale
        while re_votar:
            nombre = input("Ingrese su nombre:").capitalize
            while nombre == None or nombre == "":
                print("Por favor, ingrese un nombre")
                
            edad = int(input("Ingresa su edad:"))
            if edad <= 13:
                print("Puede votar")
                continue
            
            genero_votante = input("Ingresa el genero del votante:").capitalize
            match genero_votante:
                case "Masculino":
                    genero_masculino += 1
                case "Femenino":
                    genero_femenino += 1
                case "Otro":
                    genero_otro += 1
                case _:
                    print("Genero no valido")
                
            participante_votado = input("Ingrese el nombre del votantes: (ejemplo: Gianni)").capitalize
            
            if participante_votado not in ["Giovanni", "Gianni", "Esteban"]:
                print("Participante no válido. Intente Nuevamente")
                continue
            
            if participante_votado == "Giovanni":
                votantes_giovani += 1
                
            elif participante_votado == "Gianni":
                votantes_giani += 1 
                if edad < edad_gianni:
                    nombre_gianni = nombre
                    edad_gianni = edad
            elif participante_votado == "Esteban":
                votantes_esteban += 1
            
            if genero_votante == "Femenino":
                suma_edades += edad
                edad_femenino += 1
                genero_femenino += 1
                
            re_votar = question("¿Quieres votar de nuevo?")
            
        if edad > edad_masviejo:
            nombre_masviejo = nombre
            edad_masviejo = edad
        total_votos += 1
        
        porcentaje_giovanni = votantes_giovani / total_votos * 100
        porcentaje_gianni = votantes_giani / total_votos * 100
        porcentaje_esteban = votantes_esteban / total_votos * 100
        
        if votantes_giovani > votantes_giani and votantes_giovani > votantes_esteban:
            mensaje = ("El/La participante que debe dejar la casa es: Giovanni")
        elif votantes_giani > votantes_giovani and votantes_giani > votantes_esteban:
            mensaje = ("El/La participante que debe dejar la casa es: Gianni")
        elif votantes_esteban > votantes_giani and votantes_esteban > votantes_giovani:
            mensaje = ("El/La participante que de debe dejar la casa es: Esteban")
        else:
            mensaje = ("Nadie se va de la casa más famosa del mundo")
            
        alert (mensaje)
    
        print("El promedio de edad de las votantes femeninas son del:" + suma_edades / edad_femenino)
        print("El votante más viejo, de la casa más famosa del mundo es:" + nombre_masviejo)
        print("EL votante más joven que voto por Gianni es:" + nombre_gianni + "\n Y tiene tiene: " + edad_gianni)
        print("Giovanni tiene un porcentaje de votos del: " + porcentaje_giovanni)
        print("Gianni tiene un porcentaje de votos del:" + porcentaje_gianni)
        print("Esteban tiene un porcentaje de votos del:" + porcentaje_esteban)
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
