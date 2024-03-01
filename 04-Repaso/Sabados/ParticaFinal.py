import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
Ejercicio: Parcial 
---
Parcial Turno Mañana:
Nos piden diseñar un sistema de control de ventas para una empresa de electrodomésticos. 
(Teniendo en cuenta que no sabemos cuantas ventas hubo en total y que todos los datos deben ser ingresados por prompt y mostrados en un solo alert)

Para ello los empleados deben ingresar:

-Nombre del producto.

-Tipo de producto (Celular o Computadora o Ventilador)

-Precio del producto (No puede ser menor a $1000)

-Día de la semana en el que se realizó la venta (La empresa no trabaja sábados ni domingos)

En base a la información ingresada se debe informar:

+El porcentaje de productos que se vendieron por tipo.

+El nombre del producto más caro vendido.

+El nombre del producto mas barato vendido un viernes.

+Promedio de computadoras vendidas.

+Promedio de errores que ocurrieron durante la carga de datos (Ya sea al ingresar el tipo, el precio o el día de la venta, esto para controlar la eficiencia de los empleados al cargar las ventas)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]

    def btn_mostrar_on_click(self):
        ventas_totales = 0
        celulares = 0; computadora = 0; ventiladores = 0
        nombre_producto_mas_caro = ""; nombre_producto_mas_barato_viernes = ""
        precio_producto_mas_caro = 0; precio_producto_mas_barato_viernes = float('inf')
        total_computadoras_vendidas = 0
        errores = 0

        while True:
            nombre_producto = prompt("Ingrese el nombre del producto:")
            
            if nombre_producto.lower() == "fin":
                break 
            
            tipo_producto = prompt("Ingrese el tipo de producto (Celular, Computadora, Ventilador):").capitalize()
            while tipo_producto not in ['Celular', 'Computadora', 'Ventilador']:
                print("Tipo de producto inválido.")
                errores += 1
                tipo_producto = prompt("Ingrese Celular, Computadora o Ventilador:").capitalize()

            precio_producto = float(prompt("Ingrese el precio del producto (mayor o igual a $1000):"))
            while precio_producto < 1000:
                print("Precio inválido.")
                errores += 1
                precio_producto = float(prompt("Ingrese el precio (mayor o igual a $1000):"))

            dia_semana = prompt("Ingrese el día de la semana de la venta (Lunes a Viernes):").capitalize()
            while dia_semana not in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']:
                print("Día inválido.")
                errores += 1
                dia_semana = prompt("Ingrese Lunes, Martes, Miércoles, Jueves o Viernes:").capitalize()

            ventas_totales += 1

            if tipo_producto == 'Celular':
                celulares += 1
            elif tipo_producto == 'Computadora':
                computadora += 1
                total_computadoras_vendidas += 1
            elif tipo_producto == 'Ventilador':
                ventiladores += 1

            if precio_producto > precio_producto_mas_caro:
                nombre_producto_mas_caro = nombre_producto
                precio_producto_mas_caro = precio_producto

            if dia_semana == 'Viernes' and precio_producto < precio_producto_mas_barato_viernes:
                nombre_producto_mas_barato_viernes = nombre_producto
                precio_producto_mas_barato_viernes = precio_producto

        if ventas_totales > 0:
            mensaje = f"Total de ventas: {ventas_totales}\n" \
                    f"Porcentaje de Celulares: {(celulares / ventas_totales) * 100}%\n" \
                    f"Porcentaje de Computadoras: {(computadora / ventas_totales) * 100}%\n" \
                    f"Porcentaje de Ventiladores: {(ventiladores / ventas_totales) * 100}%\n" \
                    f"Nombre del producto más caro: {nombre_producto_mas_caro}\n" \
                    f"Nombre del producto más barato vendido un viernes: {nombre_producto_mas_barato_viernes}\n" \
                    f"Promedio de Computadoras vendidas: {total_computadoras_vendidas / ventas_totales}\n" \
                    f"Total de errores durante la carga de datos: {errores}"
            alert("Resultados", mensaje)
        else:
            alert("Resultados", "No se registraron ventas.")            
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
