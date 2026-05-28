from validaciones import validar_texto, validar_numero,validar_email
socios = [
    {
        "id": 1,
        "nombre_completo": "Micaela Calviño",
        "dni": 36154461,
        "apodo": "Miki",
        "telefono": 1143656,
        "email": "mica@correo.com",
        "fecha_alta": "21/05/2024",
        "estado": "al día",
        "generos_favoritos": "drama"
    },

    {
        "id": 2,
        "nombre_completo": "Juan Pérez",
        "dni": 40222333,
        "apodo": "Juani",
        "telefono": 116778899,
        "email": "juan@gmail.com",
        "fecha_alta": "10/01/2024",
        "estado": "atrasado",
        "generos_favoritos": "acción"
    }
]

def mostrar_socio(socio):

    print("----------------------")
    print(f'ID: {socio["id"]}')
    print(f'nombre_completo: {socio["nombre_completo"]}')
    print(f'dni: {socio["dni"]}')
    print(f'apodo: {socio["apodo"]}')
    print(f'telefono: {socio["telefono"]}')
    print(f'email: {socio["email"]}')
    print(f'Fecha de alta: {socio["fecha_alta"]}')
    print(f'Estado: {socio["estado"]}')
    print(f'Generos favoritos: {socio["generos_favoritos"]}')


# FUNCIONES AUXILIARES

def buscar_socio_por_id(id_busqueda):

    for socio in socios:

        if socio["id"] == id_busqueda:
            return socio

    return None

def generar_id_socio():

    if len(socios) == 0:
        return 1

    ultimo_id = socios[-1]["id"]

    return ultimo_id + 1


def solicitar_socio_por_id():

    id_busqueda = validar_numero(
        "Ingrese id del socio: "
    )

    socio = buscar_socio_por_id(id_busqueda)

    return socio




def validar_estado_socio():

    estados = [
        "al día",
        "atrasado",
        "dado de baja"
    ]

    while True:

        estado = input(
            "Ingrese estado al (día/atrasado/dado de baja): "
        ).lower()

        if estado in estados:
            return estado

        print("Estado inválido")


def cargar_socio():
    id_socio = generar_id_socio()

    nombre_completo = validar_texto("Ingrese su nombre completo: ") 
    dni = validar_numero("Ingrese su dni: ")
    apodo = validar_texto("Ingrese su apodo: ")
    telefono = validar_numero("Ingrese su número de telefono: ")
    email = validar_email()
    fecha_alta = input("Ingrese fecha de alta (dd/mm/aaaa): ")
    estado = validar_estado_socio()
    generos_favoritos = validar_texto("Ingrese su genero favorito: ")

    socio = {
        "id": id_socio,
        "nombre_completo": nombre_completo,
        "dni" : dni,
        "apodo" : apodo,
        "telefono" : telefono,
        "email" : email,
        "fecha_alta" : fecha_alta,
        "estado" : estado,
        "generos_favoritos" : generos_favoritos
    }

    socios.append(socio)
    print("Socio cargado con éxito...")


def ver_todos_los_socios():

    print("\n=== LISTADO DE SOCIOS ===")

    for socio in socios:
        mostrar_socio(socio)

    input("\nPresione ENTER para continuar...")

#filtrar por estado de su cuota (al día, atrasado, dado de baja).
def filtrar_socios_por_estado():

    encontrado = False

    estado = validar_estado_socio()

    for socio in socios:

        if socio["estado"] == estado:
            mostrar_socio(socio)
            encontrado = True

    if not encontrado:
        print("No se encontraron socios con ese estado")

#buscar socio por DNI, nombre o número de carnet.
def buscar_socio():
    dato_socio = input("Ingrese nombre, dni o numero de carnet: ").lower()

    for socio in socios:

        if(dato_socio == socio["nombre_completo"].lower() or dato_socio == str(socio["dni"])
           or dato_socio == str(socio["id"])):
            print("Socio encontrado con exito!")
            mostrar_socio(socio)
            break
    else:
        print("Socio no encontrado")


