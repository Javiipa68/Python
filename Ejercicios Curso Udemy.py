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
# Función para recomendar película
def recomendar_pelicula(genero, edad):
    # Condicionales basados en el género y la edad
    if genero == "acción":
        if edad >= 13:
            return "Deadpool"
        else:
            return "Regreso al futuro"
    elif genero == "comedia":
        return "Aterriza como puedas"
    else:
        return "Explorar otros géneros"

# Asignar valores manualmente en lugar de pedir al usuario
genero_favorito = "acción"  # Puedes cambiar este valor por pruebas
edad = 26  # Puedes cambiar este valor por pruebas

# Llamar a la función con los datos definidos
pelicula_recomendada = recomendar_pelicula(genero_favorito, edad)

# Mostrar el resultado


print(f"Teniendo en cuenta tu edad ({edad}) y tu género favorito ({genero_favorito}), te recomiendo la siguiente película: {pelicula_recomendada}")

# Función para añadir una tarea a la lista de tareas
def añadir_tarea(tarea):
    # Abrimos el archivo tareas.txt en modo lectura para cargar las tareas
    with open('tareas.txt', 'r') as archivo:
        tareas = archivo.readlines()  # Leemos las tareas existentes
    
    # Limpiamos las líneas leídas para eliminar saltos de línea
    tareas = [t.strip() for t in tareas]
    
    # Añadimos la nueva tarea al final de la lista
    tareas.append(tarea)
    
    # Guardamos la lista actualizada en el archivo
    with open('tareas.txt', 'w') as archivo:
        for t in tareas:
            archivo.write(t + '\n')
    
    # Retornamos la lista de tareas actualizada
    return tareas

# Función para gestionar la lista de tareas e imprimirlas
def gestionar_tareas(tareas):
    print("Tareas pendientes de realizar:\n")
    
    # Recorremos la lista de tareas e imprimimos cada una con su índice
    for idx, tarea in enumerate(tareas, 1):
        print(f"{idx}. {tarea}")
    
    # Imprimimos el número total de tareas pendientes
    print(f"\nHay {len(tareas)} tareas pendientes de realizar.")

# Ejecución del programa
if __name__ == "__main__":
    # Llamamos a la función añadir_tarea con una nueva tarea
    nueva_tarea = "Pagar la factura del internet"
    tareas = añadir_tarea(nueva_tarea)
    
    # Gestionamos e imprimimos la lista de tareas

    gestionar_tareas(tareas)


    # Función para mover el ascensor
def mover_ascensor(piso_actual, piso_deseado):
    # Bucle while que se ejecuta mientras el piso actual no es igual al deseado
    while piso_actual != piso_deseado:
        if piso_actual < piso_deseado:
            # Si el piso actual es menor, el ascensor sube
            print(f"Subiendo al piso {piso_deseado}. Piso actual: {piso_actual}")
            piso_actual += 1  # Incrementamos el piso actual
        else:
            # Si el piso actual es mayor, el ascensor baja
            print(f"Bajando al piso {piso_deseado}. Piso actual: {piso_actual}")
            piso_actual -= 1  # Decrementamos el piso actual
    
    # Mensaje indicando que se ha llegado al piso deseado
    print(f"Piso {piso_deseado} alcanzado.")

# Ejecución del programa
if __name__ == "__main__":
    piso_actual = 2  # Piso inicial
    piso_deseado = 6  # Piso al que se desea ir
    mover_ascensor(piso_actual, piso_deseado)  # Invocamos la función


#Scope y Namespace 

# Definir la variable global de los recursos del ecosistema
recursos_ecosistema = {
    "agua": 1000,
    "alimento": 800
}

# Función para que un animal interactúe con los recursos
def animal_interactua(tipo_animal, alimento_consumido, agua_consumida=None):
    global recursos_ecosistema

    # Verificar si es un herbívoro
    if tipo_animal == "herbívoro":
        # Comprobar si hay recursos suficientes para el consumo
        if recursos_ecosistema["agua"] >= agua_consumida and recursos_ecosistema["alimento"] >= alimento_consumido:
            # Consumir los recursos
            recursos_ecosistema["agua"] -= agua_consumida
            recursos_ecosistema["alimento"] -= alimento_consumido
            print(f"Un herbívoro ha consumido {agua_consumida} de agua y {alimento_consumido} de alimento.")
        else:
            print("Recursos insuficientes en el ecosistema.")
            return
    # Verificar si es un carnívoro
    elif tipo_animal == "carnívoro":
        # Comprobar si hay recursos suficientes de alimento
        if recursos_ecosistema["alimento"] >= alimento_consumido:
            # Consumir el alimento
            recursos_ecosistema["alimento"] -= alimento_consumido
            print(f"Un carnívoro ha consumido {alimento_consumido} de alimento.")
        else:
            print("Recursos insuficientes en el ecosistema.")
            return

    # Mostrar el estado actual del ecosistema después de la interacción
    print(f"Estado actual del ecosistema: {recursos_ecosistema}")

