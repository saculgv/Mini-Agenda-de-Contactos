import os, time
os.system("cls")

# Requisitos del Proyecto
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.


contactos = []

def agregar_contacto(contactos):
    nombre = ""
    while len(nombre) < 3:
        nombre = input("Ingrese el nombre del nuevo contacto\n").lower().strip()
        if len(nombre) >= 3:
            print("Nombre guardado con éxito!\n")
            time.sleep(1)
        else:
            os.system("cls")
            print("Intente nuevamente. Debe ser mayor a 3 carácteres\n")
            time.sleep(2)
    
    
    telefono = ""
    while len(telefono) != 9:
        telefono = input("Ingrese el número de 9 dígitos:\n")
        if len(telefono) == 9:
            print("Número guardado con éxito!\n")
            time.sleep(1)
        else:
            print("Número equivocado, ingrese nuevamente.\n")
            time.sleep(2)
    
    email = ""
    while len(email) < 5 or "@" not in email:
        email = input("Ingrese el email:\n").lower().strip()
        if len(email) >= 5 and "@" in email:
            print("Correo ingresado con éxito!\n")
            time.sleep(1)
        else:
            print("email incorrecto. Verifique que tenga un @ en él.\n")
            time.sleep(2)
    contacto = [nombre, telefono, email]
    contactos.append(contacto) 

def listar_contacto(contactos):
    if len(contactos) == 0:
        os.system("cls")
        print("Primero ingrese un contacto.")
        time.sleep(2)
    else:
        for contacto in range(len(contactos)):
            print(contactos[contacto])
    os.system("Pause")

def buscar_contacto(contactos):
    if len(contactos) == 0:
        os.system("cls")
        print("Primero ingrese un contacto.")
        time.sleep(2)
    else:
        buscar = input("Ingrese el nombre que desea buscar:\n").lower().strip()
        encontrados = []
        for contacto in contactos:
            if buscar in contacto[0]:
                encontrados.append(contacto)
        os.system("cls")
        if encontrados:
            print("Contactos encontrados:\n")
            for contacto in encontrados:
                print(contacto)
        else:
            print("No se encontraron contactos con ese nombre.")
        os.system("Pause")

def eliminar_contacto(contactos):
    if len(contactos) == 0:
        os.system("cls")
        print("Primero ingrese un contacto.")
        time.sleep(2)
    else:
        bandera = False
        eliminar = input("Ingrese el nombre del contacto que desea eliminar:\n").lower().strip()
        for contacto in contactos:
            if eliminar in contacto[0]:
                contactos.remove(contacto)
                print("Contacto eliminado correctamente!")
                bandera = True
                time.sleep(2)
        if bandera == False:
            print("No se han encontrado coincidencias para eliminar.")
            time.sleep(2)
        os.system("Pause")