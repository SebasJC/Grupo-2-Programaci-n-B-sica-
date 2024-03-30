titulos = []
descripciones = []
fechas = []
costos = []
estados = []
tareas = []
opcion = 0
opcion_editar = 0

while opcion != 7:
    
    print("\n--- Menú de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completa")
    print("4. Editar tarea")
    print("5. Borrar tarea")
    print("6. Guardar o cargar tareas")
    print("7. Salir")
   
    opcion = int(input("Digite la opción que desea seguir: "))
    
    if opcion == 1:
        titulo = str(input("Indique el título de la tarea. "))
        titulos.append(titulo)
        descripcion = str(input("Indique la descripción de la tarea. "))
        descripciones.append(descripcion)
        fecha = str(input("Indique la fecha de la tarea. "))
        fechas.append(fecha)
        costo = float(input("Indique el costo de la tarea. "))
        costos.append(costo)
        estado = "Incompleta"
        estados.append(estado)
        tareas = titulos + descripciones + fechas + costos + estados
    elif opcion == 2:
        for i in range (len(titulos)):
            print("Titulo: ", titulos[i], " - Descripción: ", descripciones[i], " - Fecha: ", fechas[i], " - Costo: " , costos[i], "Estado: ", estados[i])
    elif opcion == 3:
        tarea = str(input("Digite el título de la tarea que desea marcar como completa: "))
        for i in range (len(titulos)):
            if tarea == titulos[i]:
                estados[i] = "Completa"
            else:
                print("No hay ninguna tarea con ese título.")
#Funcion de editar tareas
    elif opcion == 4:
        editar_tarea = input("Digite el título de la tarea que desea editar: ")
        hallado = False
        for i in range (len(titulos)):
            if titulos[i] == editar_tarea:
              hallado = True
              print("Tarea hallada: ")
              print("Titulo:", titulos[i])
              print("Descripcion:", descripciones[i])
              print("Costo:", costos[i])
              print("Fecha:", fechas[i])
              print("Estado", estados[i])
    
            #Solicitar al usuario que ingrese los valor que desea cambiar
              descripcion_nueva = input("Nueva descripcion: ")
              fecha_nueva = input("Nueva fecha (deje en blanco si no desea cambiar): ")
              costo_nuevo = input(("Nuevo costo (deje en blanco si no desea cambiar): "))
    
            #Actualizar los valores
              if descripcion_nueva:
                    descripciones[i] = descripcion_nueva
              if fecha_nueva:
                fechas[i] = fecha_nueva
              if costo_nuevo:
                costos[i] = float(costo_nuevo)
              print("Tarea editada de forma correcta.")
      
              break
        if not encontrado:
           print("No se ninguna tarea con ese titulo.")
           
    #Funcion para borrar tarea   
    elif opcion == 5:
        borrar_tarea = input("Digite el título de la tarea que desea borrar: ")
        encontrado = False
        for i in range(len(titulos)):
            if titulos[i] == borrar_tarea:
                encontrado = True
                del titulos[i]
                del descripciones[i]
                del fechas[i]
                del costos[i]
                del estados[i]
                print("Tarea borrada exitosamente.")
                break

        if not encontrado:
            print("No se encontró ninguna tarea con ese título.")
        
        
        
    elif opcion == 6:
        print("En progreso.")
        
    elif opcion == 7:
        print("¡Hasta luego!")

    else:
        print("Opción no válida. Por favor, seleccione una opción correctamente.")
        
        

            
