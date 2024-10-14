def adivinar_palabra(letra_prueba, palabra_intento):
    
    palabra_adivinar = "karma"
    letra_en_palabra = letra_prueba in palabra_adivinar
    print(f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}")
    resultado_adivinanza = (palabra_intento == palabra_adivinar) and (len(palabra_intento) == len(palabra_adivinar)
    print(f"El jugador gana: {resultado_adivinanza})

adivinar_palabra("a", "engaño")

#Ejercicio práctico uso de listas

from io import open



libros = []

def aumentar_biblioteca(nuevo_libro):

    archivo = open('libros.txt', 'r')

    libros = archivo.read().splitlines()

    archivo.close()

    libros.append(nuevo_libro)

    print("La biblioteca de libros leídos es:", libros )

    return libros

   

def primer_libro_leido(libro):

    print("El primer libro que he leído es:", libro[0])

    return libro[0]



lib = aumentar_biblioteca('Las Aventuras de Huckleberry Finn')

primer_libro_leido(lib)




def agregar_experiencia(perfil_laboral, nueva_experiencia):
    """
    Añade una nueva experiencia laboral a un perfil laboral existente.
 
    Args:
        perfil_laboral (dict): Un diccionario que contiene información sobre el perfil laboral de una persona.
        nueva_experiencia (str): La nueva experiencia laboral a añadir al perfil.
 
    Returns:
        dict: El perfil laboral actualizado con la nueva experiencia añadida.
    """
    # Añadiendo una nueva experiencia laboral al perfil
    perfil_laboral['experiencias'] += [nueva_experiencia]
    return perfil_laboral
 
def generar_cv_reducido(perfil_laboral):
    """
    Imprime un CV reducido basado en la información del perfil laboral.
 
    Args:
        perfil_laboral (dict): Un diccionario que contiene información sobre el perfil laboral de una persona.
    """
    # Generando un CV reducido a partir del perfil laboral
    print(f"CV de {perfil_laboral['nombre']} {perfil_laboral['apellido']}")
    print(f"Edad: {perfil_laboral['edad']}, Ciudad: {perfil_laboral['ciudad']}")
    print(f"Experiencia: {perfil_laboral['experiencias']}")
 
# Creación del perfil laboral
perfil_laboral = {
    "nombre": "Ana",
    "apellido": "Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "experiencias": ["Ingeniera de software en XYZ Corp"]
}
 
# Añadiendo una nueva experiencia laboral
nueva_experiencia = "Gerente de proyecto en ABC Inc"
perfil_laboral = agregar_experiencia(perfil_laboral, nueva_experiencia)
 
# Generando el CV reducido
generar_cv_reducido(perfil_laboral)
