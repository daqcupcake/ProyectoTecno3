"""
Pagina Teorema de Pitagoras Proyecto 1

Encargado: Sebastian Ortiz

Miembros:   Daniela Arias
            Sebastian Ortiz
            Andy Torres
            
Contenido: El programa contiene la pantalla y funcionalidad del tema de pitagoras 
            
"""

#IMPORTS
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from tkinter.ttk import Combobox

#VARIABLES GLOBALES
colorFondo="#FFFFFF"
colorTexto="#000000"
colorBotones="#25C7CA"
fuente=("Arial",15)



#Datos del triangulo actual
cat1=0
cat2=0
hip=0

#Datos combo box
opciones=["Calcular Hipotenusa","Calcular Cateto"]

def crearPaginaPitagoras(principal):
    #FUNCIONES
    
    def Aleatorio():
        
        """ La funcion genera valores aleatorios según el caso que
        
            se presente"""
            
        global cat1, cat2, hip
        selec=ventPit.combo.get()
        
        if selec=="Calcular Hipotenusa":
            cat1=random.randint(1, 101)
            cat2=random.randint(1, 101)
            
            hip=np.sqrt(cat1**2+cat2**2)
            
            ventPit.laValCat1.config(text=cat1)
            ventPit.laValCat2.config(text=cat2)
            
            
        elif selec=="Calcular Cateto":
            cat1=random.randint(1, 101)
            hip=cat1+random.randint(1, 51)
            
            cat2=np.sqrt(hip**2-cat1**2)
            
            ventPit.laValCat1.config(text=cat1)
            ventPit.laValHip.config(text=hip)
        
        ventPit.verif.config(text="")
        ventPit.resHip.delete(0, tk.END)
        ventPit.resCat.delete(0, tk.END)
            
    def Revisar():
        
        """La funcion que es activada por el boton Revisar
        
            primero verifica la respuesta de usuario según lo ingresado 
            
            y luego grafica de acuerdo con los resultados previamente calculados"""
            
        global hip, cat2
        margenError=0.1
        selec=ventPit.combo.get()
        
        if selec=="Calcular Hipotenusa":
            if ventPit.resHip.get():
                if hip-margenError < float(ventPit.resHip.get()) and float(ventPit.resHip.get()) < hip+margenError:
                    ventPit.verif.config(text=f"Correcto la respuesta es {hip}")
                else:
                    ventPit.verif.config(text=f"Incorrecto la respuesta correcta es {hip}")
        
        elif selec=="Calcular Cateto":
            if ventPit.resCat.get():
                if cat2-margenError < float(ventPit.resCat.get()) and float(ventPit.resCat.get()) < cat2+margenError:
                    ventPit.verif.config(text=f"Correcto la respuesta es {cat2}")
                else:
                    ventPit.verif.config(text=f"Incorrecto la respuesta correcta es {cat2}")
                    
        ventPit.grafica=FigureCanvasTkAgg(graficar(),ventPit)
        ventPit.grafica.get_tk_widget().place(x=300,y=200)
                
        
    def graficar():
        global cat1,cat2
        
        """ La funcion toma los 2 valores de los catetos del triangulo 
            y grafica el triangulo tomando un cateto como base"""
            
        #triangulo=[(0,0),(0,cat2),(cat1,0),(0,0)]
        
        
        fig, ax = plt.subplots()            #crea la figura
        
        trigX = [0, 0, cat1,  0]            #Lista de coordenadas en x y y 
        trigY = [0, cat2, 0,  0]
        
        plt.plot(trigX, trigY, 'o')         #grafica los vertices
        plt.plot(trigX, trigY, '-')         #grafica los lados
        plt.axis('equal')                   #Ejes de la misma escala
        #plt.show()
        
        return fig
        
    def visibilidad(event):
        
        """ La funcion que cambia labels por entry y entry por labels segun el estado
        
            de la combo box"""
            
        
        selec=ventPit.combo.get()
        
        if selec=="Calcular Hipotenusa":
            
            ventPit.laValHip.place_forget()
            ventPit.resHip.place(x=150,y=300)
            
            ventPit.laValCat2.place(x=150,y=250)
            ventPit.resCat.place_forget()
            
        elif selec=="Calcular Cateto":
            
            ventPit.laValCat2.place_forget()
            ventPit.resCat.place(x=150,y=250)
            
            ventPit.laValHip.place(x=150,y=300)
            ventPit.resHip.place_forget()
            
        Aleatorio()
            
    def Volver(ventanaActual,ventanaDestino):
        ventanaActual.withdraw()
        ventanaDestino.deiconify()       
            
        
    
    #TKINTER
    
    #   PRINCIPAL
    ventPit=tk.Tk()
    #ventPit=tk.Toplevel(principal)
    ventPit.title("Teorema de Pitagoras")
    ventPit.geometry("800x600")
    
    #   BOTONES Y LABELS
    ventPit.titulo=tk.Label(ventPit,text="Aqui va el titulo")
    ventPit.titulo.place(x=350,y=50)
    ventPit.desc=tk.Label(ventPit,text="Aqui va la descripcion del programa")
    ventPit.desc.place(x=300,y=100)
    
    ventPit.combo=Combobox(ventPit,values=opciones,width=20) 
    ventPit.combo.place(x=50,y=150)
    ventPit.combo.bind("<<ComboboxSelected>>",visibilidad)
    
    ventPit.laCat1=tk.Label(ventPit,text="Cateto 1: ")
    ventPit.laCat1.place(x=50,y=200)
    ventPit.laCat2=tk.Label(ventPit,text="Cateto 2: ")
    ventPit.laCat2.place(x=50,y=250)
    ventPit.laHip=tk.Label(ventPit,text="Hipotenusa: ")
    ventPit.laHip.place(x=50,y=300)
    
    ventPit.laValCat1=tk.Label(ventPit,text=cat1)
    ventPit.laValCat1.place(x=150,y=200)
    ventPit.laValCat2=tk.Label(ventPit,text=cat2)
    ventPit.laValHip=tk.Label(ventPit,text=hip)
    
    ventPit.resHip=tk.Entry(ventPit,width=10)
    ventPit.resCat=tk.Entry(ventPit,width=10)
    
    ventPit.btnRand=tk.Button(ventPit,text="Aleatorio",command=Aleatorio)
    ventPit.btnRand.place(x=50,y=350)
    
    ventPit.btnRand=tk.Button(ventPit,text="Revisar",command=Revisar)
    ventPit.btnRand.place(x=150,y=350)
    
    ventPit.verif=tk.Label(text="")
    ventPit.verif.place(x=300,y=150)
    
    
    ventPit.btnVol=tk.Button(ventPit,text="Volver",bg=colorBotones,command=lambda: Volver(ventPit, principal))
    ventPit.btnVol.place(x=700,y=550)
    
    ventPit.protocol("WM_DELETE_WINDOW",lambda: Volver(ventPit, principal)) #Para que se cierre como Dios manda
    
    
    
    
    
    ventPit.mainloop() 