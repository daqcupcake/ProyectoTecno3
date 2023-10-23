"""
Pagina Principal Proyecto 1

Encargado: Andy Torres

Miembros:   Daniela Arias
            Sebastian Ortiz
            Andy Torres
            
Contenido:         
            
"""

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import random
import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def crearLCos(principal):
    #Funciones
    def mostrar_ocultar_txtX1(event):
        accion_seleccionada=ventLCos.listaccion.get()
        actualizar_medidas()
        if accion_seleccionada=="Calcular la longitud de un lado":
            ventLCos.lblangC.place(x=20,y=350)
            ventLCos.lblrespladoc.place(x=20,y=380)
            ventLCos.lblR.place(x=20,y=410)
            ventLCos.txtrespladoc.place(x=70,y=410)
            ventLCos.btnverificarlado.place(x=20,y=440)
            ventLCos.lblladoc.place_forget()
            ventLCos.lblrespangC.place_forget()
            ventLCos.txtrespangC.place_forget()
            ventLCos.btnverificarang.place_forget()
        elif accion_seleccionada=="Calcular la medida de un angulo":
            ventLCos.lblladoc.place(x=20,y=350)
            ventLCos.lblrespangC.place(x=20,y=380)
            ventLCos.lblR.place(x=20,y=410)
            ventLCos.txtrespangC.place(x=70,y=410)
            ventLCos.btnverificarang.place(x=20,y=440)
            ventLCos.lblangC.place_forget()
            ventLCos.lblrespladoc.place_forget()
            ventLCos.txtrespladoc.place_forget()
            ventLCos.btnverificarlado.place_forget()
    
    def generar_medidas():
        a = random.randint(1, 25)
        b = random.randint(1, 25)
        anguloC = random.randint(1, 170)
        C = anguloC*(m.pi/180)
        c = m.sqrt(a**2+b**2-2*a*b*m.cos(C))
        A = m.asin((m.sin(C)/c)*a)
        anguloA = A*(180/m.pi)
        anguloB = 180-anguloC-anguloA
        return a,b,c,anguloA,anguloB,anguloC
    
    def actualizar_medidas():
        # Generar nuevas medidas de lados y angulos
        global ladoa, ladob,ladoc,anguloA,anguloB,anguloC,lados
        ladoa,ladob,ladoc,anguloA,anguloB,anguloC = generar_medidas()
        # Actualizar las etiquetas en la interfaz grafica
        ventLCos.lblladoa.config(text=f"La medida del lado A es: {ladoa} u.l.")
        ventLCos.lblladob.config(text=f"La medida del lado B es: {ladob} u.l")
        ventLCos.lblladoc.config(text=f"La medida del lado C es: {ladoc:.4f} u.l")
        ventLCos.lblangC.config(text=f"La medida del angulo C es: {anguloC} grados")
        ventLCos.txtrespladoc.delete(0, 'end')  # Borra el contenido del primer Entry
        ventLCos.txtrespangC.delete(0, 'end')  # Borra el contenido del segundo Entry
        lados = [ladoa,ladob,ladoc]
        lados.sort(reverse=True)
        ventLCos.grafica=FigureCanvasTkAgg(graficoTri(lados[0], lados[1], lados[2]),ventLCos)
        ventLCos.grafica.get_tk_widget().place(x=450,y=230)
        
    def verificar_respuestaang():
        global anguloC
        try:
            respuesta_usuario = float(ventLCos.txtrespangC.get())
        except ValueError:
             messagebox.showerror("Error","Por favor ingresar un valor numerico.")
             return
        respuesta = float(anguloC)
        if respuesta-0.1<=respuesta_usuario<=respuesta+0.1:
            messagebox.showinfo("Verificacion", "Respuesta correcta!")
        else:
            messagebox.showerror("Verificacion", f"Respuesta incorrecta. La respuesta correcta es {respuesta}.")
    
    def verificar_respuestalado():
        global ladoc
        try:
            respuesta_usuario = float(ventLCos.txtrespladoc.get())
        except ValueError:
            messagebox.showerror("Error","Por favor ingresar un valor numerico.")
            return
        respuesta = float(ladoc)
        if respuesta-0.1<=respuesta_usuario<=respuesta+0.1:
            messagebox.showinfo("Verificacion", "Respuesta correcta!")
        else:
            messagebox.showerror("Verificacion", f"Respuesta incorrecta. La respuesta correcta es {respuesta}.")
    
    def graficoTri(a,b,c):
        m=(b**2-c**2-a**2)/(-2*a)
        h=np.sqrt(c**2-m**2)
        #print(m,h)
        fig, ax = plt.subplots()
        
        trigX = [0,a,m,0]
        trigY = [0,0,h,0]
        
        plt.plot(trigX,trigY,"o")
        plt.plot(trigX,trigY,"-")
        plt.axis("equal")
        
        return fig
    
    def Volver(ventanaActual,ventanaDestino):
        ventanaActual.withdraw()
        ventanaDestino.deiconify()
    
    #Ventana
    ventLCos=Toplevel(principal)
    ventLCos.geometry("1200x800")
    ventLCos.title("Ley de Coseno")
    
    
    #Variables Globales
    accion = ["Calcular la longitud de un lado","Calcular la medida de un angulo"]
    fuentep=("Arial",20,"bold")
    fuente=("Arial",15)
    ladoa,ladob,ladoc,anguloA,anguloB,anguloC = generar_medidas()
    lados = [ladoa,ladob,ladoc]
    lados.sort(reverse=True)
    colorBotones="#25C7CA"
    
    #Crear elementos
    ventLCos.lblprincipal= Label(ventLCos,text="Ley de Cosenos",font=fuentep,fg="#006DCC")
    ventLCos.lblinfo= Message(ventLCos,text="A traves de esta ventana, podras practicar determinar la medida de un lado de un triangulo o la medida de un angulo en grados mediante la Ley de Cosenos. Para ello, debes seleccionar si deseas calcular la medida de un lado o un angulo. Una vez que lo seleccionas, utilizando los valores que se brindan aleatoriamente,  puedes determinar cada medida. Ademas, una vez que lo verifiques podras ver como se ve graficamente dicho triangulo.\nNota: En las respuestas que tengan expansion decimal infinita periodica utiliza unicamente dos decimales sin redondear.",font=fuente,width=1100)
    ventLCos.lblnota= Label(ventLCos,text="Nota: las medidas proporcionadas de los angulos estan en grados.",font=fuente)
    ventLCos.lblaccion= Label(ventLCos, text="Elija la accion que desea realizar:",font=fuente)
    ventLCos.listaccion= Combobox(ventLCos, values=accion, width=26,font=fuente)  
    ventLCos.grafica=FigureCanvasTkAgg(graficoTri(lados[0], lados[1], lados[2]),ventLCos)
    
    
    #Asignar la funcion al evento de seleccion en el combobox
    ventLCos.listaccion.bind("<<ComboboxSelected>>",mostrar_ocultar_txtX1)
    
    #Colocar elementos
    ventLCos.lblprincipal.place(relx=0.5, y=15, anchor="center")
    ventLCos.lblinfo.place(x=20,y=30)
    ventLCos.lblaccion.place(x=20,y=230)
    ventLCos.listaccion.place(x=20,y=260)
    ventLCos.grafica.get_tk_widget().place(x=450,y=230)
    
    
    #elementos que aparecen siempre
    ventLCos.lblladoa= Label(ventLCos,text=f"La medida del lado A es: {ladoa} u.l",font=fuente)
    ventLCos.lblladoa.place(x=20,y=290)
    ventLCos.lblladob= Label(ventLCos,text=f"La medida del lado B es: {ladob} u.l",font=fuente)
    ventLCos.lblladob.place(x=20,y=320)
    ventLCos.lblR= Label(ventLCos,text="R/",font=fuente)
    ventLCos.btnverificarlado= Button(ventLCos,text="Verificar",font=fuente,command=verificar_respuestalado)
    ventLCos.btnverificarang= Button(ventLCos,text="Verificar",font=fuente,command=verificar_respuestaang)
    ventLCos.btnnuevo=Button(ventLCos,text="Nuevo",font=fuente,command=actualizar_medidas)
    ventLCos.btnnuevo.place(x=120,y=440)
    
    #elementos que aparecen si se desea determinar la medida de un lado
    ventLCos.lblangC= Label(ventLCos,text=f"La medida del angulo C es: {anguloC} grados",font=fuente)
    ventLCos.lblrespladoc= Label(ventLCos,text="Determine la medida del lado C",font=fuente)
    ventLCos.txtrespladoc= Entry(ventLCos,width=16,font=fuente)
    
    #elementos que aparecen si se desea determinar la medida de un angulo
    ventLCos.lblladoc= Label(ventLCos,text=f"La medida del lado C es: {ladoc} u.l",font=fuente)
    ventLCos.lblrespangC= Label(ventLCos,text="Determine la medida del angulo C",font=fuente)
    ventLCos.txtrespangC= Entry(ventLCos,width=16,font=fuente)
    
    ventLCos.btnVol=Button(ventLCos,text="Volver",bg="#00B37A",fg="white",command=lambda: Volver(ventLCos, principal),font=fuente)
    ventLCos.btnVol.place(x=1100,y=750)
    
    ventLCos.protocol("WM_DELETE_WINDOW",lambda: Volver(ventLCos, principal)) #Para que se cierre como Dios manda
    
    ventLCos.mainloop()
