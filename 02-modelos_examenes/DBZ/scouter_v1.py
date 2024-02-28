import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import warnings

'''
################# INTRODUCCION #################
#? El presentador del torneo de artes marciales quiere que desarrolles un modelo prototipico 
#? de scouter (un detector basicamente) para ver ciertas metricas de los participantes.
#? de cualquier parte del universo, es por eso que deberas realizar la carga 
#? de 10 participantes.
'''
NOMBRE = 'Jerónimo Córdoba' 
'''
#?################ ENUNCIADO #################
Para ello deberas programar el boton "Cargar Participantes" para poder cargar 10 luchadoras/es.
Los datos que deberas pedir para los luchadoras/es son:
    * El nombre del luchador/a.
    * El tipo de raza (Terricola , Namekiano, Alienigena , Saiyajin).
    * La cantidad de poder del participante (entre 100 y 5000).
    
B)  Al presionar el boton "Mostrar Informe 1" se deberan listar los participantes
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
    #! 0) - Cantidad de luchadores Terricolas.
    #! 1) - Cantidad de luchadores Alienigenas.
    #! 2) - Nombre, Raza y Poder del luchador mas fuerte.
    #! 3) - Nombre, Raza y Poder del luchador mas debil.
    #! 4) - Cantidad de luchadores con mas de 2500 de poder.
    #! 5) - Cantidad de luchadores con menos de 2500 de poder.
    #! 6) - Raza que mas luchadores posea inscriptos.
    #! 7) - Raza que menos luchadores posea inscriptos.
    #! 8) - el promedio de poder de todos los luchadores inscriptos.
    #! 9) - el promedio de poder de todos los luchadores Saiyajines.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Scouter de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Scouter de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/scouter_v1/UTN_Scouter_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Participantes", command=self.btn_cargar_participantes_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para el boton mostrar
        # Cargar aca los pokemones
        self.lista_nombre_participantes = [
            "Vegeta", "Goku", "Yamcha", "Pikoro", "Gohan",
            "Frieza", "Appule", "Krilin", "Roshi", "Dende"
        ]
        self.lista_raza_participantes = [
            "Saiyajin", "Saiyajin", "Terricola", "Namekiano", "Saiyajin",
            "Alienigena", "Alienigena", "Terricola", "Terricola", "Namekiano",
        ]
        self.lista_poder_participantes = [
            4900, 4800, 200, 4500, 3500, 5000, 600, 550, 450, 610
        ]

    def btn_cargar_participantes_on_click(self):
        for i in range(10):
            nombre = prompt("Ingrese el nombre del luchador/a:")
            raza = prompt("Ingrese el tipo de raza (Terricola, Namekiano, Alienigena, Saiyajin):")
            
            while True:
                try:
                    poder = int(prompt("Ingrese la cantidad de poder del participante (entre 100 y 5000):"))
                    if 100 <= poder <= 5000:
                        break
                    else:
                        alert("El poder debe estar entre 100 y 5000. Inténtelo nuevamente.")
                except ValueError:
                    alert("Por favor, ingrese un valor numérico válido para el poder.")

            self.lista_nombre_participantes.append(nombre)
            self.lista_raza_participantes.append(raza)
            self.lista_poder_participantes.append(poder)
        
    def btn_mostrar_informe_1_on_click(self):
        for i in range(len(self.lista_nombre_participantes)):
            nombre = self.lista_nombre_participantes[i]
            raza = self.lista_raza_participantes[i]
            poder = self.lista_poder_participantes[i]

        print(f"Posición {i + 1}: {nombre} - Raza: {raza} - Poder: {poder}")
    
    def btn_mostrar_informe_2_on_click(self):
        terricolas = 0; aliens = 0
        nombre_mas_fuerte = ""; raza_mas_fuerte = ""
        poder_mas_fuerte = 0
        nombre_mas_debil = ""; raza_mas_debil = ""
        poder_mas_debil = float('inf')
        poder_2500 = 0

        for i in range(len(self.lista_nombre_participantes)):
            raza = self.lista_raza_participantes[i]
            poder = self.lista_poder_participantes[i]

            if raza == "Terricola":
                terricolas += 1

            elif raza == "Alienigena":
                aliens += 1

            if poder > poder_mas_fuerte:
                nombre_mas_fuerte = self.lista_nombre_participantes[i]
                raza_mas_fuerte = raza
                poder_mas_fuerte = poder

            if poder < poder_mas_debil:
                nombre_mas_debil = self.lista_nombre_participantes[i]
                raza_mas_debil = raza
                poder_mas_debil = poder

            if poder > 2500:
                poder_2500 += 1

        print(f"0) Cantidad de luchadores Terricolas: {terricolas}")
        print(f"1) Cantidad de luchadores Alienigenas: {aliens}")
        print(f"2) Luchador más fuerte - Nombre: {nombre_mas_fuerte}, Raza: {raza_mas_fuerte}, Poder: {poder_mas_fuerte}")
        print(f"3) Luchador más débil - Nombre: {nombre_mas_debil}, Raza: {raza_mas_debil}, Poder: {poder_mas_debil}")
        print(f"4) Cantidad de luchadores con más de 2500 de poder: {poder_2500}")
    
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()
    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