# Función para simular un evento de lluvia
def lluvia(cantidad_agua):
    global recursos_ecosistema
    recursos_ecosistema["agua"] += cantidad_agua
    print(f"¡Ha llovido! Se añadieron {cantidad_agua} unidades de agua al ecosistema.")

# Inicio del programa
print(f"Inicio del día en el ecosistema: {recursos_ecosistema}")

# Interacción de un herbívoro
animal_interactua("herbívoro", 100, 200)

# Interacción de un carnívoro
animal_interactua("carnívoro", 50)

# Evento de lluvia
lluvia(200)

# Fin del día
print(f"Fin del día en el ecosistema: {recursos_ecosistema}")
    

def formato_notificacion(func):
    """
    Decorator que agrega formato de notificación a las funciones que envían notificaciones.
 
    Este decorador imprime un encabezado y pie de página alrededor de la salida de la función decorada,
    indicando el inicio y fin de un evento en una plataforma específica.
 
    Args:
        func (Callable): La función a decorar, que debe aceptar al menos un argumento 'plataforma'.
 
    Returns:
        Callable: La función envuelta con la funcionalidad de formato de notificación.
    """
    def wrapper(self, plataforma):
        print(f"***** NUEVO EVENTO en {plataforma} *****")
        func(self, plataforma)
        print(f"***** FIN DEL EVENTO en {plataforma} *****\n")
    return wrapper
 
class NotificadorRedSocial:
    """
    Clase para enviar notificaciones de eventos a diferentes plataformas de redes sociales.
    """
 
    def __init__(self):
        """
        Inicializa la clase NotificadorRedSocial con el evento a notificar.
        """
        self.evento = "Lanzamiento de un nuevo libro"
    
    @formato_notificacion
    def notificar_evento(self, plataforma):
        """
        Envía una notificación del evento a la plataforma especificada.
 
        Args:
            plataforma (str): La plataforma de redes sociales a la que se enviará la notificación.
                Las plataformas soportadas son Twitter, Instagram y Facebook.
        """
        if plataforma == "Twitter":
            print(f"Tweet: {self.evento}")
        elif plataforma == "Instagram":
            print(f"Instagram Story: {self.evento}")
        elif plataforma == "Facebook":
            print(f"Post en Facebook: {self.evento}")
        else:
            print("Plataforma no soportada")
 
 
# Simulación de envío de notificaciones
notificador = NotificadorRedSocial()
plataformas = ["Twitter", "Instagram", "Facebook", "LinkedIn"]
for plataforma in plataformas:
    notificador.notificar_evento(plataforma)    


class SimuladorPrestamo:
    def __init__(self, detalles_prestamo, años=30, precio_vivienda=300000):
        self.tasa_mensual = (detalles_prestamo.imag / 12) / 100
        self.numero_pagos = años * 12
        self.entrada = detalles_prestamo.real
        self.prestamo = precio_vivienda - self.entrada
        self.cuota_mensual = 0
    
    def calcular_pago_total(self):
        if self.tasa_mensual > 0:
            self.cuota_mensual = self.prestamo * (self.tasa_mensual * (1 + self.tasa_mensual) ** self.numero_pagos) / ((1 + self.tasa_mensual) ** self.numero_pagos - 1)
        else:
            self.cuota_mensual = self.prestamo / self.numero_pagos
    
    def mostrar_resultados(self):
        print("----- Simulación Hipoteca -----")
        print(f"Para una vivienda de {self.prestamo + self.entrada} euros, aportando una entrada de {self.entrada} euros y con una tasa de interés del {self.tasa_mensual * 12 * 100}% anual durante {self.numero_pagos // 12} años:")
        print(f"Cuota mensual a pagar: {self.cuota_mensual} euros")
        print("----- Fin de la Simulación -----")

# Ejemplo de uso
detalles_prestamo = complex(50000, 2.5)  # Entrada de 50,000 euros, tasa de interés de 2.5%
simulador = SimuladorPrestamo(detalles_prestamo)
simulador.calcular_pago_total()
simulador.mostrar_resultados()    

