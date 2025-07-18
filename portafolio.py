flag = True

Tareas = []

Estado_Tareas = {}



while flag:
    print("--- Gestor de Tareas ---\n 1. Agregar tarea \n2. Ver tareas \n3. Marcar tarea como completada \n4. Eliminar tarea \n5. Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":

        
    elif opcion == "2":

    
    elif opcion == "3":


    elif opcion == "4":


    elif opcion == "5":
        flag = False

    else:
        print("opcion no valida")


def AgregarTarea():

    nombre = input("ingrese el nombre de la tarea: ")
    if nombre not in Tareas:
        Tareas.append(nombre)

    print("1. Pendiente \n2. Completada")
    Estado = input("En que estado se encuentra la tarea?: ")

    if nombre not in Estado_Tareas:
        if Estado == "1":
            Estado_Tareas[nombre] = "Pendiente"
        elif Estado == "2":
            Estado_Tareas[nombre] = "Completada"
        else:
            print("Opcion no valida.")

            