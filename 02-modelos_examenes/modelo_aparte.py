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
        total_personas = 5
        contadores_sexo = {'F': 0, 'M': 0, 'NB': 0}
        fiebre = 0; no_fiebre = 0
        edad_masculino = 0;edad_noBinario = 0; edad_femenino = 0
        total_mayores_edad = 0; total_menores_edad = 0
        edad_mayores = 0; temperatura_menores = 0
        nombres_sexo_masculino_temp_baja = []
        nombres_sexo_femenino_temp_baja = []
        nombres_sexo_nb_temp_alta = []

        for i in range(total_personas):
            nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")

            temperatura = float(input(f"Ingrese la temperatura de {nombre}: "))
            while temperatura < 35 or temperatura > 42:
                temperatura = float(input("Temperatura inválida. Ingrese la temperatura: "))

            sexo = input(f"Ingrese el sexo de {nombre} (F, M, NB): ").upper()
            while sexo not in ['F', 'M', 'NB']:
                sexo = input("Sexo inválido. Ingrese el sexo (F, M, NB): ").upper()

            edad = int(input(f"Ingrese la edad de {nombre}: "))
            while edad <= 0:
                edad = int(input("Edad inválida. Ingrese la edad: "))

            contadores_sexo[sexo] += 1

            if temperatura >= 38:
                fiebre += 1
            else:
                no_fiebre += 1

            if int(nombre[-1]) in [0, 1]:
                if sexo == 'F':
                    contadores_sexo['F'] += 1
                    edad_femenino += edad
                    if temperatura < 35.0:
                        nombres_sexo_femenino_temp_baja.append(nombre)
                elif sexo == 'M':
                    edad_masculino += edad
                    if temperatura < 35.0:
                        nombres_sexo_masculino_temp_baja.append(nombre)
                else:
                    edad_noBinario += edad
                    if temperatura > 42.0:
                        nombres_sexo_nb_temp_alta.append(nombre)

            elif int(nombre[-1]) in [2, 3]:
                if sexo == 'M':
                    contadores_sexo['M'] += 1
                    edad_noBinario += edad
                    if temperatura < 35.0:
                        nombres_sexo_nb_temp_alta.append(nombre)
                elif sexo == 'NB':
                    edad_noBinario += edad
                else:
                    edad_femenino += edad
                    if temperatura < 35.0:
                        nombres_sexo_femenino_temp_baja.append(nombre)

            elif int(nombre[-1]) in [4, 5]:
                if sexo == 'NB':
                    contadores_sexo['NB'] += 1
                elif sexo == 'F':
                    contadores_sexo['F'] += 1
                    edad_femenino += edad
                    if temperatura < 35.0:
                        nombres_sexo_femenino_temp_baja.append(nombre)
                else:
                    edad_masculino += edad
                    if temperatura < 35.0:
                        nombres_sexo_masculino_temp_baja.append(nombre)

            elif int(nombre[-1]) in [6, 7]:
                if edad >= 18:
                    total_mayores_edad += 1
                    edad_mayores += edad
                    if sexo == 'M' and temperatura < 35.0:
                        nombres_sexo_masculino_temp_baja.append(nombre)
                if sexo == 'M':
                    edad_masculino += edad
                    if temperatura < 35.0:
                        nombres_sexo_masculino_temp_baja.append(nombre)

            elif int(nombre[-1]) in [8, 9]:
                if edad < 18:
                    total_menores_edad += 1
                    temperatura_menores += temperatura
                    if sexo == 'F' and temperatura < 35.0:
                        nombres_sexo_femenino_temp_baja.append(nombre)

        sexo_mas_ingresado = max(contadores_sexo, key=contadores_sexo.get)

        porcentaje_fiebre = (fiebre / total_personas) * 100
        porcentaje_sin_fiebre = (no_fiebre / total_personas) * 100

        if contadores_sexo['F'] > 0:
            edad_promedio_femenino = edad_femenino / contadores_sexo['F']
        else:
            edad_promedio_femenino = 0

        if contadores_sexo['M'] > 0:
            edad_promedio_masculino = edad_masculino / contadores_sexo['M']
        else:
            edad_promedio_masculino = 0

        if contadores_sexo['NB'] > 0:
            edad_promedio_nb = edad_noBinario / contadores_sexo['NB']
        else:
            edad_promedio_nb = 0

        if total_mayores_edad > 0:
            edad_promedio_mayores_edad = edad_mayores / total_mayores_edad
        else:
            edad_promedio_mayores_edad = 0

        if total_menores_edad > 0:
            temp_promedio_menores_edad = temperatura_menores / total_menores_edad
        else:
            temp_promedio_menores_edad = 0

        print("\nResultados:")
        print(f"Punto A: El sexo más ingresado fue {sexo_mas_ingresado}")
        print(f"Punto B: Porcentaje de personas con fiebre: {porcentaje_fiebre}%, Sin fiebre: {porcentaje_sin_fiebre}%")

        print("\nResultados según DNI:")
        print(f"1) DNI terminados en 0 o 1: \n  - Cantidad de personas femeninas: {contadores_sexo['F']}\n"
            f"  - Edad promedio de personas masculinas: {edad_promedio_masculino}\n"
            f"  - Personas no binarias con más temperatura: {'' if not nombres_sexo_nb_temp_alta else nombres_sexo_nb_temp_alta}")

        print(f"2) DNI terminados en 2 o 3: \n  - Cantidad de personas masculinas: {contadores_sexo['M']}\n"
            f"  - Edad promedio de personas no binarias: {edad_promedio_nb}\n"
            f"  - Personas femeninas con la temperatura más baja: {'' if not nombres_sexo_femenino_temp_baja else nombres_sexo_femenino_temp_baja}")

        print(f"3) DNI terminados en 4 o 5: \n  - Cantidad de personas no binarias: {contadores_sexo['NB']}\n"
            f"  - Edad promedio de personas femeninas: {edad_promedio_femenino}\n"
            f"  - Personas masculinas con la temperatura más baja: {'' if not nombres_sexo_masculino_temp_baja else nombres_sexo_masculino_temp_baja}")

        print(f"4) DNI terminados en 6 o 7: \n  - Cantidad de personas mayores de edad: {total_mayores_edad}\n"
            f"  - Edad promedio en total de personas mayores de edad: {edad_promedio_mayores_edad}\n"
            f"  - Personas masculinas con la temperatura más baja: {'' if not nombres_sexo_masculino_temp_baja else nombres_sexo_masculino_temp_baja}")

        print(f"5) DNI terminados en 8 o 9: \n  - Cantidad de personas menores de edad: {total_menores_edad}\n"
            f"  - Temperatura promedio en total de personas menores de edad: {temp_promedio_menores_edad}\n"
            f"  - Personas femeninas con la temperatura más baja: {'' if not nombres_sexo_femenino_temp_baja else nombres_sexo_femenino_temp_baja}")

        print("\nResultados para todos los alumnos:")
        print(f"B: El sexo más ingresado fue {sexo_mas_ingresado}")
        print(f"C: Porcentaje de personas con fiebre: {porcentaje_fiebre}%, Sin fiebre: {porcentaje_sin_fiebre}%")
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
