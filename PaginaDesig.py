"""
Pagina Desigualdad Triangular Proyecto 1

Encargado: Daniela Arias 

Miembros:   Daniela Arias
            Sebastian Ortiz
            Andy Torres
            
Contenido: El programa contiene la pantalla y funcionalidad del tema de desigualdad triangular 
            
"""
#IMPORTS
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#VARIABLES GLOBALES
colorFondo="#FFFFFF"
colorTexto="#000000"
colorBotones="#64D1AA"
fuente=("Arial",15)


def crearPaginaDesig(principal):
    
    #FUNCIONES
    def graficoTri(a,b,c):
        
        """ La funcion toma los 3 valores de los lados del triangulo ya ordenados de mayor a menor
            y grafica el triangulo tomando el lado mayor como base"""
            
        m=(b**2-c**2-a**2)/(-2*a)           #coordenada en X del tercer punto
        h=np.sqrt(c**2-m**2)                #coordenada en Y del tercer punto
        
        
        #triangulo=[(0,0),(a,0),(m,h),(0,0)]
        
        
        fig, ax = plt.subplots()            #crea la figura
        
        trigX = [0, a, m,  0]               #Lista de coordenadas en x y y 
        trigY = [0, 0, h,  0]
        
        plt.plot(trigX, trigY, 'o')         #grafica los vertices
        plt.plot(trigX, trigY, '-')         #grafica los lados
        plt.axis('equal')                   #Ejes de la misma escala
        #plt.show()
        
        return fig
       
    
    def graficoNoTri(a,b,c):
        """ La funcion toma los 3 valores de los segmentos ya ordenados de mayor a menor
            y grafica tomando el lado mayor como base"""
            
        #(0,b)(0,0),(a,0)(a,c)
        
        fig, ax = plt.subplots()            #crea la figura
        
        x=[0,0,a,a]                         #Lista de coordenadas en x y y 
        y=[b,0,0,c]
        plt.plot(x, y, 'o')                 #grafica los vertices
        plt.plot(x, y, '-')                 #grafica los lados
        plt.axis('equal')                   #Ejes de la misma escala
        #plt.show()
        
        return fig
        
    
    def Revisar():
        
        """La funcion que es activada por el boton Revisar
        
            primero verifica la desigualdad triangular y luego grafica de acuerdo con los resultados"""
        
        if ventDesig.num1.get() and ventDesig.num2.get() and ventDesig.num3.get():        #verifica que haya algo en los input
            
            n1=float(ventDesig.num1.get())                            #Asigna variable locales
            n2=float(ventDesig.num2.get())
            n3=float(ventDesig.num3.get())
            
            #Ordenamos los lados es orden de tamaño
            
            lados=[n1,n2,n3]                                #Lista y sort (mas sencillo que con ifs)
            lados.sort(reverse=True)
            
            #SI cumple desigualdad triangular
            
            if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:          
                ventDesig.lrespuesta.config(text="Las medidas dadas corresponden a un triangulo")
                
                ventDesig.grafica=FigureCanvasTkAgg(graficoTri(lados[0], lados[1], lados[2]),ventDesig)
                ventDesig.grafica.get_tk_widget().place(x=300,y=300)
                
            #NO cumple desigualdad triangular
                
            else: 
                ventDesig.lrespuesta.config(text="Las medidas dadas no corresponden a un triangulo")
                
                
                ventDesig.grafica=FigureCanvasTkAgg(graficoNoTri(lados[0], lados[1], lados[2]),ventDesig)
                ventDesig.grafica.get_tk_widget().place(x=300,y=300)
                
                
                
            
       
        
    def Volver(ventanaActual,ventanaDestino):
        ventanaActual.withdraw()
        ventanaDestino.deiconify()
    
    #TKINTER
    
    #   PRINCIPAL
    #ventDesig=tk.Tk()
    ventDesig=tk.Toplevel(principal)
    ventDesig.title("Desigualdad Triangular")
    ventDesig.geometry("1200x800")
    
    #   BOTONES Y LABELS
    ventDesig.titulo=tk.Label(ventDesig,text="Desigualdad Triangular",font=('Arial 20 bold'),justify="center",fg="#006DCC")
    ventDesig.titulo.place(x=400,y=20)
    ventDesig.desc=tk.Message(ventDesig,text="A traves de esta ventana, podras practicar determinar si tres numeros brindados corresponden a las medidas de un triangulo mediante la desigualdad triangular. Para ello, debes escribir en cada caso el numero y una vez verificado si corresponde o no a un triangulo. Ademas, una vez que lo verifiques podras ver como se ve graficamente dicho triangulo.",font=fuente,width=1100)
    ventDesig.desc.place(x=50,y=80)
    ventDesig.lnum1=tk.Label(ventDesig,text="Numero 1:",font=fuente)
    ventDesig.lnum1.place(x=50, y=250)
    ventDesig.num1=tk.Entry(ventDesig,width=10,font=fuente)
    ventDesig.num1.place(x=150, y=250)
    ventDesig.lnum2=tk.Label(ventDesig,text="Numero 2:",font=fuente)
    ventDesig.lnum2.place(x=50, y=300)
    ventDesig.num2=tk.Entry(ventDesig,width=10,font=fuente)
    ventDesig.num2.place(x=150, y=300)
    ventDesig.lnum3=tk.Label(ventDesig,text="Numero 3:",font=fuente)
    ventDesig.lnum3.place(x=50, y=350)
    ventDesig.num3=tk.Entry(ventDesig,width=10,font=fuente)
    ventDesig.num3.place(x=150, y=350)
    
    ventDesig.btnRev=tk.Button(ventDesig,text="Revisar",bg=colorBotones,command=Revisar,font=fuente)
    ventDesig.btnRev.place(x=75,y=400)
    ventDesig.lrespuesta=tk.Label(ventDesig,text="",font=fuente)
    ventDesig.lrespuesta.place(x=300,y=250)
    
    
    
    
    
    ventDesig.btnVol=tk.Button(ventDesig,text="Volver",bg="#00B37A",fg="white",command=lambda: Volver(ventDesig, principal),font=fuente)
    ventDesig.btnVol.place(x=1100,y=750)
    
    ventDesig.protocol("WM_DELETE_WINDOW",lambda: Volver(ventDesig, principal)) #Para que se cierre como Dios manda
    
    
    ventDesig.mainloop()             #Perro salchicha gordo bachcicha, toma solcito a la orilla del mar...