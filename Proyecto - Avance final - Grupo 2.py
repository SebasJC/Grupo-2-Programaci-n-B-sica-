# Función para guardar las tareas en un archivo CSV
def guardar_tareas():
    try:
        # Abrir el archivo 'tareas.csv' en modo escritura ('w')
        with open('tareas.csv', 'w', newline='') as archivo_csv:
            # Interactuar sobre las listas de títulos, descripciones, fechas, costos y estados
            # y escribir cada tarea como una fila en el archivo CSV
            for tarea in zip(titulos, descripciones, fechas, costos, estados):
                fila = ','.join(map(str, tarea))  # Convertir la tarea a una cadena separada por comas
                archivo_csv.write(fila + '\n')    # Escribir la fila en el archivo CSV
        print("Tareas guardadas correctamente.")
    except IOError:
        print("Ocurrió un error al guardar las tareas.")

# Función para cargar las tareas desde un archivo CSV
def cargar_tareas():
    try:
        # Abrir el archivo 'tareas.csv' en modo lectura ('r')
        with open('tareas.csv', 'r') as archivo_csv:
            # Interactuar sobre cada fila del archivo CSV
            # y cargar los datos de las tareas en las listas correspondientes
            for fila in archivo_csv:
                tarea = fila.strip().split(',')    # Dividir la fila en valores individuales
                titulos.append(tarea[0])           # Agregar el título a la lista de títulos
                descripciones.append(tarea[1])     # Agregar la descripción a la lista de descripciones
                fechas.append(tarea[2])            # Agregar la fecha a la lista de fechas
                costos.append(float(tarea[3]))     # Convertir el costo a float y agregarlo a la lista de costos
                estados.append(tarea[4])           # Agregar el estado a la lista de estados
        print("Tareas cargadas correctamente.")
    except IOError:
        print("No se encontró ningún archivo de tareas.")

# Listas para almacenar los datos de las tareas
titulos = []
descripciones = []
fechas = []
costos = []
estados = []

# Bucle principal del programa
opcion = 0
while opcion != 8:
    # Mostrar el menú de opciones
    print("\n--- Menú de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completa")
    print("4. Editar tarea")
    print("5. Borrar tarea")
    print("6. Guardar tareas")
    print("7. Cargar tareas")
    print("8. Salir")

    # Solicitar al usuario que elija una opción
    opcion = int(input("Digite la opción que desea seguir: "))

    # Opción 1: Agregar tarea
    if opcion == 1:
        # Solicitar al usuario información sobre la nueva tarea y agregarla a las listas
        titulo = str(input("Indique el título de la tarea: "))
        titulos.append(titulo)
        descripcion = str(input("Indique la descripción de la tarea: "))
        descripciones.append(descripcion)
        fecha = str(input("Indique la fecha de la tarea: "))
        fechas.append(fecha)
        costo = float(input("Indique el costo de la tarea: "))
        costos.append(costo)
        estado = "Incompleta"
        estados.append(estado)
    
    # Opción 2: Ver tareas
    elif opcion == 2:
        # Interactuar sobre las listas de títulos, descripciones, fechas, costos y estados
        # e imprimir cada tarea en el formato deseado
        for i in range(len(titulos)):
            print("Título: ", titulos[i], " - Descripción: ", descripciones[i], " - Fecha: ", fechas[i], " - Costo: ", costos[i], "Estado: ", estados[i])
    
    # Opción 3: Marcar tarea como completa
    elif opcion == 3:
        # Solicitar al usuario el título de la tarea que desea marcar como completa
        tarea = str(input("Digite el título de la tarea que desea marcar como completa: "))
        # Interactuar sobre la lista de títulos y, si se encuentra la tarea, cambiar su estado a "Completa"
        for i in range(len(titulos)):
            if tarea == titulos[i]:
                estados[i] = "Completa"
                break
        else:
            print("No hay ninguna tarea con ese título.")
    
    # Opción 4: Editar tarea
    elif opcion == 4:
        # Solicitar al usuario el título de la tarea que desea editar
        editar_tarea = input("Digite el título de la tarea que desea editar: ")
        encontrado = False
        # Interactuar sobre la lista de títulos y, si se encuentra la tarea, permitir al usuario editar sus detalles
        for i in range(len(titulos)):
            if titulos[i] == editar_tarea:
                encontrado = True
                print("Tarea hallada: ")
                print("Titulo:", titulos[i])
                print("Descripcion:", descripciones[i])
                print("Costo:", costos[i])
                print("Fecha:", fechas[i])
                print("Estado", estados[i])

                # Solicitar al usuario los nuevos detalles de la tarea y actualizarlos si es necesario
                descripcion_nueva = input("Nueva descripcion: ")
                fecha_nueva = input("Nueva fecha (deje en blanco si no desea cambiar): ")
                costo_nuevo = input(("Nuevo costo (deje en blanco si no desea cambiar): "))

                if descripcion_nueva:
                    descripciones[i] = descripcion_nueva
                if fecha_nueva:
                    fechas[i] = fecha_nueva
                if costo_nuevo:
                    costos[i] = float(costo_nuevo)
                print("Tarea editada de forma correcta.")
                break
        if not encontrado:
           print("No se encuentra ninguna tarea con ese título.")
    
    # Opción 5: Borrar tarea
    elif opcion == 5:
        # Solicitar al usuario el título de la tarea que desea borrar
        borrar_tarea = input("Digite el título de la tarea que desea borrar: ")
        encontrado = False
        # Interactuar sobre la lista de títulos y, si se encuentra la tarea, eliminarla de todas las listas
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
    
    # Opción 6: Guardar tareas
    elif opcion == 6:
        guardar_tareas()  # Llamar a la función para guardar las tareas en el archivo CSV
    
    # Opción 7: Cargar tareas
    elif opcion == 7:
        cargar_tareas()   # Llamar a la función para cargar las tareas desde el archivo CSV
    
    # Opción 8: Salir
    elif opcion == 8:
        print("¡Hasta luego!")  # Imprimir un mensaje de despedida
    
    # Manejo de opción no válida
    else:
        print("Opción no válida. Por favor, seleccione una opción correctamente.")