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
Para ello deberas programar el boton "Cargar Guerreros" para poder cargar 10 Caballeros del zodiaco.
Los datos que deberas pedir para los Caballeros del zodiaco son:
    * El nombre del Caballeros del zodiaco.
    * El tipo de armadura (Bronce, Plata, Oro, Divina, Oscura).
    * La cantidad de cosmos del guerrero (entre 25000 y 150000).
    
B)  Al presionar el boton "Mostrar Informe 1" se deberan listar los Caballeros del zodiaco
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
    #! 0) - Cantidad de guerreros de armadura de Oro.
    #! 1) - Cantidad de guerreros de armadura Divina.
    #! 2) - Nombre, Armadura y Cosmos del guerrero mas fuerte.
    #! 3) - Nombre, Raza y Poder del guerrero mas debil.
    #! 4) - Cantidad de guerreros con mas de 85000 de poder y armadura de Plata.
    #! 5) - Cantidad de guerreros con menos de 50000 de poder y armadura de Bronce.
    #! 6) - Armadura que mas guerreros posea inscriptos.
    #! 7) - Armadura que menos guerreros posea inscriptos.
    #! 8) - el promedio de cosmos de todos los guerreros con armadura Oscura.
    #! 9) - el porcentaje, tipo de armadura y promedio de cosmos de guerreros 
    #!      de cada tipo de armadura, respecto al total de guerreros.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Saint Seiya {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"{NOMBRE} de la constelacion Uteneana", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/saint_seiya_v1/UTN_SaintSeiya_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Caballeros del Zodíaco", command=self.btn_cargar_participantes_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        self.lista_nombre_guerreros = [
            "Hades", "Hyoga", "Ikki", "Ichi", "Tenma",
            "Athena", "Poseidon", "Shaina", "Marin", "Orpheo"
        ]
        self.lista_tipo_armadura_guerreros = [
            "Divina", "Oscura", "Bronce", "Plata", "Bronce",
            "Divina", "Divina", "Plata", "Plata", "Plata",
        ]
        self.lista_cosmos_guerreros = [
            149000, 48000, 25000, 45000, 35000, 150000, 140000, 55000, 45000, 61000
        ]

    def btn_cargar_participantes_on_click(self):
        for _ in range(10):
            nombre = prompt("Ingrese el nombre del Caballero del Zodíaco:")
            tipo_armadura = prompt("Ingrese el tipo de armadura (Bronce, Plata, Oro, Divina, Oscura):")
            cosmos = int(prompt("Ingrese la cantidad de cosmos del guerrero (entre 25000 y 150000):"))

            while cosmos < 25000 or cosmos > 150000:
                alert("La cantidad de cosmos debe estar entre 25000 y 150000.")
                cosmos = int(prompt("Ingrese la cantidad de cosmos del guerrero (entre 25000 y 150000):"))

            self.lista_nombre_guerreros.append(nombre)
            self.lista_tipo_armadura_guerreros.append(tipo_armadura.capitalize())
            self.lista_cosmos_guerreros.append(cosmos)

        alert("Los datos se cargaron correctamente.")
        
    def btn_mostrar_informe_1_on_click(self):
        print("Informe 1:")
        for i in range(len(self.lista_nombre_guerreros)):
            nombre = self.lista_nombre_guerreros[i]
            tipo_armadura = self.lista_tipo_armadura_guerreros[i]
            cosmos = self.lista_cosmos_guerreros[i]
            print(f"Caballero {i + 1}: {nombre} - Armadura: {tipo_armadura} - Cosmos: {cosmos}")
    
    def btn_mostrar_informe_2_on_click(self):
        print("Informe 2:")
        gold_armor = self.lista_tipo_armadura_guerreros.count("Oro")

        celestials_armor = self.lista_tipo_armadura_guerreros.count("Divina")

        max_cosmos_index = self.lista_cosmos_guerreros.index(max(self.lista_cosmos_guerreros))
        max_cosmos_info = (
            self.lista_nombre_guerreros[max_cosmos_index],
            self.lista_tipo_armadura_guerreros[max_cosmos_index],
            self.lista_cosmos_guerreros[max_cosmos_index]
        )

        min_cosmos_index = self.lista_cosmos_guerreros.index(min(self.lista_cosmos_guerreros))
        min_cosmos_info = (
            self.lista_nombre_guerreros[min_cosmos_index],
            self.lista_tipo_armadura_guerreros[min_cosmos_index],
            self.lista_cosmos_guerreros[min_cosmos_index]
        )

        iron_armor = sum(1 for i in range(len(self.lista_cosmos_guerreros)) if
                                        self.lista_cosmos_guerreros[i] > 85000 and self.lista_tipo_armadura_guerreros[i] == "Plata")

        copper_armor = sum(1 for i in range(len(self.lista_cosmos_guerreros)) if
                                        self.lista_cosmos_guerreros[i] < 50000 and self.lista_tipo_armadura_guerreros[i] == "Bronce")

        armadura_mas_guerreros = max(set(self.lista_tipo_armadura_guerreros), key=self.lista_tipo_armadura_guerreros.count)

        armadura_menos_guerreros = min(set(self.lista_tipo_armadura_guerreros), key=self.lista_tipo_armadura_guerreros.count)

        dark_armor = [cosmos for i, cosmos in enumerate(self.lista_cosmos_guerreros) if
                                self.lista_tipo_armadura_guerreros[i] == "Oscura"]
        promedio_cosmos_oscura = sum(dark_armor) / len(dark_armor) if dark_armor else 0

        tipos_armadura = set(self.lista_tipo_armadura_guerreros)
        for tipo_armadura in tipos_armadura:
            count_tipo_armadura = self.lista_tipo_armadura_guerreros.count(tipo_armadura)
            porcentaje_tipo_armadura = (count_tipo_armadura / len(self.lista_tipo_armadura_guerreros)) * 100

            tipos_armaduras = [cosmos for i, cosmos in enumerate(self.lista_cosmos_guerreros) if
                                    self.lista_tipo_armadura_guerreros[i] == tipo_armadura]
            promedio_tipos_armaduras = sum(tipos_armaduras) / len(tipos_armaduras) if tipos_armaduras else 0

            print(f"{tipo_armadura}: {porcentaje_tipo_armadura}% - Promedio Cosmos: {promedio_tipos_armaduras}")

        print(f"0) Cantidad de guerreros de armadura de Oro: {gold_armor}")
        print(f"1) Cantidad de guerreros de armadura Divina: {celestials_armor}")
        print(f"2) Guerrero más fuerte: Nombre: {max_cosmos_info[0]}, Armadura: {max_cosmos_info[1]}, Cosmos: {max_cosmos_info[2]}")
        print(f"3) Guerrero más débil: Nombre: {min_cosmos_info[0]}, Armadura: {min_cosmos_info[1]}, Cosmos: {min_cosmos_info[2]}")
        print(f"4) Cantidad de guerreros con más de 85000 de poder y armadura de Plata: {iron_armor}")
        print(f"5) Cantidad de guerreros con menos de 50000 de poder y armadura de Bronce: {copper_armor}")
        print(f"6) Armadura que más guerreros posea inscriptos: {armadura_mas_guerreros}")
        print(f"7) Armadura que menos guerreros posea inscriptos: {armadura_menos_guerreros}")
        print(f"8) Promedio de cosmos de todos los guerreros con armadura Oscura: {promedio_cosmos_oscura}")
        print(f"9) Cantidad de armaduras de cada tipo:" + "\n" + str(tipos_armadura))
    
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()
    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
