import os, time
from functions import *
os.system("cls")

while True:
    os.system("cls")
    print("\t\t Mini Agenda de Contactos\n")
    print("1)  Agregar un contacto: nombre, teléfono, email.")
    print("2)  Listar contactos: mostrar todos los contactos guardados.")
    print("3)  Buscar un contacto por nombre.")
    print("4)  Eliminar un contacto.")
    print("5)  Salir del programa.\n")

    try:

        opcion = int(input("Ingrese una opción.\n"))
        
        if opcion == 1:
            os.system("cls")
            print("Agregar un contacto:")
            agregar_contacto(contactos)
        elif opcion == 2:
            os.system("cls")
            print("Listar contactos:")
            listar_contacto(contactos)
        elif opcion == 3:
            os.system("cls")
            print("Buscar un contacto por nombre.")
            buscar_contacto(contactos)

        elif opcion == 4:
            os.system("cls")
            print("Eliminar un contacto.")
            eliminar_contacto(contactos)

        elif opcion == 5:
            os.system("cls")
            print("Salir del programa.")
            print("Chao pecao'...")
            break

        else:
            print("La opción ingresada no existe")

    except:
        print("El valor ingresado debe ser numerico")
        time.sleep(2)