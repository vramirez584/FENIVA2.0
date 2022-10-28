#Repositorio GitHub: 
import tkinter as tk 
from tkinter import ttk 
import time 
#Funcion FechaHora
def FechaHora():
    FechaHoraActual = time.strftime("%c")
    #Etiqueta FechaHora
    LabelFechaHora = ttk.Label(text=f"{FechaHoraActual}")
    LabelFechaHora.place(x=1, y=91)
#Funcion AgregarEmpleado
def FunctionAgregarEmpleado():

  LabelNombreEmpleado = ttk.Label(text="Ingrese el nombre del empleado:")
  LabelNombreEmpleado.place(x=1, y=150)
  #Caja NombreEmpleado
  BoxNombreEmpleado = ttk.Entry()
  BoxNombreEmpleado.place (x=1, y=200)
  LabelIdentificacionEmpleado = ttk.Label(text="Ingrese el numero de cedula del empleado:")
  LabelIdentificacionEmpleado.place(x=1, y=250)
  #Caja IdentificacionEmpleado
  BoxIdentificacionEmpleado = ttk.Entry()
  BoxIdentificacionEmpleado.place (x=1, y=300)
ventana = tk.Tk()
ventana.title("FENIVA")
ventana.config(width= 400, height = 1000)
#Etiqueta CodigoEmpleado
LabelCodigoEmpleado = ttk.Label(text="Ingrese el codigo del empleado:")
LabelCodigoEmpleado.place(x=1, y=1)
#Caja CodigoEmpleado
BoxCodigoEmpleado = ttk.Entry()
BoxCodigoEmpleado.place (x=1, y=31, width = 100)
#Boton CodigoEmpleado
ButtonCodigoEmpleado = ttk.Button(text= "Aceptar", command=FechaHora)
ButtonCodigoEmpleado.place (x=1, y=61)
#Boton AgregarEmpleado
ButtonAgregarEmpleado = ttk.Button(text="Agregar empleado", command= FunctionAgregarEmpleado)
ButtonAgregarEmpleado.place (x=100, y=61)
ventana.mainloop()
