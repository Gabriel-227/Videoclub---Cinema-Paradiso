

#validar que el usuario ingrese un numero 
def validar_numero(mensaje):

    while True:

        dato = input(mensaje)

        if dato.isdigit():
            return int(dato)

        print("Error. Ingrese solo números.")

#validar que el usuario no ingrese un campo vacio y tampoco numeros
def validar_texto(mensaje):

    while True:

        texto = input(mensaje).strip()

        if texto == "":
            print("Error. El campo no puede estar vacío.")

        elif texto.isdigit():
            print("Error. No puede ingresar números.")

        else:
            return texto

 #validar que el usuario ingrese un estado valido       
def validar_estado(mensaje):

    estados_validos = [
        "disponible",
        "prestada",
        "en proyección",
        "dada de baja"
    ]

    while True:

        estado = input(mensaje).lower()

        if estado in estados_validos:
            return estado

        print("Estado inválido.")


def validar_email():

    while True:

        email = input("Ingrese email: ")

        if "@" in email:
            return email

        print("Email inválido")