# Función para crear el tablero
def crear_tablero(filas, columnas):
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    return tablero

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print("| " + " | ".join(fila) + " |")
    print("  " + "   ".join([str(i) for i in range(len(tablero[0]))]))  # Mostrar el índice de columnas

# Función para colocar la ficha en la columna seleccionada
def colocar_ficha(tablero, columna, ficha):
    for fila in reversed(tablero):
        if fila[columna] == ' ':
            fila[columna] = ficha
            return True
    return False

# Función para comprobar si hay un ganador
def comprobar_ganador(tablero, ficha):
    # Comprobar horizontal
    for fila in tablero:
        for col in range(len(fila) - 3):
            if fila[col] == fila[col+1] == fila[col+2] == fila[col+3] == ficha:
                return True
    
    # Comprobar vertical
    for col in range(len(tablero[0])):
        for fila in range(len(tablero) - 3):
            if tablero[fila][col] == tablero[fila+1][col] == tablero[fila+2][col] == tablero[fila+3][col] == ficha:
                return True
    
    # Comprobar diagonal positiva (\)
    for fila in range(len(tablero) - 3):
        for col in range(len(tablero[0]) - 3):
            if tablero[fila][col] == tablero[fila+1][col+1] == tablero[fila+2][col+2] == tablero[fila+3][col+3] == ficha:
                return True
    
    # Comprobar diagonal negativa (/)
    for fila in range(3, len(tablero)):
        for col in range(len(tablero[0]) - 3):
            if tablero[fila][col] == tablero[fila-1][col+1] == tablero[fila-2][col+2] == tablero[fila-3][col+3] == ficha:
                return True
    
    return False

# Función principal para ejecutar el juego
def jugar():
    filas, columnas = 6, 7
    tablero = crear_tablero(filas, columnas)
    mostrar_tablero(tablero)
    turno = 0
    fichas = ['X', 'O']
    
    while True:
        print(f"Turno del jugador {turno + 1} ({fichas[turno]})")
        
        # Validación de entrada del usuario
        while True:
            try:
                columna = input("Introduce una columna (0-6): ")
                # Verificar si la entrada es un número válido
                if columna.isdigit():
                    columna = int(columna)
                    if 0 <= columna < columnas:
                        break
                    else:
                        print("Por favor, introduce un número entre 0 y 6.")
                else:
                    print("Entrada no válida. Por favor, introduce un número.")
            except ValueError:
                print("Error de entrada. Inténtalo de nuevo.")

        if colocar_ficha(tablero, columna, fichas[turno]):
            mostrar_tablero(tablero)
            
            if comprobar_ganador(tablero, fichas[turno]):
                print(f"¡Jugador {turno + 1} ha ganado!")
                break
            elif all(tablero[0][col] != ' ' for col in range(columnas)):  # Comprobar empate
                print("¡Empate! No hay más movimientos posibles.")
                break
            
            turno = (turno + 1) % 2  # Cambiar de turno
        else:
            print("Movimiento no válido, inténtalo de nuevo.")

# Ejecutar el juego
if __name__ == "__main__":
    jugar()