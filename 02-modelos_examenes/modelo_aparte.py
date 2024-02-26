import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
Ejercicio: Extra-Parcial 
---
Ejercicio:
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
edad(mayor a 0)
pedir datos por prompt y mostrar por print

Punto A- informar cual fue el sexo mas ingresado
Punto B- el porcentaje de personas con fiebre y el porcentaje sin fiebre
Punto C- por el número de DNI del alumno

DNI terminados en 0 o 1:
1)informar la cantidad de personas de sexo  femenino
2) la edad promedio de  personas de sexo  masculino
3) el nombre de la persona la persona de sexo  nb con más temperatura(si la hay)

DNI terminados en 2 o 3:
1) informar la cantidad de personas de sexo  masculino
2) la edad promedio de  personas de sexo  nb
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)

DNI terminados en 4 o 5:    
1)informar la cantidad de personas de sexo  nb
2) la edad promedio de  personas de sexo  femenino
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)

DNI terminados en 6 o 7:
1)informar la cantidad de personas mayores de edad (desde los 18 años)
2)la edad promedio en total de todas las personas mayores de edad (18 años)
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)

DNI terminados en 8 o 9:
1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)

Todos los alumnos: 
B-informar cual fue el sexo mas ingresado
C-el porcentaje de personas con fiebre y el porcentaje sin fiebre
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]

    def btn_mostrar_on_click(self):
        masculino = 0; femenino = 0; noBinario = 0
        edad_masculino = 0; edad_femenino = 0
        fiebre = 0; no_fiebre = 0
        mayores = 0; menores = 0; suma_edad_mayores = 0; temperatura_menor_edad = 0
        
        nombre_noBinario = []
        nombres_masculino_baja = []
        nombres_femenino_alta = []
        
        while len(nombre_noBinario) < 5:
            nombre = prompt("Ingrese el nombre")
        
        while True:
            try: 
                temperatura = float(prompt("Ingrese la temperatura"))
                if temperatura <= 35 or temperatura >= 42:
                    break
                else:
                    alert("La temperatura debe estar entre 35 y 42")
            except:
                alert("La temperatura debe ser un valor numerico")
            
        genero = prompt("Ingrese el genero").lower()
        match genero:
            case "masculino":
                masculino += 1
                edad_masculino += 1
                if temperatura < 37:
                    nombres_masculino_baja.append(nombre)
            case "femenino":
                femenino += 1
                edad_femenino += 1
                if temperatura > 37:
                    nombres_femenino_alta.append(nombre)
                    fiebre += 1
                else:
                    no_fiebre += 1
            case "no binario":
                noBinario += 1
                nombre_noBinario.append(nombre)
                if temperatura < 38:
                    fiebre += 1
                else:
                    no_fiebre += 1
            case _:
                alert("El genero debe ser 'm', 'f' o 'nb'")
                    
        while True:
            try:
                edad = int(prompt("Ingrese su edad"))
                if edad > 0:
                    break
                else:
                    alert("La edad debe ser mayor a 0")
            except:
                alert("La edad debe ser un valor numerico")
        if edad >= 18:
            mayores += 1
            suma_edad_mayores += edad
        else:
            menores += 1
            temperatura_menor_edad += temperatura

        porcentaje_fiebre = (fiebre/5)*100
        porcentaje_no_fiebre = (no_fiebre/5)*100
        
        dni_terminacion = int(prompt("Ingrese los últimos dígitos del DNI (0-9):"))

        if dni_terminacion in [0, 1]:
            if genero.lower() == 'f':
                femenino += 1
            elif genero.lower() == 'm':
                masculino += edad
            elif genero.lower() == 'nb':
                if not nb_temperatura_alta_01 or temperatura > nb_temperatura_alta_01[1]:
                    nb_temperatura_alta_01 = (nombre, temperatura)
        
        resultado = f"Sexo más ingresado: {genero}\n" \
                    f"Porcentaje de personas con fiebre: {porcentaje_fiebre}%\n" \
                    f"Porcentaje de personas sin fiebre: {porcentaje_no_fiebre}%\n\n" \
                    f"Información para DNI terminados en 0 o 1:\n" \
                    f"Cantidad de personas de sexo femenino: {femenino}\n" \
                    f"Edad promedio de personas de sexo masculino: {edad_femenino}\n" \
                    f"Nombre de la persona NB con más temperatura: {nombre_noBinario[0]} ({temperatura}°C)\n\n" \
                    f"Información para DNI terminados en 2 o 3:\n" \
                    f"Cantidad de personas de sexo masculino: {femenino}\n" \
                    f"Edad promedio de personas de sexo NB: {edad_femenino}\n" \
                    f"Nombre de la persona femenino con temperatura más baja: {nombres_femenino_alta[0]} ({nombres_femenino_alta[1]}°C)\n\n" \
                    f"Información para DNI terminados en 4 o 5:\n" \
                    f"Cantidad de personas de sexo NB: {noBinario}\n" \
                    f"Edad promedio de personas de sexo femenino: {edad_masculino}\n" \
                    f"Nombre de la persona masculino con temperatura más baja: {nombres_masculino_baja[0]} ({nombres_masculino_baja[1]}°C)\n\n" \
                    f"Información para DNI terminados en 6 o 7:\n" \
                    f"Cantidad de personas mayores de edad: {mayores}\n" \
                    f"Edad promedio de todas las personas mayores de edad: {suma_edad_mayores/mayores}\n" \
                    f"Nombre de la persona masculino con temperatura más baja: {nombres_masculino_baja[0]} ({nombres_masculino_baja[1]}°C)\n\n" \
                    f"Información para DNI terminados en 8 o 9:\n" \
                    f"Cantidad de personas menores de edad: {menores}\n" \
                    f"Temperatura promedio de todas las personas menores de edad: {temperatura_menor_edad/menores}\n" \
                    f"Nombre de la persona femenino con temperatura más baja: {nombres_femenino_alta[0]} ({nombres_femenino_alta[1]}°C)"

        alert(resultado)
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
