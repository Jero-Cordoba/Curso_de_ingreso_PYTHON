import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import warnings

'''
################# INTRODUCCION #################
#? El profesor OAK de pueblo paleta quiere que construyas un segundo modelo prototipico 
#? de pokedex con 10 pokemones de prueba.
'''
NOMBRE = 'Jerónimo Córdoba' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon.
    * El tipo de color (azul , amarillo, blanco , otro).
    * La altura del pokemon en centimetros (validar que sea mayor a 10 y menor a 200).
    
B)  Al presionar el boton "Mostrar Informe 1" se deberan listar los pokemones y su posicion en la 
    lista (por terminal), adicionalmente mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) Al presionar el boton "Mostrar Informe 2"
    #! 0) - Cantidad de pokemones de color amarillo.
    #! 1) - Cantidad de pokemones de color blanco.
    #! 2) - Nombre, color y altura del pokemon mas alto.
    #! 3) - Nombre, color y altura del pokemon mas bajo.
    #! 4) - Cantidad de pokemones con mas de 100 cm de altura.
    #! 5) - Cantidad de pokemones con menos de 100 cm de altura.
    #! 6) - color de los pokemones del color que mas pokemones posea.
    #! 7) - color de los pokemones del color que menos pokemones posea.
    #! 8) - el promedio de altura de todos los pokemones ingresados.
    #! 9) - el promedio de altura de todos los pokemones azules.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Pokedex de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Pokedex de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/pokedex_v2/UTN_Pokedex_App_v2.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para el boton mostrar
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = [
            "Togepi", "Vulpix Alola", "Pikachu", "Zapdos", "Lapras",
            "Moltres", "Mew", "Blastoise", "Articuno", "Vaporeon"
        ]
        self.lista_altura_pokemones = [
            60, 70, 50, 199, 180, 198, 80, 145, 197, 90
        ]
        self.lista_color_pokemones = [
            "Blanco", "Blanco", "Amarillo", "Amarillo", "Azul",
            "Otro", "Otro", "Azul", "Azul", "Azul"
        ]

    def btn_cargar_pokedex_on_click(self):
        self.lista_nombre_pokemones = []
        self.lista_altura_pokemones = []
        self.lista_color_pokemones = []

        for _ in range(10):
            nombre = prompt("Ingrese el nombre del pokemon:")
            color = ""
            while color not in ["azul", "amarillo", "blanco", "otro"]:
                color = prompt("Ingrese el color del pokemon (azul, amarillo, blanco, otro):").lower()

            altura = 0
            while not (10 < altura < 200):
                try:
                    altura = int(prompt("Ingrese la altura del pokemon en centímetros (entre 10 y 200):"))
                except ValueError:
                    altura = 0

            self.lista_nombre_pokemones.append(nombre)
            self.lista_color_pokemones.append(color.capitalize())  # Convertir la primera letra a mayúscula
            self.lista_altura_pokemones.append(altura)

        alert("Pokedex cargada con éxito.")
        
    def btn_mostrar_informe_1_on_click(self):
        print("Lista de Pokemones:")
        for i in range(len(self.lista_nombre_pokemones)):
            nombre = self.lista_nombre_pokemones[i]
            color = self.lista_color_pokemones[i]
            altura = self.lista_altura_pokemones[i]
            print(f"{i+1}. {nombre}, Color: {color}, Altura: {altura} cm")
    
    def btn_mostrar_informe_2_on_click(self):
        cantidad_amarillo = self.lista_color_pokemones.count("Amarillo")
        print(f"Informe 0: Cantidad de pokemones de color amarillo: {cantidad_amarillo}")

        cantidad_blanco = self.lista_color_pokemones.count("Blanco")
        print(f"Informe 1: Cantidad de pokemones de color blanco: {cantidad_blanco}")

        max_altura_index = self.lista_altura_pokemones.index(max(self.lista_altura_pokemones))
        nombre_alto = self.lista_nombre_pokemones[max_altura_index]
        color_alto = self.lista_color_pokemones[max_altura_index]
        altura_alto = self.lista_altura_pokemones[max_altura_index]
        print(f"Informe 2: Pokemon más alto - Nombre: {nombre_alto}, Color: {color_alto}, Altura: {altura_alto} cm")

        min_altura_index = self.lista_altura_pokemones.index(min(self.lista_altura_pokemones))
        nombre_bajo = self.lista_nombre_pokemones[min_altura_index]
        color_bajo = self.lista_color_pokemones[min_altura_index]
        altura_bajo = self.lista_altura_pokemones[min_altura_index]
        print(f"Informe 3: Pokemon más bajo - Nombre: {nombre_bajo}, Color: {color_bajo}, Altura: {altura_bajo} cm")

        cantidad_altura_mas_100 = sum(altura > 100 for altura in self.lista_altura_pokemones)
        print(f"Informe 4: Cantidad de pokemones con más de 100 cm de altura: {cantidad_altura_mas_100}")

        cantidad_altura_menos_100 = sum(altura < 100 for altura in self.lista_altura_pokemones)
        print(f"Informe 5: Cantidad de pokemones con menos de 100 cm de altura: {cantidad_altura_menos_100}")

    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()
    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
