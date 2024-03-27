tareas = []

def agregar_tarea():
    descripcion = input("Describa la nueva tarea: ")
    tareas.append({"descripcion": descripcion, "estado": "pendiente"})

def eliminar_tarea():
    listar_tareas()
    indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        print("Tarea eliminada correctamente.")
    else:
        print("Número de tarea no válido.")

def completar_tarea():
    listar_tareas()
    indice = int(input("Ingrese el número de la tarea a completar: ")) - 1
    if 0 <= indice < len(tareas):
        tareas[indice]["estado"] = "completada"
        print("Tarea completada correctamente.")
    else:
        print("Número de tarea no válido.")

def listar_tareas():
    if tareas:
        for indice, tarea in enumerate(tareas, start=1):
            print(f"{indice}. {tarea['descripcion']} - {tarea['estado']}")
    else:
        print("No hay tareas pendientes.")

def menu():
    while True:
        print("\\nGestor de Tareas Pendientes")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Completar tarea")
        print("4. Listar tareas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            listar_tareas()
        elif opcion == "5":
            print("Gracias por usar el gestor de tareas.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()