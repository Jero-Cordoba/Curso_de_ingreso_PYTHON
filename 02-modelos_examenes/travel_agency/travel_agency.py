from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import tkinter as tk
import customtkinter
import warnings

'''
#!################ INTRODUCCION #################
# Nos encargan el desarrollo de una aplicación que le permita a sus usuarios inscribirse a 
    un listado de viajeros para un nuevo transbordador de SpaceX:
'''
NOMBRE = 'Jerónimo Córdoba' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
A) Para ello deberás programar el botón 'Cargar Viajeros' para poder cargar los siguientes datos de 5 personas:
    * Nombre
    * Altura (entre 60 cm y 200 cm)
    * Peso (entre 40 kilos y 250 kilos)
    * Edad (entre 1 y 100 ) 

B) Al presionar el botón "Mostrar Datos Crudo" se deberán listar todos los datos de los usuarios y 
    su posición en la lista (por terminal) 

#!################ ACLARACION IMPORTANTE #################
Del punto C solo deberá realizar 2 informes. Para determinar que informe hacer, 
    tenga en cuenta lo siguiente:

    Informe 1- Tome el último número de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    Informe 2- el promedio de altura entre todos los usuarios ingresados que sean mayores de 18 años

Realizar los informes correspondientes a los números obtenidos. 
    EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) 
        A- El nombre de la persona con el menor peso ingresado
        B- La cantidad de personas de más de 50 años
    #! 1) 
        A- El nombre de la persona con el mayor peso ingresado
        B- La cantidad de personas de menos de 50 años
    #! 2)
        A- El nombre de la persona con la mayor altura ingresada
        B- La cantidad de personas de más de 80 kilos
    #! 3)
        A- El nombre de la persona con la menor altura ingresada
        B- La cantidad de personas de menos de 100 kilos
    #! 4) 
        A- El nombre de la persona con la mayor edad ingresada
        B- La cantidad de personas de más de 100 cm de altura
    #! 5) 
        A- El nombre de la persona con la menor edad ingresada
        B- La cantidad de personas de menos de 170 cm de altura 
    #! 6) 
        A- El nombre de las personas que NO superen la edad promedio
        B- La cantidad de personas de menos de 160 cm de altura
    #! 7) 
        A- El nombre de las personas que NO superen la altura promedio
        B- La cantidad de personas de menos de 80 kilos
    #! 8)
        A- El nombre de las personas que NO superen el peso promedio
        B- La cantidad de personas de más  de 50 kilos
    #! 9) 
        A- El nombre de las personas que SI superen el peso promedio
        B- La cantidad de personas de menos de 18 años
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - ◄TravelCode Agency► coded by {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"◄TravelCode Agency► coded by {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/travel_agency/UTN_Travel_Agency_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Viajeros", command=self.btn_cargar_viajeros_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos Crudo", command=self.btn_mostrar_datos_crudo_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para el boton mostrar
        # Cargar aca los pokemones
        self.lista_nombres = [
            "Pepe", "Moni", "Paola", "Fatiga", "Dardo",
            "Maria", "Añanga", "Goku", "Vegeta", "Roshi"
        ]

        self.lista_alturas_cm = [
            174, 165, 155, 60, 180, 159, 60, 175, 170, 150
        ]

        self.lista_pesos = [
            80, 70, 65, 41, 90, 66, 150, 75, 70, 60
        ]

        self.lista_edades = [
            55, 46, 18, 12, 47, 42, 99, 35, 37, 90
        ]

    def btn_cargar_viajeros_on_click(self):
        self.lista_viajeros = []
        for _ in range(5):
            nombre = prompt("Ingrese el nombre del viajero:")
            altura = int(prompt("Ingrese la altura del viajero (entre 60 cm y 200 cm):"))
            while altura < 60 or altura > 200:
                altura = int(prompt("Altura inválida. Ingrese la altura del viajero (entre 60 cm y 200 cm):"))

            peso = int(prompt("Ingrese el peso del viajero (entre 40 kg y 250 kg):"))
            while peso < 40 or peso > 250:
                peso = int(prompt("Peso inválido. Ingrese el peso del viajero (entre 40 kg y 250 kg):"))

            edad = int(prompt("Ingrese la edad del viajero (entre 1 y 100):"))
            while edad < 1 or edad > 100:
                edad = int(prompt("Edad inválida. Ingrese la edad del viajero (entre 1 y 100):"))

            self.lista_viajeros.append((nombre, altura, peso, edad))

    def btn_mostrar_datos_crudo_on_click(self):
        for i, viajero in enumerate(self.lista_viajeros):
            print(f"Posición {i + 1}: {viajero}")

    def btn_mostrar_informe_1_on_click(self):
        informe_numero = int(NOMBRE[-1]) % 2 

        if informe_numero == 0:
            persona_menor_peso = self.obtener_persona_menor_peso()
            cantidad_personas_mas_50 = sum(1 for viajero in self.lista_viajeros if viajero[3] > 50)

            print(f"A- Nombre de la persona con el menor peso ingresado: {persona_menor_peso[0]}")
            print(f"B- Cantidad de personas de más de 50 años: {cantidad_personas_mas_50}")

        elif informe_numero == 1:
            persona_mayor_peso = self.obtener_persona_mayor_peso()
            cantidad_personas_menos_50 = sum(1 for viajero in self.lista_viajeros if viajero[3] < 50)

            print(f"A- Nombre de la persona con el mayor peso ingresado: {persona_mayor_peso[0]}")
            print(f"B- Cantidad de personas de menos de 50 años: {cantidad_personas_menos_50}")
        
    def obtener_persona_menor_peso(self):
        menor_peso = float('inf')
        persona_menor_peso = None

        for viajero in self.lista_viajeros:
            peso_actual = viajero[2]
            if peso_actual < menor_peso:
                menor_peso = peso_actual
                persona_menor_peso = viajero

        return persona_menor_peso

    def obtener_persona_mayor_peso(self):
        mayor_peso = float('-inf')
        persona_mayor_peso = None

        for viajero in self.lista_viajeros:
            peso_actual = viajero[2]
            if peso_actual > mayor_peso:
                mayor_peso = peso_actual
                persona_mayor_peso = viajero

        return persona_mayor_peso
    
    def btn_mostrar_informe_2_on_click(self):
        informe_numero = int(NOMBRE[-1]) % 2 

        if informe_numero == 0:
            persona_mayor_altura = self.obtener_persona_mayor_altura()
            cantidad_personas_mas_80_kilos = sum(1 for viajero in self.lista_viajeros if viajero[2] > 80)

            print(f"A- Nombre de la persona con la mayor altura ingresada: {persona_mayor_altura[0]}")
            print(f"B- Cantidad de personas de más de 80 kilos: {cantidad_personas_mas_80_kilos}")

        elif informe_numero == 1:
            persona_menor_altura = self.obtener_persona_menor_altura()
            cantidad_personas_menos_100_kilos = sum(1 for viajero in self.lista_viajeros if viajero[2] < 100)

            print(f"A- Nombre de la persona con la menor altura ingresada: {persona_menor_altura[0]}")
            print(f"B- Cantidad de personas de menos de 100 kilos: {cantidad_personas_menos_100_kilos}")

    def obtener_persona_mayor_altura(self):
        mayor_altura = float('-inf')
        persona_mayor_altura = None

        for viajero in self.lista_viajeros:
            altura_actual = viajero[1]
            if altura_actual > mayor_altura:
                mayor_altura = altura_actual
                persona_mayor_altura = viajero

        return persona_mayor_altura

    def obtener_persona_menor_altura(self):
        menor_altura = float('inf')
        persona_menor_altura = None

        for viajero in self.lista_viajeros:
            altura_actual = viajero[1]
            if altura_actual < menor_altura:
                menor_altura = altura_actual
                persona_menor_altura = viajero

        return persona_menor_altura

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
