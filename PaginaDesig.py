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
colorBotones="#25C7CA"
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
                ventDesig.grafica.get_tk_widget().place(x=50,y=250)
                
            #NO cumple desigualdad triangular
                
            else: 
                ventDesig.lrespuesta.config(text="Las medidas dadas no corresponden a un triangulo")
                
                
                ventDesig.grafica=FigureCanvasTkAgg(graficoNoTri(lados[0], lados[1], lados[2]),ventDesig)
                ventDesig.grafica.get_tk_widget().place(x=50,y=250)
                
                
                
            
       
        
    def Volver(ventanaActual,ventanaDestino):
        ventanaActual.withdraw()
        ventanaDestino.deiconify()
    
    #TKINTER
    
    #   PRINCIPAL
    #ventDesig=tk.Tk()
    ventDesig=tk.Toplevel(principal)
    ventDesig.title("Desigualdad Triangular")
    ventDesig.geometry("800x600")
    
    #   BOTONES Y LABELS
    ventDesig.titulo=tk.Label(ventDesig,text="Aqui va el titulo")
    ventDesig.titulo.place(x=350,y=50)
    ventDesig.desc=tk.Label(ventDesig,text="Aqui va la descripcion del programa")
    ventDesig.desc.place(x=300,y=100)
    ventDesig.lnum1=tk.Label(ventDesig,text="Numero 1:")
    ventDesig.lnum1.place(x=50, y=150)
    ventDesig.num1=tk.Entry(ventDesig,width=10)
    ventDesig.num1.place(x=150, y=150)
    ventDesig.lnum2=tk.Label(ventDesig,text="Numero 2:")
    ventDesig.lnum2.place(x=200, y=150)
    ventDesig.num2=tk.Entry(ventDesig,width=10)
    ventDesig.num2.place(x=300, y=150)
    ventDesig.lnum3=tk.Label(ventDesig,text="Numero 3:")
    ventDesig.lnum3.place(x=350, y=150)
    ventDesig.num3=tk.Entry(ventDesig,width=10)
    ventDesig.num3.place(x=450, y=150)
    
    ventDesig.btnRev=tk.Button(ventDesig,text="Revisar",command=Revisar)
    ventDesig.btnRev.place(x=550,y=150)
    ventDesig.lrespuesta=tk.Label(ventDesig,text="")
    ventDesig.lrespuesta.place(x=50,y=200)
    
    
    
    
    
    ventDesig.btnVol=tk.Button(ventDesig,text="Volver",bg=colorBotones,command=lambda: Volver(ventDesig, principal))
    ventDesig.btnVol.place(x=700,y=550)
    
    ventDesig.protocol("WM_DELETE_WINDOW",lambda: Volver(ventDesig, principal)) #Para que se cierre como Dios manda
    
    
    ventDesig.mainloop()             #Perro salchicha gordo bachcicha, toma solcito a la orilla del mar...