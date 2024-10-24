#se muestra la cabecera del programa
def cabecera():
    a ="""
    ██╗  ██╗ █████╗ ███████╗██╗  ██╗ ██████╗ █████╗ ██╗      ██████╗
    ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗██║     ██╔════╝
    ███████║███████║███████╗███████║██║     ███████║██║     ██║     
    ██╔══██║██╔══██║╚════██║██╔══██║██║     ██╔══██║██║     ██║     
    ██║  ██║██║  ██║███████║██║  ██║╚██████╗██║  ██║███████╗╚██████╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝
                                        <Javi Ipa> 
    """

    print(a)
#Vamos a solicitar al usuario el mensaje para calcular su Hash

mensaje = input('Introduce un mensaje:')

#obtenemos el Hash del mensaje

hash_value = hash (mensaje)
#Mostramos en pantalla el Hash del mensaje

print('El Hash del mensaje es:', hash_value)
