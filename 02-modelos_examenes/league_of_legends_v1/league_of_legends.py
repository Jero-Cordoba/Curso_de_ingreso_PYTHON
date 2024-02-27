import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import warnings

'''
################# INTRODUCCION #################
#? Un jugador de League of Legends tiene un fin de semana libre y 
#? va a jugar partidas hasta que se canse.
'''
NOMBRE = 'Jerónimo Córdoba' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
Para ello deberas programar el boton "Cargar Campeones" para poder cargar 10 personajes del juego.
Para mejorar su jugabilidad, por cada partida jugada va a registrar:
    * Modo de juego ("Normal", "Clasificatoria", "ARAM")
    * Nombre del personaje que usó
    * La cantidad de asesinatos a favor (No puede ser negativo)
    * Muertes en contra (No puede ser negativo)
    * Asistencias a favor. (No puede ser negativo, hasta 40)
    
B)  Al presionar el boton "Mostrar Informe 1" se deberan listar los Campeones
        y su posicion en la lista (por terminal), 
        adicionalmente mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) Al presionar el boton "Mostrar Informe 2"
    #! 0) - El modo de juego más jugado.
    #! 1) - El modo de juego menos jugado.
    #! 2) - El personaje con el cual murió más.
    #! 3) - El personaje con el cual asistio más.
    #! 4) - El promedio de asesinatos a favor en modo Clasificatoria.
    #! 5) - El promedio de muertes en contra en modo ARAM.
    #! 6) - El promedio de asistencias en modo Normal.
    #! 7) - De la partida con mas muertes en contra, el nombre del personaje y el modo de juego.
    #! 8) - De la partida con mas asistencias a favor, el nombre del personaje y el modo de juego.
    #! 9) - De la partida con mas asesinatos a favor, el nombre del personaje y el modo de juego.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - League of {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"League of {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/league_of_legends_v1/UTN_LoL_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Campeones", command=self.btn_cargar_campeones_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para el boton mostrar
        # Cargar aca los pokemones
        self.lista_nombre_campeones = [
            "Jinx", "Akali", "Ashe", "Vladimir", "Kalista",
            "Teemo", "Annie", "Zed", "Katarina", "Hecarim"
        ]
        self.lista_asesinatos_a_favor = [
            9, 7, 7, 4, 12, 20, 5, 7, 14, 15
        ]
        self.lista_asistencias_a_favor = [
            4, 5, 9, 1, 0, 2, 10, 8, 5, 9
        ]

        self.lista_muertes_en_contra = [
            6, 8, 9, 3, 2, 1, 4, 5, 9, 2
        ]

        self.lista_modo_de_juego = [
            "ARAM", "ARAM", "Clasificatoria", "Normal", "Clasificatoria",
            "Clasificatoria", "ARAM", "Clasificatoria", "Normal", "Clasificatoria",
        ]

    def btn_cargar_campeones_on_click(self):
        self.lista_modo_de_juego = []
        self.lista_nombre_campeones = []
        self.lista_asesinatos_a_favor = []
        self.lista_muertes_en_contra = []
        self.lista_asistencias_a_favor = []

        for i in range(10):
            modalidad = prompt("Ingrese el modo de juego (Normal, Clasificatoria, ARAM): ").capitalize()
            while modalidad not in ["Normal", "Clasificatoria", "ARAM"]:
                alert("Modo de juego no válido. Intente nuevamente.")
                modalidad = prompt("Ingrese el modo de juego (Normal, Clasificatoria, ARAM): ").capitalize()

            campeon = prompt("Ingrese el nombre del campeón: ")
            asesinatos = int(prompt("Ingrese la cantidad de asesinatos a favor (no puede ser negativo): "))
            while asesinatos < 0:
                alert("Cantidad de asesinatos no válida. Intente nuevamente.")
                asesinatos = int(prompt("Ingrese la cantidad de asesinatos a favor (no puede ser negativo): "))

            muertes = int(prompt("Ingrese la cantidad de muertes en contra (no puede ser negativo): "))
            while muertes < 0:
                alert("Cantidad de muertes no válida. Intente nuevamente.")
                muertes = int(prompt("Ingrese la cantidad de muertes en contra (no puede ser negativo): "))

            asistencias = int(prompt("Ingrese la cantidad de asistencias a favor (no puede ser negativo, hasta 40): "))
            while asistencias < 0 or asistencias > 40:
                alert("Cantidad de asistencias no válida. Intente nuevamente.")
                asistencias = int(prompt("Ingrese la cantidad de asistencias a favor (no puede ser negativo, hasta 40): "))    
            
            self.lista_modo_de_juego.append(modalidad)
            self.lista_nombre_campeones.append(campeon)
            self.lista_asesinatos_a_favor.append(asesinatos)
            self.lista_muertes_en_contra.append(muertes)
            self.lista_asistencias_a_favor.append(asistencias)
            alert("Datos cargados exitosamente.")

    def btn_mostrar_informe_1_on_click(self):
        print("Informe 1:")
        for i, campeon in enumerate(self.lista_nombre_campeones, 1):
            print(f"{i}. {campeon}")
            dni = int(NOMBRE.split()[-1][-1])
            informe_number = dni if dni <= 4 else 9 - dni
            print(f"Realizar informe {informe_number}")
    
    def btn_mostrar_informe_2_on_click(self):
        print("Informe 2:")
    
        print(f"0) Modo de juego más jugado: {self.modo_mas_jugado()}")
        
        print(f"1) Modo de juego menos jugado: {self.modo_menos_jugado()}")
        
        print(f"2) Personaje con el cual murió más: {self.personaje_con_mas_muertes()}")
        
        print(f"3) Personaje con el cual asistió más: {self.personaje_con_mas_asistencias()}")
        
        print(f"4) Promedio de asesinatos a favor en modo Clasificatoria: {self.promedio_asesinatos_modo('Clasificatoria')}")
        
        print(f"5) Promedio de muertes en contra en modo ARAM: {self.promedio_muertes_modo('ARAM')}")
        
        print(f"6) Promedio de asistencias en modo Normal: {self.promedio_asistencias_modo('Normal')}")
        
        partida_mas_muertes_info = self.partida_mas_muertes()
        print(f"7) De la partida con más muertes en contra: {partida_mas_muertes_info}")
        
        partida_mas_asistencias_info = self.partida_mas_asistencias()
        print(f"8) De la partida con más asistencias a favor: {partida_mas_asistencias_info}")
        
        partida_mas_asesinatos_info = self.partida_mas_asesinatos()
        print(f"9) De la partida con más asesinatos a favor: {partida_mas_asesinatos_info}")

    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()
        
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
