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
colorBotones="#64D1AA"
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
        
        """ La funcion genera valores aleatorios segun el caso que
        
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
        
            primero verifica la respuesta de usuario segun lo ingresado 
            
            y luego grafica de acuerdo con los resultados previamente calculados"""
            
        global hip, cat2
        margenError=0.1
        selec=ventPit.combo.get()
        
        if selec=="Calcular Hipotenusa":
            if ventPit.resHip.get():
                if hip-margenError < float(ventPit.resHip.get()) and float(ventPit.resHip.get()) < hip+margenError:
                    ventPit.verif.config(text=f"Correcto la respuesta es {hip:.2f}")
                else:
                    ventPit.verif.config(text=f"Incorrecto la respuesta correcta es {hip:.4f}")
            print("AA")        
        
        elif selec=="Calcular Cateto":
            if ventPit.resCat.get():
                if cat2-margenError < float(ventPit.resCat.get()) and float(ventPit.resCat.get()) < cat2+margenError:
                    ventPit.verif.config(text=f"Correcto la respuesta es {cat2:.2f}")
                else:
                    ventPit.verif.config(text=f"Incorrecto la respuesta correcta es {cat2:.4f}")
                    
        ventPit.grafica=FigureCanvasTkAgg(graficar(),ventPit)
        ventPit.grafica.get_tk_widget().place(x=400,y=310)
                
        
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
            ventPit.resHip.place(x=170,y=360)
            
            ventPit.laValCat2.place(x=170,y=410)
            ventPit.resCat.place_forget()
            
        elif selec=="Calcular Cateto":
            
            ventPit.laValCat2.place_forget()
            ventPit.resCat.place(x=170,y=360)
            
            ventPit.laValHip.place(x=170,y=410)
            ventPit.resHip.place_forget()
            
        Aleatorio()
            
    def Volver(ventanaActual,ventanaDestino):
        ventanaActual.withdraw()
        ventanaDestino.deiconify()       
            
        
    
    #TKINTER
    
    #   PRINCIPAL
    #ventPit=tk.Tk()
    ventPit=tk.Toplevel(principal)
    ventPit.title("Teorema de Pitagoras")
    ventPit.geometry("1200x800")
    
    #   BOTONES Y LABELS
    ventPit.titulo=tk.Label(ventPit,text="Teorema de Pitagoras",font=('Arial 20 bold'),justify="center",fg="#006DCC")
    ventPit.titulo.place(x=400,y=20)
    ventPit.desc=tk.Message(ventPit,text="A traves de esta ventana, podras practicar determinar la medida de un lado mediante el teorema de Pitagoras. Para ello, debes seleccionar si deseas calcular un cateto o una hipotenusa. Una vez que lo seleccionas, utilizando los valores que brinda aleatoriamente puedes determinar cada medida. Ademas, una vez que lo verifiques podras ver como se ve graficamente dicho triangulo.\nNota: En las respuestas que tengan expansion decimal infinita periodica utiliza unicamente dos decimales sin redondear.",font=fuente,width=1100)
    ventPit.desc.place(x=50,y=70)
    
    ventPit.combo=Combobox(ventPit,values=opciones,width=20,font=fuente) 
    ventPit.combo.place(x=50,y=260)
    ventPit.combo.bind("<<ComboboxSelected>>",visibilidad)
    
    ventPit.laCat1=tk.Label(ventPit,text="Cateto 1: ",font=fuente)
    ventPit.laCat1.place(x=50,y=310)
    ventPit.laCat2=tk.Label(ventPit,text="Cateto 2: ",font=fuente)
    ventPit.laCat2.place(x=50,y=360)
    ventPit.laHip=tk.Label(ventPit,text="Hipotenusa: ",font=fuente)
    ventPit.laHip.place(x=50,y=410)
    
    ventPit.laValCat1=tk.Label(ventPit,text=cat1,font=fuente)
    ventPit.laValCat1.place(x=170,y=310)
    ventPit.laValCat2=tk.Label(ventPit,text=cat2,font=fuente)
    ventPit.laValHip=tk.Label(ventPit,text=hip,font=fuente)
    
    ventPit.resHip=tk.Entry(ventPit,width=10,font=fuente)
    ventPit.resCat=tk.Entry(ventPit,width=10,font=fuente)
    
    ventPit.btnRand=tk.Button(ventPit,text="Aleatorio",command=Aleatorio,font=fuente,bg=colorBotones)
    ventPit.btnRand.place(x=50,y=460)
    
    ventPit.btnRand=tk.Button(ventPit,text="Revisar",command=Revisar,font=fuente,bg=colorBotones)
    ventPit.btnRand.place(x=150,y=460)
    
    ventPit.verif=tk.Label(ventPit,text="",font=fuente)
    ventPit.verif.place(x=400,y=260)
    
    ventPit.btnVol=tk.Button(ventPit,text="Volver",bg="#00B37A",fg="white",command=lambda: Volver(ventPit, principal),font=fuente)
    ventPit.btnVol.place(x=1100,y=750)
    
    
    ventPit.protocol("WM_DELETE_WINDOW",lambda: Volver(ventPit, principal)) #Para que se cierre como Dios manda
    
    
    
    
    ventPit.mainloop() 