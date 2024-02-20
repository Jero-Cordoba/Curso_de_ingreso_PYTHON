import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Jerónimo
apellido: Córdoba
---
Ejercicio: Match_01
---
Enunciado:
Obtener el valor del mes seleccionado en el combobox_mes y  
al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si el mes seleccionado es Enero: ‘que comiences bien el año!!!’
    Si el mes seleccionado es Marzo: ‘a clases!!’
    Si el mes seleccionado es Julio: ‘se vienen las vacaciones!!’
    Si el mes seleccionado es Diciembre: ‘Felices fiestas!!!’
En caso de seleccionar un mes distinto a los mencionados, no hacer nada
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        meses = self.combobox_mes.get()
        
        match meses:
            case 'Enero':
                mensaje = "Que comience el año"
            case 'Febrero':
                mensaje = "NO PUEDE HACER TANTO CALOR"
            case 'Marzo':
                mensaje = "A clases😀🔫"
            case 'Abril':
                mensaje = "Muchos feriados"
            case 'Mayo':
                mensaje = "Anda preparando ese locro"
            case 'Junio':
                mensaje = "Empieza el frio 🥶"
            case 'Julio':
                mensaje = "Vacaciones de invierno 🏂⛷"
            case 'Agosto':
                mensaje = "Segunda mitad de cursada"
            case 'Septiembre':
                mensaje = "Primavera"
            case 'Octubre':
                mensaje = "BU 👻☠"
            case 'Noviembre':
                mensaje = "FINALES"
            case 'Diciembre':
                mensaje = "Vacaciones"
        pass
        alert("Match-01", mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