#actualizar datos de contacto o estado
def editar_socio():

    ver_todos_los_socios()

    socio = solicitar_socio_por_id()

    if socio:

        print("Socio encontrado")
        mostrar_socio(socio)

        nuevo_telefono = validar_numero(
            "Ingrese nuevo teléfono: "
        )

        nuevo_email = validar_email()

        nuevo_estado = validar_estado_socio()

        socio["telefono"] = nuevo_telefono
        socio["email"] = nuevo_email
        socio["estado"] = nuevo_estado

        print("Datos actualizados correctamente")

    else:
        print("Socio no encontrado")


#dar de baja socio
def dar_de_baja_socio():

    ver_todos_los_socios()

    socio = solicitar_socio_por_id()

    if socio:

        print("Socio encontrado")
        mostrar_socio(socio)

        if socio["estado"] == "dado de baja":
            print("El socio ya está dado de baja")
            return

        confirmacion = input(
            "¿Seguro que desea dar de baja al socio? (s/n): "
        ).lower()

        if confirmacion == "s":

            socio["estado"] = "dado de baja"

            print("Socio dado de baja correctamente")

        else:
            print("Operación cancelada")

    else:
        print("Socio no encontrado")



def menu_socios():

    while True:

        print("\n=== SOCIOS ===")
        print("1. Cargar socio")
        print("2. Listar socios")
        print("3. Buscar socio por estado (al día, atrasado, dado de baja).")
        print("4. Buscar socio")
        print("5. Editar socio")
        print("6. Dar de baja un socio")
        print("9. Volver")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                cargar_socio()

            case "2":
                ver_todos_los_socios()

            case "3":
                filtrar_socios_por_estado()

            case "4":
                buscar_socio()

            case "5":
                editar_socio()
            
            case "6":
                dar_de_baja_socio()

            case "9":
                break

            case _:
                print("Opción inválida")



"""
#codigo de matias

# Menú principal del sistema
lista_socios = []

def menu_principal():
    pass

# Función temporal para volver al menú principal
def volver():
    menu_principal()

# Crear un nuevo socio y guardarlo en la estructura de datos
def crear_socio(lista):
    
    print("Ingresa el Nombre y el Apellido")
    nombre_completo = input()

    print("Ingresa el DNI")
    dni = input()
    
    print("Ingresa apodo")
    apodo = input()

    print("Ingresa el número de teléfono")
    telefono = input()

    print("Ingresa el email")
    email = input()

    print("Ingresa Fecha de Alta")
    fecha_alta = input()

    print("Ingresa el Estado de la cuota")
    estado_cuota = input()

    print("Ingresa los géneros favoritos")
    generos_favoritos = input()

    id_calculado = len(lista) + 1
    socio = {"id" : id_calculado, 
         "nombre_completo": nombre_completo, 
         "dni": dni, 
         "apodo" : apodo, 
         "telefono" : telefono, 
         "email" : email,
         "fecha_alta" : fecha_alta, 
         "estado_cuota" : estado_cuota, 
         "generos_favoritos" : generos_favoritos}
    
    lista.append(socio)
    #pass

# Buscar socios por DNI, nombre o número de carnet
def buscar_socio():
    pass

# Editar información de un socio existente
def editar_socio():
    pass

# Eliminar o dar de baja un socio
def eliminar_socio():
    pass

# Módulo encargado de la gestión de socios
# Será utilizado por el sistema de préstamos
# para validar existencia y consultar datos
def socios():
    while True: 
    
       
1 - Crear socio
2 - Buscar socio
3 - Editar socio
4 - Eliminar socio
0 - Volver

Seleccione una opción:

    
        valor = int(input())

        if valor == 0:
            print("Has escogido volver al menú principal")
            #volver()
            break

        # Evaluar opción seleccionada por el usuario
        match valor:

            case 1:
                print("Has escogido crear un socio")
                crear_socio(lista_socios)
            case 2:
                print("Has escogido buscar un socio")
                buscar_socio()
            case 3:
                print("Has escogido editar un socio")
                editar_socio()
            case 4:
                print("Has escogido eliminar un socio")
                eliminar_socio()
            case _:
                print("Ingrese un número del 0 al 4") 

socios()
"""