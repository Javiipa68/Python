import json

# Función para guardar la agenda en un archivo
def guardar_agenda(agenda, archivo='agenda.json'):
    with open(archivo, 'w') as f:
        json.dump(agenda, f, indent=4)
    print("Agenda guardada exitosamente.")

# Función para cargar la agenda desde un archivo
def cargar_agenda(archivo='agenda.json'):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("No se encontró el archivo de la agenda. Se creará una nueva agenda.")
        return {}

# Función para añadir un nuevo contacto a la agenda
def añadir_contacto(agenda):
    nombre = input('Introduce el nombre: ')
    dirección = input('Introduce la dirección: ')
    email = input('Introduce el email: ')
    teléfono = input('Introduce el teléfono: ')
    
    # Añadir el contacto al diccionario de la agenda
    agenda[nombre] = {
        'Nombre': nombre,
        'Dirección': dirección,
        'Email': email,
        'Teléfono': teléfono
    }
    
    guardar_agenda(agenda)  # Guardar la agenda actualizada en el archivo

# Función para consultar un contacto en la agenda
def consultar_contacto(agenda, nombre):
    contacto = agenda.get(nombre)
    if contacto:
        print(f"Nombre: {contacto['Nombre']}")
        print(f"Dirección: {contacto['Dirección']}")
        print(f"Email: {contacto['Email']}")
        print(f"Teléfono: {contacto['Teléfono']}")
    else:
        print('Contacto no encontrado')

# Menú principal que une todas las funciones
def menu():
    agenda = cargar_agenda()  # Cargar la agenda al iniciar
    
    while True:
        print("\n1. Añadir contacto")
        print("2. Consultar contacto")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            añadir_contacto(agenda)  # Llamada a la función para añadir contacto
        elif opcion == '2':
            nombre = input('Introduce el nombre del contacto a buscar: ')
            consultar_contacto(agenda, nombre)  # Llamada a la función para consultar contacto
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecución del menú
if __name__ == '__main__':
    menu()