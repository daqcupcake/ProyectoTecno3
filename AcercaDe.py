import tkinter as tk

def creaVentana2(vent1):
    #root = Tk()
    ventana2=tk.Toplevel(vent1)
    #root.geometry("400x100")
    ventana2.geometry("800x600")
    ventana2.title("Acerca de")
    
    ventana2.lblArea = tk.Label(ventana2,text ="")
    ventana2.lblArea.grid(row=0,column=2)




    # Crear las etiquetas
    ventana2.lblTitulo = tk.Label(ventana2, text="Acerca del proyecto", font=("Arial", 16))
    ventana2.lbldescripcion1 = tk.Label(ventana2, text="Este proyecto fué realizado para el curso Tecnologías Digitales Aplicadas a la Matemática Educativa III de la carrera Enseñanza de la Matemática con Entornos Tecnológicos del Tecnológico de Costa Rica.", font=("Arial", 12), wraplength=(600))
    ventana2.lbldescripcion2 = tk.Label(ventana2, text="El objetivo de este proyecto es aplicar conceptos de Programación Orientada a Objetos (POO) y comandos básicos de Python para crear una clase que represente un triángulo y sus propiedades, así como implementar diversos métodos relacionados con el mismo. La aplicación computacional resultante incluirá una interfaz de usuario funcional con un diseño apropiado, centrándose en abordar temas como la desigualdad triangular, el Teorema de Pitágoras, la Ley de Senos y la Ley de Cosenos.", font=("Arial", 12), wraplength=(600))
    ventana2.lblestudiantes = tk.Label(ventana2, text="""El proyecto fué realizado por los estudiantes:
    - Daniela Arias Quesada
    - Sebastián Ortiz González
    - Andy Torres Alfaro
    """)
    ventana2.lblprofesora = tk.Label(ventana2, text="""Docente del curso:
    - M.Sc. Rebeca Ortega Solís
    """)
    ventana2.lblsemestre = tk.Label(ventana2, text="Proyecto realizado durante el segundo semestre del 2023.")
    
    
    # Crear el botón de calcular
    ventana2.botonPrincipal = tk.Button(ventana2, text="Página Principal", command=lambda:volverArchivo01(ventana2,vent1))
    
            
            
    # Colocar los elementos en la ventana
    ventana2.lblTitulo.place(x=300, y=20, anchor="center")
    ventana2.lbldescripcion1.place(x=50, y=80)
    ventana2.lbldescripcion2.place(x=50, y=120)
    ventana2.lblestudiantes.place(x=50, y=220)
    ventana2.lblprofesora.place(x=50, y=310)
    ventana2.lblsemestre.place(x=150, y=350)
    ventana2.botonPrincipal.place(x=250, y=400)
    ventana2.protocol("WM_DELETE_WINDOW",lambda: volverArchivo01(ventana2, vent1))
    
    
    def volverArchivo01(ventanaActual,ventanaDestino):
         ventanaActual.withdraw()
         ventanaDestino.deiconify()

