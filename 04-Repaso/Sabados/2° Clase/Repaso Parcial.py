import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.   btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_iteracion_on_click(self):
        #Que va antes del while
        continuar = True #bandera
        tecnologia_mas_votada=None #No tiene nada

        contador_masculino_TOT_IA = 0
        #2 
        contador_IOT = 0
        contador_IA = 0
        contador_RV_RA = 0
        #3
        contador_masculino=0
        contador_femenino=0
        contador_otro=0
        #4
        contador_IOT_edad=0
        #5
        contador_femenino_votaron_IA=0
        acumulador_femenino_edad=0
        #6 
        bandera_minimo= False
        minima_edad=0
        nombre_minimo=0
        genero_minimo=0

        #Que va dentro del while
        while continuar == True: #Hasta que el usuario lo desee.
            # * nombre del empleado
            # * edad (no menor a 18)
            # * genero (Masculino - Femenino - Otro)
            # * tecnologia (IA, RV/RA, IOT)  
            nombre = prompt("Nombre","Ingreso nombre")


            #EDAD
            edad = prompt("Edad","Ingrese edad")
            edad = int(edad)
            while edad > 18 and edad <99 : #NO SE VALUA CON IF
                edad = prompt("ERROR","Ingrese edad una edad +18")
                edad = int(edad)    
            
            #GENERO
            genero = prompt("Genero","Ingrese genero")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro": #Va and porque si se cumple 1 no entra al while/ != distinto de
                prompt("ERROR","Ingrese genero")

            #Tecnologia
            tecnologia = prompt("Tecnologia","Ingrese tecnologia")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                prompt("ERROR","Ingrese tecnologia")

            #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.CANTIDAD=CONTADOR
            if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50: #Parentesis porque sino  evalua de genero a tecnologia IOT, y no tecnologia entre IOT o IA
                contador_masculino_TOT_IA += 1

            #!X 2) - Tecnología que mas se votó.CONTADORES 
            if tecnologia == "IA":
                contador_IA += 1
                if edad >= 18 and edad <= 25 or edad >= 33 and edad <= 42:#4
                    contador_IOT_edad +=1
                
            elif tecnologia == "IOT":
                contador_IOT += 1
            else:
                contador_RV_RA += 1
                #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
                if edad < minima_edad or contador_RV_RA !=0:#bandera_minimo == False:
                    minima_edad= edad
                    nombre_minimo= nombre
                    genero_minimo=genero
                    #bandera_minimo = True
            
            #O
            
            # match tecnologia:
            #     case "IA":
            #         contador_IA +=1
                    # if edad >= 18 and edad <= 25 or edad >= 33 and edad <= 42:#4
                    #     contador_IOT_edad +=1
            # match tecnologia:
            #     case"IOT":
            #         contador_IOT +=1
            # match tecnologia:
            #     case "RV/RA" :
            #         contador_RV_RA +=1


            #!X 3) - Porcentaje de empleados por cada genero
            if genero=="Masculino":
                contador_masculino+=1

            elif genero=="Femenino":
                contador_femenino+=1
                #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
                if tecnologia == "IA":
                    contador_femenino_votaron_IA +=1
                    acumulador_femenino_edad +=1
                    

            else:
                contador_otro+=1
            
            

            continuar = question("Seguir","Desea continuar?")#Pregunta entre aceptar o cancelar y va alfinal

##########################################################
            
        #Que va fuera del while
    
        #!X 2) - Tecnología que mas se votó.CONTADORES 
        if contador_IA > contador_IOT  and contador_IA >contador_RV_RA:
            tecnologia_mas_votada = "IA"

        elif contador_IOT>contador_RV_RA:
            tecnologia_mas_votada = "IOT"

        else:
            tecnologia_mas_votada = "RV/RA"

        #3
        total_empleados= contador_femenino+contador_masculino+ contador_otro

        porcentaje_masculinos= (contador_masculino*100)/total_empleados
        porcentaje_femenino= (contador_femenino*100)/total_empleados
        #porcentaje_otro=(contador_otro*100)/100
        porcentaje_otro= 100-(porcentaje_masculinos + porcentaje_femenino)
        
        #4
         #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  LINEA 103 hacer con IF.
        porcentaje_iot_edad=( contador_IOT_edad*100)/total_empleados #O por el contador_IOT

        #5
        #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
        if contador_femenino_votaron_IA != 0:
            promedio_edad= acumulador_femenino_edad/contador_femenino_votaron_IA
        else:
            promedio_edad= "No se ingreso ninguno femeninoque cumpla con la condición"
        
        #6
        #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

        alert("1.",f"Cantidad masculinos que votaron IOT/IA en el rango de edad 25-50: {contador_masculino_TOT_IA}")
        alert("2.",f"La tecnologia mas votada es: {tecnologia_mas_votada}")
        alert("3.",f" porcentaje\n\tMasculino: {porcentaje_masculinos}\n\tporcentaje femenino: {porcentaje_femenino}\n\tporcentaje otro: {porcentaje_otro}")
        alert("4."f"El porcentaje de IOT que votaron es de : {porcentaje_iot_edad}")
        alert("5.",f"Promedio de edad de los empleados de genero Femenino que votaron por IA: {promedio_edad}")
        if contador_RV_RA != 0:
            alert(f"6.{nombre_minimo}{genero_minimo}{minima_edad}")
        else: 
            alert("Mensaje","No se encontro minimo para RV")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
