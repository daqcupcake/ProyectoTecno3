
"""
Página Principal Proyecto 1

Encargado: Daniela Arias 

Miembros:   Daniela Arias
            Sebastián Ortiz
            Andy Torres
            
Contenido: El programa contiene la primera pantalla que funciona como menú para todo el proyecto           
            
"""

#IMPORTS
import tkinter as tk

from PaginaDesig import crearPaginaDesig
from PaginaPitagoras import crearPaginaPitagoras
from PaginaLeySenos import crearLSen
from PaginaLeyCoseno import crearLCos
from AcercaDe import creaVentana2

#VARIABLES GLOBALES
colorFondo="#FFFFFF"
colorTexto="#003C71"
colorBotones="#64D1AA"
fuente=("Arial",15)




    

    

    


#TKINTER

#   PRINCIPAL

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()  #define que esta es la ventana principal
        
        self.title("Página Principal Triángulos")
        self.geometry("800x600")


        #   BOTONES Y LABELS
        self.titulo=tk.Label(self,text="GeomeTRIX Máster",font=('Arial 24 bold'),justify="center",fg="#006DCC")
        self.titulo.place(x=260,y=20)
        self.titulo2=tk.Label(self,text="Domina la geometría de triángulos en un toque.",font=fuente,fg=colorTexto)
        self.titulo2.place(x=180,y=80)
        self.desc=tk.Message(self,text="Reciban la bienvenida a la app donde aprenderás sobre Desigualdad Triangular, el teorema de Pitágoras, Ley de Senos y Ley de Cosenos. En ella, encontrarás práctica ilimitada sobre los diferentes temas y recibirás retroalimentación a medida que respondes cada ejercicio. En cada app, a parte de practicar los diferentes procedimientos, podrás visualizar la gráfica de cada triángulo.",font=fuente,width=755)
        self.desc.place(x=20,y=125)
        self.titulo3=tk.Label(self,text="Para acceder, oprime el tema que te gustaría practicar:",font=fuente,fg=colorTexto)
        self.titulo3.place(x=25,y=260)
        
        
        self.btnDes=tk.Button(self,text="Desigualdad triangular",bg=colorBotones,command=self.Desigualdad,font=('Arial 18'),width=20)
        self.btnDes.place(x=50,y=320)
        self.btnPit=tk.Button(self,text="Teorema de Pitágoras",bg=colorBotones,command=self.Pitagoras,font=('Arial 18'),width=20)
        self.btnPit.place(x=400,y=320)
        self.btnLSen=tk.Button(self,text="Ley de Senos",bg=colorBotones,command=self.LeySen,font=('Arial 18'),width=20)
        self.btnLSen.place(x=50,y=410)
        self.btnLCos=tk.Button(self,text="Ley de Cosenos",bg=colorBotones,command=self.LeyCos,font=('Arial 18'),width=20)
        self.btnLCos.place(x=400,y=410)
        self.btnAcd=tk.Button(self,text="Acerca de",bg="#00B37A",fg="white",command=self.AcercaDe,font=fuente)
        self.btnAcd.place(x=675,y=550)
        #FUNCIONES

    def Desigualdad(self):
        self.withdraw()
        crearPaginaDesig(self)
        
    def Pitagoras(self):
        self.withdraw()
        crearPaginaPitagoras(self)
    
    def LeySen(self):
        self.withdraw()
        crearLSen(self)
        
    def LeyCos(self):
        self.withdraw()
        crearLCos(self)
        
    def AcercaDe(self):
        self.withdraw()
        creaVentana2(self)
        



#PRINCIPAL
if __name__=="__main__":
    app=Principal()
    app.mainloop()


