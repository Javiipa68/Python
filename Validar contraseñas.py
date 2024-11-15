# Contraseña a verificar
password =input ("Contraseña a verificar") 

# Validaciones individuales
longitud = len(password) >= 8  # Al menos 8 caracteres
caracter = "@" not in password and "#" not in password  # No contiene @ ni #
numero = any(char.isdigit() for char in password)  # Contiene al menos un número
espacios = " " not in password  # No contiene espacios

# Verificación general
es_segura = longitud and caracter and numero and espacios

# Resultados
print(f"Contraseña: {password}")
print(f"¿La contraseña cumple con los criterios establecidos? {es_segura}")