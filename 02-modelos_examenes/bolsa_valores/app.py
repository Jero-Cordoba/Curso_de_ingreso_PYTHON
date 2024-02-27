import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "Jerónimo Córdoba" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4) = 7

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9. 9-7 = 2

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=6, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        self.lista_nombre = ["Pepe", "Paola", "Dardo", "Fatiga", "Maria"]
        self.lista_monto = [20000,30000,40000,50000,60000]
        self.lista_tipo_instrumento = ["CEDEAR","BONOS","MEP","CEDEAR","CEDEAR"]
        self.lista_cantidad_instrumento = [20, 35, 199, 100, 80]
    
    def btn_cargar_datos_on_click(self):
        self.lista_nombre = []
        self.lista_monto = []
        self.lista_tipo_instrumento = []
        self.lista_cantidad_instrumento = []

        for _ in range(10):
            nombre = prompt("Ingrese el nombre del usuario:")
            monto = int(prompt("Ingrese el monto en pesos de la operación (no menor a $10000):"))
            while monto < 10000:
                alert("El monto debe ser igual o mayor a $10000.")
                monto = int(prompt("Ingrese el monto en pesos de la operación (no menor a $10000):"))

            tipo_instrumento = prompt("Ingrese el tipo de instrumento (CEDEAR, BONOS, MEP):")
            cantidad_instrumento = int(prompt("Ingrese la cantidad de instrumentos (no menos de cero):"))
            while cantidad_instrumento < 0:
                alert("La cantidad de instrumentos debe ser igual o mayor a cero.")
                cantidad_instrumento = int(prompt("Ingrese la cantidad de instrumentos (no menos de cero):"))

            self.lista_nombre.append(nombre)
            self.lista_monto.append(monto)
            self.lista_tipo_instrumento.append(tipo_instrumento)
            self.lista_cantidad_instrumento.append(cantidad_instrumento)
            
            alert("Los datos se cargaron correctamente.")
        
    def btn_mostrar_informe_1(self):
        for i in range(len(self.lista_nombre)):
            nombre = self.lista_nombre[i]
            monto = self.lista_monto[i]
            tipo_instrumento = self.lista_tipo_instrumento[i]
            cantidad_instrumento = self.lista_cantidad_instrumento[i]
            print(f"{i + 1}) Nombre: {nombre}, Monto: ${monto},Tipo de Instrumento: {tipo_instrumento},"f"Cantidad de Instrumentos: {cantidad_instrumento}")
        
    def btn_mostrar_informe_2(self):
        if int(NOMBRE[-1]) == 7:
            pass
        elif int(NOMBRE[-1]) == 2:
            pass
        else:
            print("No es necesario realizar este informe.")
            
    def btn_mostrar_informe_3(self):
        if int(NOMBRE[-1]) == 5:
            pass
        elif int(NOMBRE[-1]) == 9:
            pass
        else:
            print("No es necesario realizar este informe.")    
            
    def btn_mostrar_todos_on_click(self):
            tipo_menos_operado = min(set(self.lista_tipo_instrumento), key=self.lista_tipo_instrumento.count)
            print(f"Tipo de instrumento que menos se operó en total: {tipo_menos_operado}")

            tipo_mas_operado = max(set(self.lista_tipo_instrumento), key=self.lista_tipo_instrumento.count)
            print(f"Tipo de instrumento que más se operó en total: {tipo_mas_operado}")

            usuarios_entre_50_y_200_mep = 0
            for i in range(len(self.lista_monto)):
                if self.lista_tipo_instrumento[i] == "MEP" and 50 <= self.lista_monto[i] <= 200:
                    usuarios_entre_50_y_200_mep += 1
            print(f"Cantidad de usuarios que compraron entre 50 y 200 MEP: {usuarios_entre_50_y_200_mep}")

            usuarios_sin_cedear = 0
            for tipo in self.lista_tipo_instrumento:
                if tipo != "CEDEAR":
                    usuarios_sin_cedear += 1
            print(f"Cantidad de usuarios que no compraron CEDEAR: {usuarios_sin_cedear}")

            primer_usuario_bonos_cedear = None
            for i in range(len(self.lista_nombre)):
                if self.lista_tipo_instrumento[i] in ["BONOS", "CEDEAR"]:
                    primer_usuario_bonos_cedear = f"Nombre: {self.lista_nombre[i]}, Cantidad Invertida: ${self.lista_monto[i]}"
                    break
            print(f"Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR: {primer_usuario_bonos_cedear}")

            usuario_menos_bonos = None
            for i in range(len(self.lista_nombre)):
                if self.lista_tipo_instrumento[i] == "BONOS":
                    if usuario_menos_bonos is None or self.lista_cantidad_instrumento[i] < self.lista_cantidad_instrumento[usuario_menos_bonos]:
                        usuario_menos_bonos = i
            if usuario_menos_bonos is not None:
                print(f"Nombre y posición de la persona que menos BONOS compró: {self.lista_nombre[usuario_menos_bonos]}")

            usuario_menos_dinero = None
            for i in range(len(self.lista_nombre)):
                if usuario_menos_dinero is None or self.lista_monto[i] < self.lista_monto[usuario_menos_dinero]:
                    usuario_menos_dinero = i
            if usuario_menos_dinero is not None:
                print(f"Nombre y posición del usuario que invirtió menos dinero: {self.lista_nombre[usuario_menos_dinero]}")

            usuario_mas_instrumentos = None
            for i in range(len(self.lista_nombre)):
                if usuario_mas_instrumentos is None or self.lista_cantidad_instrumento[i] > self.lista_cantidad_instrumento[usuario_mas_instrumentos]:
                    usuario_mas_instrumentos = i
            if usuario_mas_instrumentos is not None:
                print(f"Nombre y posición del usuario que más cantidad de instrumentos compró: {self.lista_nombre[usuario_mas_instrumentos]}")

            total_dinero_cedear = 0
            count_cedear = 0
            for i in range(len(self.lista_monto)):
                if self.lista_tipo_instrumento[i] == "CEDEAR":
                    total_dinero_cedear += self.lista_monto[i]
                    count_cedear += 1
            promedio_dinero_cedear = total_dinero_cedear / count_cedear if count_cedear > 0 else 0
            print(f"Promedio de dinero en CEDEAR ingresado en total: ${promedio_dinero_cedear:.2f}")

            total_cantidad_mep = 0
            count_mep = 0
            for i in range(len(self.lista_cantidad_instrumento)):
                if self.lista_tipo_instrumento[i] == "MEP":
                    total_cantidad_mep += self.lista_cantidad_instrumento[i]
                    count_mep += 1
            promedio_cantidad_mep = total_cantidad_mep / count_mep if count_mep > 0 else 0
            print(f"Promedio de cantidad de instrumentos MEP vendidos en total: {promedio_cantidad_mep:.2f}")
                
if __name__ == "__main__":
    app = App()
    app.mainloop()
