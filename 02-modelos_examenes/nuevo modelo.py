import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
Ejercicio: Extra-Parcial 
---
Ejercicio:
Enunciado 2 : de 10 casas que se fueron a fumigar 
(un casa por fumigador)necesitamos saber los siguientes datos sabiendo que el litro de insecticida sale 1000

color (negro , gris , mixto)
cantidad por metro cuadrado de mosquitos
cantidad de minuto de trabajo
cantidad de producto utilizado
sexo del fumigador
nombre del fumigador
pedir datos por prompt y mostrar por print
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]

    def btn_mostrar_on_click(self):
        total_casas = 10
        litro_insecticida_costo = 1000
        total_costo_insecticida = 0
        total_minutos_trabajo = 0
        total_productos_utilizados = 0
        total_mosquitos = 0
        fumigadores = []

        for i in range(total_casas):
            color = input(f"Ingrese el color de la casa {i + 1} (negro, gris, mixto): ").lower()
            while color not in ['negro', 'gris', 'mixto']:
                color = input("Color inválido. Ingrese el color de la casa (negro, gris, mixto): ").lower()

            cantidad_mosquitos = int(input(f"Ingrese la cantidad de mosquitos por metro cuadrado en la casa {i + 1}: "))
            while cantidad_mosquitos <= 0:
                cantidad_mosquitos = int(input("Cantidad inválida. Ingrese la cantidad de mosquitos por metro cuadrado: "))

            minutos_trabajo = int(input(f"Ingrese la cantidad de minutos de trabajo en la casa {i + 1}: "))
            while minutos_trabajo <= 0:
                minutos_trabajo = int(input("Cantidad inválida. Ingrese la cantidad de minutos de trabajo: "))

            producto_utilizado = float(input(f"Ingrese la cantidad de producto utilizado en la casa {i + 1}: "))
            while producto_utilizado <= 0:
                producto_utilizado = float(input("Cantidad inválida. Ingrese la cantidad de producto utilizado: "))

            sexo_fumigador = input(f"Ingrese el sexo del fumigador en la casa {i + 1} (M/F): ").upper()
            while sexo_fumigador not in ['M', 'F']:
                sexo_fumigador = input("Sexo inválido. Ingrese el sexo del fumigador (M/F): ").upper()

            nombre_fumigador = input(f"Ingrese el nombre del fumigador en la casa {i + 1}: ")

            total_costo_insecticida += producto_utilizado * litro_insecticida_costo
            total_minutos_trabajo += minutos_trabajo
            total_productos_utilizados += producto_utilizado
            total_mosquitos += cantidad_mosquitos

            fumigadores.append({
                'color': color,
                'cantidad_mosquitos': cantidad_mosquitos,
                'minutos_trabajo': minutos_trabajo,
                'producto_utilizado': producto_utilizado,
                'sexo_fumigador': sexo_fumigador,
                'nombre_fumigador': nombre_fumigador
            })

        promedio_mosquitos = total_mosquitos / total_casas
        promedio_minutos_trabajo = total_minutos_trabajo / total_casas
        promedio_producto_utilizado = total_productos_utilizados / total_casas

        print("\nResultados:")
        print(f"Promedio de mosquitos por metro cuadrado: {promedio_mosquitos}")
        print(f"Promedio de minutos de trabajo: {promedio_minutos_trabajo}")
        print(f"Promedio de producto utilizado: {promedio_producto_utilizado}")
        print(f"Total costo de insecticida: {total_costo_insecticida}")

        print("\nDatos de los fumigadores:")
        
        for i, fumigador in enumerate(fumigadores, 1):
            print(f"\nDatos del fumigador {i}:")
            print(f"Color: {fumigador['color']}")
            print(f"Cantidad de mosquitos por metro cuadrado: {fumigador['cantidad_mosquitos']}")
            print(f"Minutos de trabajo: {fumigador['minutos_trabajo']}")
            print(f"Cantidad de producto utilizado: {fumigador['producto_utilizado']}")
            print(f"Sexo del fumigador: {fumigador['sexo_fumigador']}")
            print(f"Nombre del fumigador: {fumigador['nombre_fumigador']}")
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

#Inicialización de variables: Se definen variables para almacenar los totales y una lista fumigadores para almacenar los datos de cada fumigador.

#Bucle de ingreso de datos: Se utiliza un bucle for para solicitar datos de cada casa (fumigador) al usuario. Se realizan validaciones para asegurar que los datos ingresados sean válidos.

#Cálculos y acumulación de totales: Se calculan y acumulan diferentes totales durante el bucle de entrada de datos.

#Cálculos de promedios: Se calculan los promedios de mosquitos, minutos de trabajo y producto utilizado.

#Impresión de resultados: Se imprimen los resultados, incluyendo promedios y totales.

#Impresión de datos de fumigadores: Se itera sobre la lista de fumigadores y se imprimen los datos de cada uno.