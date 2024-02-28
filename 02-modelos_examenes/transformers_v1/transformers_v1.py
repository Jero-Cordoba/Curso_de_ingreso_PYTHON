import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import warnings

import customtkinter

'''
################# INTRODUCCION #################
#? En Cybertron se requiere contabilizar los transformers que hay en guerra 
#? para ello habra que construir un programita que ayude con esa cuestion y 
#? recobrar la paz.
'''
NOMBRE = 'Jerónimo Córdoba' 
'''
#?################ ENUNCIADO #################
Es por eso que deberas programar el boton "Cargar Transformer" para poder cargar 10 robots.
Los datos que deberas pedir para los transformers son:
    * El nombre del transformer
    * El bando del transformer (Autobot, Maximal, Predacon, Descepticon, Terrorcon)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)
    * La altura (en metros enteros [sin decimales]) del transformer (Validar que sea mayor a 5 y menor a 50)
    * El peso (en toneladas) del transformer (Validar que sea mayor a 20 y menor a 500)

B) Al presionar el boton "Mostrar Informe 1" se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) Al presionar el boton "Mostrar Informe 2"
    #! 0) - Cantidad de Transformers del bando Autobots
    #! 1) - Cantidad de Transformers del bando Maximals
    #! 2) - Nombre, bando, poder, altura y peso del Transformer con el poder mas alto
    #! 3) - Nombre, bando, poder, altura y peso del Transformer con el peso mas bajo
    #! 4) - Cantidad de Transformers, con mas de 150 de poder.
    #! 5) - Cantidad de Transformers, con menos de 25 metros de altura
    #! 6) - Bando de los Transformers del bando que mas Transformers posea 
    #! 7) - Bando de los Transformers del Bando que menos Transformers posea 
    #! 8) - el promedio de poder de todos los Transformers ingresados
    #! 9) - el promedio de poder de todos los Transformers del bando Descepticon
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Cybertron Manager de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Cybertron Manager de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/transformers_v1/UTN_Transformers_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Transformers", command=self.btn_cargar_transformer_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Ambos Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para boton mostrar
        # Cargar aca los transformers
        self.lista_nombre_transformers = [
            "OptimusPrime", "OptimusPrimal", "Megatron", "Airazor", "Cheetor",
            "Wheeljack", "Starscream", "Bumblebee", "Mirage", "Scourge", "Megatron"
        ]
        self.lista_poder_transformers = [
            200, 199, 198, 140, 150,
            130, 120, 145, 125, 199, 190
        ]
        self.lista_bando_transformers = [
            "Autobot", "Maximal", "Descepticon", "Maximal", "Maximal",
            "Autobot", "Descepticon", "Autobot", "Autobot", "Terrorcon", "Predacon"
        ]
        self.lista_altura_transformers = [
            30, 25, 35, 20, 22,
            20, 16, 12, 15, 40, 34
        ]
        self.lista_peso_transformers = [
            300, 390, 450, 250, 175,
            200, 180, 105, 90, 350, 420
        ]

    def btn_cargar_transformer_on_click(self):
        for _ in range(10):
            nombre = prompt("Ingrese el nombre del Transformer:")
            bando = prompt("Ingrese el bando del Transformer (Autobot, Maximal, Predacon, Descepticon, Terrorcon):")
            poder = int(prompt("Ingrese la cantidad de poder del Transformer (entre 50 y 200):"))
            altura = int(prompt("Ingrese la altura del Transformer en metros (entre 5 y 50):"))
            peso = int(prompt("Ingrese el peso del Transformer en toneladas (entre 20 y 500):"))

            while poder < 50 or poder > 200:
                alert("El poder debe estar entre 50 y 200.")
                poder = int(prompt("Ingrese la cantidad de poder del Transformer (entre 50 y 200):"))

            while altura < 5 or altura > 50:
                alert("La altura debe estar entre 5 y 50 metros.")
                altura = int(prompt("Ingrese la altura del Transformer en metros (entre 5 y 50):"))

            while peso < 20 or peso > 500:
                alert("El peso debe estar entre 20 y 500 toneladas.")
                peso = int(prompt("Ingrese el peso del Transformer en toneladas (entre 20 y 500):"))

        self.lista_nombre_transformers.append(nombre)
        self.lista_bando_transformers.append(bando)
        self.lista_poder_transformers.append(poder)
        self.lista_altura_transformers.append(altura)
        self.lista_peso_transformers.append(peso)
        alert("Los datos se cargaron correctamente.")
        
    def btn_mostrar_informe_1_on_click(self):
        print("Primer Informe:")
        for i in range(len(self.lista_nombre_transformers)):
            nombre = self.lista_nombre_transformers[i]
            bando = self.lista_bando_transformers[i]
            poder = self.lista_poder_transformers[i]
            altura = self.lista_altura_transformers[i]
            peso = self.lista_peso_transformers[i]

            print(f"Transformador {i + 1}: {nombre} - Bando: {bando} - Poder: {poder} - Altura: {altura}m - Peso: {peso} ton")
    
    def btn_mostrar_informe_2_on_click(self):
        print("Segundo Informe:")
    
        todos_autobots = 0
        todos_maximals = 0
        total_poder = 0
        total_altura_azules = 0
        count_azules = 0

        max_altura_transformer = None
        min_altura_transformer = None

        max_poder_transformer = None
        min_poder_transformer = None

        for i in range(len(self.lista_nombre_transformers)):
            nombre = self.lista_nombre_transformers[i]
            bando = self.lista_bando_transformers[i]
            poder = self.lista_poder_transformers[i]
            altura = self.lista_altura_transformers[i]
            peso = self.lista_peso_transformers[i]

        if bando == "Autobot":
            todos_autobots += 1
        elif bando == "Maximal":
            todos_maximals += 1

        total_poder += poder

        if self.lista_color_transformers[i] == "Azul":
            total_altura_azules += altura
            count_azules += 1

        if max_altura_transformer is None or altura > max_altura_transformer:
            max_altura_transformer = altura
            max_altura_transformer_info = (nombre, bando, poder, altura, peso)

        if min_altura_transformer is None or altura < min_altura_transformer:
            min_altura_transformer = altura
            min_altura_transformer_info = (nombre, bando, poder, altura, peso)

        if max_poder_transformer is None or poder > max_poder_transformer:
            max_poder_transformer = poder
            max_poder_transformer_info = (nombre, bando, poder, altura, peso)

        if min_poder_transformer is None or poder < min_poder_transformer:
            min_poder_transformer = poder
            min_poder_transformer_info = (nombre, bando, poder, altura, peso)

            promedio_poder = total_poder / len(self.lista_nombre_transformers)

        if count_azules > 0:
            promedio_altura_azules = total_altura_azules / count_azules
        else:
            promedio_altura_azules = 0 

        print(f"Cantidad de Autobots: {todos_autobots}")
        print(f"Cantidad de Maximals: {todos_maximals}")
        print(f"Transformer más alto: {max_altura_transformer_info}")
        print(f"Transformer más bajo: {min_altura_transformer_info}")
        print(f"Cantidad de Transformers con más de 150 de poder: {sum(poder > 150 for poder in max_poder_transformer_info[2])}")
        print(f"Cantidad de Transformers con menos de 25 metros de altura: {count_azules}")
        print(f"Bando con más Transformers: {'Autobot' if todos_autobots > todos_maximals else 'Maximal'}")
        print(f"Bando con menos Transformers: {'Autobot' if todos_autobots < todos_maximals else 'Maximal'}")
        print(f"Promedio de poder de todos los Transformers: {promedio_poder}")
        print(f"Promedio de poder de Transformers Descepticon: {promedio_altura_azules}")
    
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()
            
    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
