import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import warnings

'''
################# INTRODUCCION #################
#? Se nos ha solicitado desarrollar una aplicación para llevar registro de las 
#? entradas vendidas en el Estadio River Plate, para el concierto de Taylor Swift. 
#? Para ello, se solicitará al usuario la siguiente información al momento de 
#? comprar cada entrada:
'''
NOMBRE = 'Jerónimo  Córdoba' 
'''
#?################ ENUNCIADO #################
Para ello deberas programar el boton "Cargar Ventas" para poder cargar 10 ventas.
Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 


B)  Al presionar el boton "Mostrar Informe 1" se deberan listar las ventas (todos sus datos)
        y su posicion en la lista (por terminal).
        Adicionalmente mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) Al presionar el boton "Mostrar Informe 2"
    #! 0) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 1) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 2) - Calcula el número total de entradas compradas por personas mayores de 30 años y 
    #!          su precio promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa (OMITO).
    #! 5) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito (OMITO)
    #! 6) - Encuentra los nombres y las edades de la personas que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (OMITO)
    #! 7) - Encuentra la cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 8) - Calcula el monto total recaudado por la venta de entradas de tipo "General" y 
    #!          pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5.
    #! 9) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Punto de Venta {NOMBRE} [version 2]")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Punto de Venta {NOMBRE} [Version 2]", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/taylor_swift_v2/UTN_PuntoVenta_App_v2.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Ventas", command=self.btn_cargar_ventas_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para el boton mostrar
        # Cargar aca los pokemones
        self.nombres = [
            "Juan", "María", "Luis", "Ana", "Carlos", "Jose", "Pedro", "Sofía", "Miguel", "Valentina",
            "Andrés", "Lucía", "Fernando", "Gabriela", "Diego", "Martina", "Jorge", "Camila", "Ricardo", "Isabella",
            "José", "Paula", "Manuel", "Alejandra", "Santiago", "Daniela", "Gustavo", "Carolina", "Emilio", "Antonella",
            "Pablo", "Valeria", "Eduardo", "Florencia", "Alberto", "Agustina", "Raul", "Rocio", "Javier", "Marina",
            "Sebastian", "Catalina", "Rafael", "Carmen", "Rodrigo", "Elena", "Oscar", "Pilar", "Hugo", "Juana",
            "Guillermo", "Natalia", "Francisco", "Constanza", "Hector", "Adriana", "Victor", "Anita", "Lorenzo", "Estela",
            "Enrique", "Diana", "Fabian", "Patricia", "Felipe", "Claudia", "Camilo", "Teresa", "Samuel", "Rosa",
            "Joaquin", "Monica", "Lucas", "Ines", "Omar", "Gloria", "Mariano", "Silvia", "Nicolas", "Alicia",
            "Federico", "Olga", "Arturo", "Amparo", "Julio", "Elsa", "Alfredo", "Beatriz", "Elias", "Rita",
            "Benjamin", "Margarita", "Agustin", "Dolores", "Dario", "Lourdes", "Gerardo", "Manuela", "Feliciano", "Marta"
        ]

        self.edades = [
            25, 33, 20, 29, 50, 40, 22, 28, 35, 18, 26, 21, 30, 32, 19, 27, 24, 38, 31, 23,
            29, 17, 28, 34, 20, 25, 22, 33, 40, 16, 19, 37, 24, 28, 31, 21, 33, 18, 29, 26,
            35, 20, 23, 39, 30, 27, 22, 36, 28, 32, 31, 19, 24, 20, 25, 33, 40, 27, 21, 39,
            29, 22, 36, 30, 19, 25, 21, 38, 34, 17, 32, 18, 23, 27, 22, 40, 36, 29, 20, 33,
            31, 35, 24, 19, 28, 30, 26, 37, 33, 21, 25, 29, 16, 38, 40, 50, 27, 30, 32, 24
        ]

        self.generos = [
            "Masculino", "Femenino", "Masculino", "Femenino", "Otro", "Masculino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"
        ]

        self.tipo_entrada = [
            "General", "Campo delantero", "Platea", "General", "Platea", "General", "General", "Platea", "Campo delantero", "General",
            "Campo delantero", "Platea", "General", "General", "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "General", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero"
        ]

        # Lista de medio de pago (Credito, Debito, Efectivo)
        self.medio_pago = [
            "Credito", "Debito", "Efectivo", "Credito", "Efectivo", "Debito", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito"
        ]

        # Lista de precios correspondientes a cada tipo de entrada
        self.precios = [
            16000, 30000, 25000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
            25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
            30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
            16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
            25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
            30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
            16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
            25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
            30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
            16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000
        ]
        
        self.lista_ventas = []

    def btn_cargar_ventas_on_click(self):
        for _ in range(10):
            nombre_comprador = prompt("Ingrese el nombre del comprador:")

            edad = 0
            while edad < 16:
                try:
                    edad = int(prompt("Ingrese la edad del comprador (mayor o igual a 16):"))
                except ValueError:
                    edad = 0

            genero = ""
            while genero.lower() not in ["masculino", "femenino", "otro"]:
                genero = prompt("Ingrese el género del comprador (Masculino, Femenino, Otro):").lower()

            tipo_entrada = ""
            while tipo_entrada.lower() not in ["general", "campo delantero", "platea"]:
                tipo_entrada = prompt("Ingrese el tipo de entrada (General, Campo delantero, Platea):").lower()

            medio_pago = ""
            while medio_pago.lower() not in ["credito", "efectivo", "debito"]:
                medio_pago = prompt("Ingrese el medio de pago (Crédito, Efectivo, Débito):").lower()

            precio_entrada = 0
            if tipo_entrada.lower() == "general":
                precio_entrada = 16000
            elif tipo_entrada.lower() == "campo delantero":
                precio_entrada = 25000
            elif tipo_entrada.lower() == "platea":
                precio_entrada = 30000

            if medio_pago.lower() == "credito":
                precio_entrada *= 0.8  
            elif medio_pago.lower() == "debito":
                precio_entrada *= 0.85 

            venta = [
                nombre_comprador,
                edad,
                genero.capitalize(),
                tipo_entrada.capitalize(),
                medio_pago.capitalize(),
                precio_entrada
            ]

            self.lista_ventas.append(venta)

        alert("Ventas cargadas con éxito.")
        
    def btn_mostrar_informe_1_on_click(self):
        for i, venta in enumerate(self.lista_ventas):
            print(f"Venta {i + 1}: {venta}")

        informe_numero = int(NOMBRE[-1])

        if informe_numero % 2 == 0:
            generos_campo = [venta[2] for venta in self.lista_ventas if venta[3] == "Campo delantero"]
            genero_mas_frecuente = max(set(generos_campo), key=generos_campo.count)
            print(f"Género más frecuente entre las personas que compraron entradas de tipo 'Campo': {genero_mas_frecuente}")

            personas_mayores_30 = [venta for venta in self.lista_ventas if venta[1] > 30]
            if personas_mayores_30:
                cantidad_entradas_mayores_30 = sum(venta[0] for venta in personas_mayores_30)
                precio_promedio_mayores_30 = sum(venta[5] for venta in personas_mayores_30) / len(personas_mayores_30)
                print(f"Número total de entradas compradas por personas mayores de 30 años: {cantidad_entradas_mayores_30}")
                print(f"Precio promedio: {precio_promedio_mayores_30}")
            else:
                print("No hay personas mayores de 30 años en la lista.")

        else:
            personas_general_credito = [venta for venta in self.lista_ventas if venta[3] == "General" and venta[4] == "Credito"]
            if personas_general_credito:
                cantidad_personas_general_credito = len(personas_general_credito)
                edad_promedio_general_credito = sum(venta[1] for venta in personas_general_credito) / cantidad_personas_general_credito
                print(f"Cantidad de personas que compraron entradas de tipo 'General' pagando con tarjeta de crédito: {cantidad_personas_general_credito}")
                print(f"Edad promedio de estas personas: {edad_promedio_general_credito}")
            else:
                print("No hay personas que cumplan con las condiciones.")
    
    def btn_mostrar_informe_2_on_click(self):
        total_personas = len(self.lista_ventas)
        personas_platea_debito = [venta for venta in self.lista_ventas if venta[3] == "Platea" and venta[4] == "Debito"]
        porcentaje_platea_debito = (len(personas_platea_debito) / total_personas) * 100

        print(f"Porcentaje de personas que compraron entradas de tipo 'Platea' y pagaron con tarjeta de débito: {porcentaje_platea_debito}%")

        def es_primo(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        personas_platea_primo = [venta for venta in self.lista_ventas if venta[3] == "Platea" and es_primo(venta[1])]
        cantidad_platea_primo = len(personas_platea_primo)

        print(f"Cantidad de personas que compraron entradas de tipo 'Platea' y cuya edad es un número primo: {cantidad_platea_primo}")

        monto_total_general_credito_multiplo_5 = sum(venta[5] for venta in self.lista_ventas if venta[3] == "General" and venta[4] == "Credito" and venta[1] % 5 == 0)

        print(f"Monto total recaudado por la venta de entradas de tipo 'General' y pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5: {monto_total_general_credito_multiplo_5}")

        monto_total_platea_debito_multiplo_6 = sum(venta[5] for venta in self.lista_ventas if venta[3] == "Platea" and venta[4] == "Debito" and venta[1] % 6 == 0)

        print(f"Monto total recaudado por la venta de entradas de tipo 'Platea' y pagadas con tarjeta de débito por personas cuyas edades son múltiplos de 6: {monto_total_platea_debito_multiplo_6}")
            
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()
    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
