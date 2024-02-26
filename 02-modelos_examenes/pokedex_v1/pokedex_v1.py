import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import warnings
import customtkinter

'''
################# INTRODUCCION #################
#? El profesor OAK de pueblo paleta quiere que construyas un primer modelo prototipico 
#? de pokedex con 10 pokemones de prueba.
'''
NOMBRE = 'Jerónimo Córdoba' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)

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
    #! 0) - Cantidad de pokemones de tipo Fuego
    #! 1) - Cantidad de pokemones de tipo Electrico
    #! 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    #! 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    #! 4) - Cantidad de pokemones, con mas de 100 de poder.
    #! 5) - Cantidad de pokemones, con menos de 100 de poder
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea 
    #! 8) - el promedio de poder de todos los ingresados
    #! 9) - el promedio de poder de todos los pokemones de Electrico
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Pokedex de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Pokedex de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/pokedex_v1/UTN_Pokedex_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para boton mostrar
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = [
            "Charmander", "Charizard", "Pikachu", "Zapdos", "Mewtwo",
            "Moltres", "Mew", "Blastoise", "Raichu", "Digglet"
        ]
        self.lista_poder_pokemones = [
            60, 120, 51, 190, 194,
            190, 195, 120, 95, 51
        ]
        self.lista_tipo_pokemones = [
            "Fuego", "Fuego", "Electrico", "Electrico", "Psiquico",
            "Fuego", "Psiquico", "Agua", "Electrico", "Tierra"
        ]

    def btn_cargar_pokedex_on_click(self):
            for i in range(10):
                nombre = prompt("Poke-Ejercicio", "Ingrese el nombre del pokemon")
                
                tipo = prompt("Poke-Ejercicio", "Ingrese el tipo del pokemon")
                while tipo not in ["Agua", "Electrico", "Fuego", "Psiquico", "Tierra"]:
                    alert("Poke-Ejercicio", "Tipo invalido")
                    tipo = prompt("Poke-Ejercicio", "Ingrese el tipo del pokemon")
                    
                poder = int(prompt("Poke-Ejercicio", "Ingrese el poder del pokemon"))
                while poder < 50 or poder > 200:
                    alert("Poke-Ejercicio", "Poder invalido")
                    poder = int(prompt("Poke-Ejercicio", "Ingrese el poder del pokemon"))
                    
                self.lista_nombre_pokemones.append(nombre)
                self.lista_poder_pokemones.append(poder)
                self.lista_tipo_pokemones.append(tipo)

                alert("Se cargaron correctamente los datos.")
    
    def btn_mostrar_informe_1_on_click(self):
        print("Informe 1:")
        for i, pokemon in enumerate(self.lista_nombre_pokemones, 1):
            print(f"{i}. {pokemon}")
    
    def btn_mostrar_informe_2_on_click(self):
        print("Informe 2:")
        tipo_fuego = 0; tipo_electrico = 0
        pokemones_mas_poderoso = {"Nombre": "", "Tipo": "", "Poder": 0}
        pokemones_menos_poderoso = {"Nombre": "", "Tipo": "", "Poder": float('inf')}
        total_poder_mayor_100 = 0; total_poder_menor_100 = 0
        tipos = {"Agua": 0, "Tierra": 0, "Psiquico": 0, "Fuego": 0, "Electrico": 0}
        total_poder = 0; total_poder_electrico = 0
        count_pokemon = len(self.lista_nombre_pokemones)

        for i in range(count_pokemon):
            if self.lista_tipo_pokemones[i] == "Fuego":
                tipo_fuego += 1
            elif self.lista_tipo_pokemones[i] == "Electrico":
                tipo_electrico += 1
            
            if self.lista_poder_pokemones[i] > pokemones_mas_poderoso["Poder"]:
                pokemones_mas_poderoso["Nombre"] = self.lista_nombre_pokemones[i]
                pokemones_mas_poderoso["Tipo"] = self.lista_tipo_pokemones[i]
                pokemones_mas_poderoso["Poder"] = self.lista_poder_pokemones[i]
            
            if self.lista_poder_pokemones[i] < pokemones_menos_poderoso["Poder"]:
                pokemones_menos_poderoso["Nombre"] = self.lista_nombre_pokemones[i]
                pokemones_menos_poderoso["Tipo"] = self.lista_tipo_pokemones[i]
                pokemones_menos_poderoso["Poder"] = self.lista_poder_pokemones[i]
                
            if self.lista_poder_pokemones[i] > 100:
                total_poder_mayor_100 += 1
            
            if self.lista_poder_pokemones[i] < 100:
                total_poder_menor_100 += 1
            
            tipos[self.lista_tipo_pokemones[i]] += 1
        
            tipos[self.lista_tipo_pokemones[i]] += 1
            
            total_poder += self.lista_poder_pokemones[i]
            
            if self.lista_tipo_pokemones[i] == "Electrico":
                total_poder_electrico += self.lista_poder_pokemones[i]

        tipo_mas_pokemones = max(tipos, key=tipos.get)
        
        tipo_menos_pokemones = min(tipos, key=tipos.get)

        promedio_poder = total_poder / count_pokemon

        if tipo_electrico > 0:
            promedio_poder_electrico = total_poder_electrico / tipo_electrico
        else:
            promedio_poder_electrico = 0

        print(f"0) Cantidad de pokemones de tipo Fuego: {tipo_fuego}")
        print(f"1) Cantidad de pokemones de tipo Electrico: {tipo_electrico}")
        print(f"2) Nombre, tipo y Poder del pokemon con el poder mas alto: {pokemones_mas_poderoso}")
        print(f"3) Nombre, tipo y Poder del pokemon con el poder mas bajo: {pokemones_menos_poderoso}")
        print(f"4) Cantidad de pokemones, con mas de 100 de poder: {total_poder_mayor_100}")
        print(f"5) Cantidad de pokemones, con menos de 100 de poder: {total_poder_menor_100}")
        print(f"6) Tipo de los pokemones del tipo que mas pokemones posea: {tipo_mas_pokemones}")
        print(f"7) Tipo de los pokemones del tipo que menos pokemones posea: {tipo_menos_pokemones}")
        print(f"8) El promedio de poder de todos los ingresados: {promedio_poder}")
        print(f"9) El promedio de poder de todos los pokemones de Electrico: {promedio_poder_electrico}")
    
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()
    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
