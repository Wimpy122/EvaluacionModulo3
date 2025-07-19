flag = True

Tareas = ["Evaluacion 1"]

Estado_Tareas = {"Evaluacion 1": "Completada"}

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
            Tareas.remove(nombre)


def VerTareas(lista):
    for tarea, estado in lista.items():
        print(f"\n{tarea} - {estado}")

def Modificar_Estado(lista):
    tarea = input("Ingrese nombre tarea: ")
    for diccionario in lista:   
        if tarea in lista:
            lista[tarea] = "Completada"
        else:
            print("Nombre no Encontrado")

def Eliminar_Tarea(Estado, Nombre):
    tarea = input("Ingrese nombre tarea: ")
    if tarea in Estado:
            del Estado[tarea]
    else:
        print("Nombre no Encontrado")
    
    if tarea in Nombre:
        Nombre.remove(tarea)
    else:
        print("Nombre no Encontrado")


while flag:
    print("\n--- Gestor de Tareas ---\n1. Agregar tarea \n2. Ver tareas \n3. Marcar tarea como completada \n4. Eliminar tarea \n5. Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        AgregarTarea()
        
    elif opcion == "2":
        VerTareas(Estado_Tareas)
    
    elif opcion == "3":
        Modificar_Estado(Estado_Tareas)

    elif opcion == "4":
        Eliminar_Tarea(Estado_Tareas, Tareas)

    elif opcion == "5":
        flag = False
        
    else:
        print("opcion no valida")


