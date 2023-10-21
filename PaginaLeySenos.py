

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import random
import math as m
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def crearLSen(principal):
    #Funciones
    def mostrar_ocultar_txtX1(event):
        accion_seleccionada=ventLSen.listaccion.get()
        actualizar_medidas()
        if accion_seleccionada=="Calcular la longitud de un lado":
            ventLSen.lblangB.place(x=500,y=180)
            ventLSen.lblrespladob.place(x=500,y=220)
            ventLSen.lblR.place(x=500,y=260)
            ventLSen.txtrespladob.place(x=550,y=260)
            ventLSen.btnverificarlado.place(x=500,y=300)
            ventLSen.lblladob.place_forget()
            ventLSen.lblrespangB.place_forget()
            ventLSen.txtrespangB.place_forget()
            ventLSen.btnverificarang.place_forget()
        elif accion_seleccionada=="Calcular la medida de un angulo":
            ventLSen.lblladob.place(x=500,y=180)
            ventLSen.lblrespangB.place(x=500,y=220)
            ventLSen.lblR.place(x=500,y=260)
            ventLSen.txtrespangB.place(x=550,y=260)
            ventLSen.btnverificarang.place(x=500,y=300)
            ventLSen.lblangB.place_forget()
            ventLSen.lblrespladob.place_forget()
            ventLSen.txtrespladob.place_forget()
            ventLSen.btnverificarlado.place_forget()
    
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
        ventLSen.lblladoa.config(text=f"La medida del lado A es: {ladoa} u.l.")
        ventLSen.lblangA.config(text=f"La medida del angulo A es: {anguloA:.4f} grados")
        ventLSen.lblladob.config(text=f"La medida del lado B es: {ladob} u.l")
        ventLSen.lblangB.config(text=f"La medida del angulo B es: {anguloB:.4f} grados")
        ventLSen.txtrespladob.delete(0, 'end')  # Borra el contenido del primer Entry
        ventLSen.txtrespangB.delete(0, 'end')  # Borra el contenido del segundo Entry
        lados = [ladoa,ladob,ladoc]
        lados.sort(reverse=True)
        ventLSen.grafica=FigureCanvasTkAgg(graficoTri(lados[0], lados[1], lados[2]),ventLSen)
        ventLSen.grafica.get_tk_widget().place(x=40,y=200)
        
    def verificar_respuestaang():
        global anguloB
        try:
            respuesta_usuario = float(ventLSen.txtrespangB.get())
        except ValueError:
             messagebox.showerror("Error","Por favor ingresar un valor numerico.")
             return
        respuesta = float(anguloB)
        if respuesta-0.1<=respuesta_usuario<=respuesta+0.1:
            messagebox.showinfo("Verificacion", "Respuesta correcta!")
        else:
            messagebox.showerror("Verificacion", f"Respuesta incorrecta. La respuesta correcta es {respuesta}.")
    
    def verificar_respuestalado():
        global ladob
        try:
            respuesta_usuario = float(ventLSen.txtrespladob.get())
        except ValueError:
            messagebox.showerror("Error","Por favor ingresar un valor numerico.")
            return
        respuesta = float(ladob)
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
    #ventLSen = Tk()
    ventLSen=Toplevel(principal)
    ventLSen.geometry("800x600")
    ventLSen.title("Ley de Senos")
    
    
    #Variables Globales
    accion = ["Calcular la longitud de un lado","Calcular la medida de un angulo"]
    fuentep=("Arial",17,"bold")
    fuente=("Arial",15)
    ladoa,ladob,ladoc,anguloA,anguloB,anguloC = generar_medidas()
    lados = [ladoa,ladob,ladoc]
    lados.sort(reverse=True)
    colorBotones="#25C7CA"
    
    #Crear elementos
    ventLSen.lblprincipal= Label(ventLSen,text="Ley de Senos",font=fuentep)
    ventLSen.lblinfo= Label(ventLSen,text="En esta ventana podras elegir entre calcular la medida de un lado o angulo utilizando la ley de senos.",font=fuente)
    ventLSen.lblnota= Label(ventLSen,text="Nota: las medidas proporcionadas de los angulos estan en grados.",font=fuente)
    ventLSen.lblaccion= Label(ventLSen, text="Elija la accion que desea realizar:",font=fuente)
    ventLSen.listaccion= Combobox(ventLSen, values=accion, width=26,font=fuente)  
    ventLSen.grafica=FigureCanvasTkAgg(graficoTri(lados[0], lados[1], lados[2]),ventLSen)
    
    
    #Asignar la funcion al evento de seleccion en el combobox
    ventLSen.listaccion.bind("<<ComboboxSelected>>",mostrar_ocultar_txtX1)
    
    #Colocar elementos
    ventLSen.lblprincipal.place(relx=0.5, y=15, anchor="center")
    ventLSen.lblinfo.place(x=20,y=30)
    ventLSen.lblnota.place(x=20,y=60)
    ventLSen.lblaccion.place(x=20,y=100)
    ventLSen.listaccion.place(x=20,y=140)
    ventLSen.grafica.get_tk_widget().place(x=0,y=200)
    
    
    #elementos que aparecen siempre
    ventLSen.lblladoa= Label(ventLSen,text=f"La medida del lado A es: {ladoa} u.l",font=fuente)
    ventLSen.lblladoa.place(x=500,y=100)
    ventLSen.lblangA= Label(ventLSen,text=f"La medida del angulo A es: {anguloA:.4f} grados",font=fuente)
    ventLSen.lblangA.place(x=500,y=140)
    ventLSen.lblR= Label(ventLSen,text="R/",font=fuente)
    ventLSen.btnverificarlado= Button(ventLSen,text="Verificar",font=fuente,command=verificar_respuestalado)
    ventLSen.btnverificarang= Button(ventLSen,text="Verificar",font=fuente,command=verificar_respuestaang)
    ventLSen.btnnuevo=Button(ventLSen,text="Nuevo",font=fuente,command=actualizar_medidas)
    ventLSen.btnnuevo.place(x=600,y=300)
    
    ventLSen.btnVol=Button(ventLSen,text="Volver",bg=colorBotones,command=lambda: Volver(ventLSen, principal))
    ventLSen.btnVol.place(x=700,y=550)
    
    ventLSen.protocol("WM_DELETE_WINDOW",lambda: Volver(ventLSen, principal)) #Para que se cierre como Dios manda
    
    #elementos que aparecen si se desea determinar la medida de un lado
    ventLSen.lblangB= Label(ventLSen,text=f"La medida del angulo B es: {anguloB:.4f} grados",font=fuente)
    ventLSen.lblrespladob= Label(ventLSen,text="Determine la medida del lado B",font=fuente)
    ventLSen.txtrespladob= Entry(ventLSen,width=16,font=fuente)
    
    #elementos que aparecen si se desea determinar la medida de un angulo
    ventLSen.lblladob= Label(ventLSen,text=f"La medida del lado B es: {ladob} u.l",font=fuente)
    ventLSen.lblrespangB= Label(ventLSen,text="Determine la medida del angulo B",font=fuente)
    ventLSen.txtrespangB= Entry(ventLSen,width=16,font=fuente)
    
    ventLSen.mainloop()
