import time
def Menu():
  Opcion = 0
  isInt = True
  isInt2 = True
  print("\t*****FENIVA*****\nBienvenido a FENIVA.\nPor favor, seleccione la opcion que necesite.\n")
  while(Opcion != 4):
    print("Opcion 1: Hacer un registro de entrada.\nOpcion 2: Visualizar un registro de entrada.\nOpcion 3: Agregar empleado a la lista.\nOpcion 4: Salir del programa.")
    try:
      Opcion = int(input("Opcion: "))
      if Opcion == 1:
        print("Vamos a ingresar un registro de entrada. Ingrese los siguientes datos: ")
        #NOMBRES
        while isInt == True:
          NombreCompleto = input("Digite sus nombre completo: ")
          try:
            int(NombreCompleto)
            print("Por favor, Ingrese nombres validos.")
          except ValueError:
            isInt=False
        #DOCUMENTO
        while True:
          try: 
            Documento = int(input("Digite su numero de documento: "))
            break
          except ValueError:
            print("Por favor, Ingrese un documento valido.")
        HoraLlegada = time.strftime("%c")
        Registro = str(f"Nombre: {NombreCompleto} Documento: {Documento} Hora de llegada:  {HoraLlegada}\n")
        Archivo = open("registro.txt","a")
        Archivo.write(Registro)
        Archivo.close()
      elif Opcion == 2:
        with open("registro.txt") as file_object:
          Consulta = file_object.readlines()
          DocumentoFiltro = input("Por favor, ingrese el numero de documento de la persona que desea consultar: ")
          Filtro = [x for x in Consulta if DocumentoFiltro in x]
        print("Estos son los registros encontrados: \n")
        print(Filtro)
      elif Opcion == 3:
        print("Vamos a ingresar un empleado nuevo. Ingrese los siguientes datos: ")
        #NOMBRES
        while isInt == True:
          NombreCompleto = input("Digite sus nombre completo: ")
          try:
            int(NombreCompleto)
            print("Por favor, Ingrese nombres validos.")
          except ValueError:
            isInt=False
        #DOCUMENTO
        while True:
          try: 
            Documento = int(input("Digite su numero de documento: "))
            break
          except ValueError:
            print("Por favor, Ingrese un documento valido.")
        Empleados = str(f"Nombre: {NombreCompleto} Documento: {Documento}\n")
        Archivo = open("empleados.txt","a")
        Archivo.write(Empleados)
        Archivo.close()
        print("Empleado agregado con exito!")
      elif Opcion == 4:
        print("Cerrando programa...")
      pass
    except ValueError:
        print("Opcion incorrecta. Por favor, ingrese una opcion valida")
Menu()
