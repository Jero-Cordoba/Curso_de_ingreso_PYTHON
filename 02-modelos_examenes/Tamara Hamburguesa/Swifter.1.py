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
NOMBRE = 'Jerónimo Córdoba'
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
    #! 0) - Cantidad total de dinero recaudado por las ventas de entradas.
    #! 1) - Cantidad de entradas vendidas para cada tipo.
    #! 2) - Promedio de edad de las personas que compraron ubicación en Platea.
    #! 3) - Nombre de la persona de mayor edad que compró una entrada de platea.
    #! 4) - Porcentaje de entradas vendidas de tipo "General"
    #! 5) - Porcentaje de entradas vendidas de tipo "Campo"
    #! 6) - Nombre de la/s persona/s de menor edad, de género Femenino que compro una 
    #!       entrada Platea.
    #! 7) - Nombre de la/s persona/s de mayor edad, de género Masculino que compro una 
    #!       entrada general.
    #! 8) - Tipo de entradas más vendidas.
    #! 9) - Tipo de entradas menos vendidas.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Punto de Venta {NOMBRE} [version 1]")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Punto de Venta {NOMBRE} [Version 1]", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/taylor_swift_v1/UTN_PuntoVenta_App_v1.png')
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
        
        self.ventas = []
        self.entradas_totales = 0

    def btn_cargar_ventas_on_click(self):
        
        
        for i in range(10):
            
            nombre = prompt("Ingrese el nombre del comprador:")
            edad = int(prompt("Ingrese la edad del comprador (mayor o igual a 16):"))
            genero = prompt("Ingrese el género del comprador (Masculino, Femenino, Otro):")
            
            while edad < 16:
                alert("La edad debe ser mayor o igual a 16.")
                edad = int(prompt("Ingrese la edad del comprador (mayor o igual a 16):"))

            tipo_entrada = prompt("Ingrese el tipo de entrada (General, Campo delantero, Platea):")
            medio_pago = prompt("Ingrese el medio de pago (Crédito, Efectivo, Débito):")

            precio = self.calcular_precio_entrada(tipo_entrada, medio_pago)
        
            venta = {
                    "Nombre": nombre,
                    "Edad": edad,
                    "Género": genero,
                    "Tipo de Entrada": tipo_entrada,
                    "Medio de Pago": medio_pago,
                    "Precio": precio
                }
            self.ventas.append(venta)
            
            precios_entradas = {
            "General": 16000,
            "Campo delantero": 25000,
            "Platea": 30000
            }

            descuento_credito = 0.2
            descuento_debito = 0.15

            precio_base = precios_entradas[tipo_entrada]

            if medio_pago == "Crédito":
                precio_final = precio_base * (1 - descuento_credito)
            elif medio_pago == "Débito":
                precio_final = precio_base * (1 - descuento_debito)
            else:
                precio_final = precio_base

            return precio_final
            
    def btn_mostrar_informe_1_on_click(self):
        print("Informe 1:")
        for i, venta in enumerate(self.ventas, start=1):
            print(f"Venta {i}:")
            print(f"Nombre: {venta['Nombre']}")
            print(f"Edad: {venta['Edad']}")
            print(f"Género: {venta['Género']}")
            print(f"Tipo de Entrada: {venta['Tipo de Entrada']}")
            print(f"Medio de Pago: {venta['Medio de Pago']}")
            print(f"Precio: ${venta['Precio']}")
    
    def btn_mostrar_informe_2_on_click(self):
        print("Informe 2:")
        
        tipo_entrada_vendida = {"General": 0, "Campo delantero": 0, "Platea": 0}
        suma_edad_platea = 0; cantidad_platea = 0
        persona_mayor_platea = {"Nombre": "", "Edad": 0}
        porcentaje_general = 0; porcentaje_campo = 0
        edad_menor_mujer_platea = float('inf')
        nombre_menor_mujer_platea = ""
        edad_mayor_hombre_general = 0; nombre_mayor_hombre_general = ""
        
        total_recaudado = sum(venta["Precio"] for venta in self.ventas)
        print(f"0) Cantidad total de dinero recaudado: ${total_recaudado}")


        for venta in self.ventas:
            tipo_entrada_vendida[venta["Tipo de Entrada"]] += 1
            if venta["Tipo de Entrada"] == "Platea":
                suma_edad_platea += venta["Edad"]
                cantidad_platea += 1
                if venta["Edad"] > persona_mayor_platea["Edad"]:
                    persona_mayor_platea["Nombre"] = venta["Nombre"]
                    persona_mayor_platea["Edad"] = venta["Edad"]

            if venta["Tipo de Entrada"] == "General" and venta["Género"] == "Masculino" and venta["Edad"] > edad_mayor_hombre_general:
                nombre_mayor_hombre_general = venta["Nombre"]
                edad_mayor_hombre_general = venta["Edad"]

            if venta["Tipo de Entrada"] == "Platea" and venta["Género"] == "Femenino" and venta["Edad"] < edad_menor_mujer_platea:
                nombre_menor_mujer_platea = venta["Nombre"]
                edad_menor_mujer_platea = venta["Edad"]

        if cantidad_platea != 0:
            promedio_edad_platea = suma_edad_platea / cantidad_platea
            print(f"1) Cantidad de entradas vendidas para cada tipo: {tipo_entrada_vendida}")
            print(f"2) Promedio de edad de las personas que compraron ubicación en Platea: {promedio_edad_platea:.2f}")
            print(f"3) Nombre de la persona de mayor edad que compró una entrada de platea: {persona_mayor_platea['Nombre']}")

        if cantidad_platea != 0:
            porcentaje_general = (tipo_entrada_vendida["General"] / cantidad_platea) * 100

        if cantidad_platea != 0:
            porcentaje_campo = (tipo_entrada_vendida["Campo delantero"] / cantidad_platea) * 100

        print(f"4) Porcentaje de entradas vendidas de tipo 'General': {porcentaje_general:.2f}%")
        print(f"5) Porcentaje de entradas vendidas de tipo 'Campo delantero': {porcentaje_campo:.2f}")
        print(f"6) Nombre de la/s persona/s de menor edad, de género Femenino que compró una entrada Platea: {nombre_menor_mujer_platea}")
        print(f"7) Nombre de la/s persona/s de mayor edad, de género Masculino que compró una entrada general: {nombre_mayor_hombre_general}")

        tipo_entrada_mas_vendida = max(tipo_entrada_vendida, key=tipo_entrada_vendida.get)
        tipo_entrada_menos_vendida = min(tipo_entrada_vendida, key=tipo_entrada_vendida.get)
        print(f"8) Tipo de entradas más vendidas: {tipo_entrada_mas_vendida}")
        print(f"9) Tipo de entradas menos vendidas: {tipo_entrada_menos_vendida}")
    
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
