lista_estudiantes=[]
ListaTitulo=["NOMBRE","EDAD","CURSO","PROMEDIO"]
listacursos=["4° Basico","7° Basico","8° Basico", "1° Basico","2° Basico","3° Basico","5° Basico","6° Basico"]
def agregar_estudiante():
    while True:
        try:
            nombre=input("Ingrese el nombre del estudiante: ")
            edad=int(input("Ingrese la edad del estudiante: "))
            curso=input("Ingrese el curso del estudiante, Ejemplo (4° Basico): ")
            promedio=float(input("Ingrese el promedio del estudiante, Ejemplo (6.4): "))
        except ValueError:
            print("Error, ingrese un valor valido")
        else:
            estudiante={
                "Nombre":nombre,
                "Edad":edad,
                "Curso":curso,
                "Promedio":promedio,         
                }
            lista_estudiantes.append(estudiante)
            print("Datos de estudiante ingresados correctamente")
            print("")
            break
def ver_estudiantes():
    for x in lista_estudiantes:
        print(x)
        print("")
def modificar_estudiante():
    print("")
def eliminar_estudiante():
        ver_estudiantes()
        try:
            op=input("ingrese un nombre del estudiante que desea borrar: ")
        except ValueError:
            print("Ingrese una opcion valida")
        else: 
            if :
                lista_estudiantes.remove(op)
                print("")
                print("##ESTUDIANTE ELIMINADO CON EXITO##")
                print("")
            else:
                ("El estudiante no se encuentra en la lista")
def guardar_archivo():
    with open("Estudiantes.txt","w",encoding="utf-8") as archivo:
        archivo.write(ListaTitulo)
        for x in lista_estudiantes:
            archivo.write(x)
def mostrar_menu():
        print("1.- Agregar estudiante")
        print("2-  Ver todos los estudiantes")
        print("3.- Modificar producto")
        print("4.- Eliminar producto")
        print("5.- Guardar coleccion en un archivo")
        print("6.- Salir del programa")
        print("")
def menu():
    print("")
    while True:
        mostrar_menu()
        try:
            opcion=int(input("Seleccione una opcion: "))
        except ValueError:
            print("Opcion invalida, intentelo de nuevo")
        else:
            if opcion==1:
                agregar_estudiante()
            elif opcion==2:
                ver_estudiantes()
            elif opcion==3:
                modificar_estudiante()
            elif opcion==4:
                eliminar_estudiante()
            elif opcion==5:
                guardar_archivo()
            elif opcion==6:
                break
            else:
                print("Seleccione una opcion valida, intentelo de nuevo")
