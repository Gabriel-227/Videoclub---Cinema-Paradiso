from validaciones import validar_texto, validar_numero, validar_estado

#listas globales
peliculas = [
    {
        "id": 1,
        "titulo": "Matrix",
        "director": "Wachowski",
        "anio_estreno": 2000,
        "pais_de_origen": "USA",
        "genero": "Accion",
        "duracion": 136,
        "formato": "DVD",
        "estado": "disponible"
    },

    {
        "id": 2,
        "titulo": "Shrek",
        "director": "Dreamworks",
        "anio_estreno": 2001,
        "pais_de_origen": "USA",
        "genero": "Animacion",
        "duracion": 90,
        "formato": "Blu-ray",
        "estado": "prestada"
    }
]





#funcion con print para mostrar peliculas
def mostrar_pelicula(pelicula):

    print("----------------------")
    print(f'ID: {pelicula["id"]}')
    print(f'Titulo: {pelicula["titulo"]}')
    print(f'Director: {pelicula["director"]}')
    print(f'Año: {pelicula["anio_estreno"]}')
    print(f'Genero: {pelicula["genero"]}')
    print(f'Estado: {pelicula["estado"]}')

#CREATE PELICULAS
def cargar_pelicula():

    id_pelicula = generar_id_pelicula()

    titulo = validar_texto("Ingrese el nombre de la película: ") 
    director = validar_texto("Ingrese el nombre del director de la película: ")
    anio_estreno = validar_numero("Ingrese el año de estreno: ")
    pais_de_origen = validar_texto("Ingrese el país de origen: ")
    genero = validar_texto("Ingrese el género de la película: ")
    duracion = validar_numero("ingrese la duracion: ")
    formato = validar_texto("Ingrese el formato de la película: ")
    estado = validar_estado("Ingrese el estado -  (disponible, prestada, en proyección, dada de baja): ")

    pelicula = {
        "id": id_pelicula,
        "titulo": titulo,
        "director" : director,
        "anio_estreno" : anio_estreno,
        "pais_de_origen" : pais_de_origen,
        "genero" : genero,
        "duracion" : duracion,
        "formato" : formato,
        "estado" : estado
    }

    peliculas.append(pelicula)
    print("Pelicula cargada con exito...")

#Listar todas las peliculas
def ver_todas_las_peliculas():
    print("\n=== LISTADO DE PELÍCULAS ===")
    for pelicula in peliculas:
        mostrar_pelicula(pelicula)
    input("\nPresione ENTER para continuar...")

#---FUNCIONES DE BUSQUEDA---

#funcion para filtrar pelicula por genero
def filtrar_genero():
    encontrada = False

    genero = validar_texto("Ingrese genero: ").lower()

    for pelicula in peliculas:
        if( genero == pelicula["genero"].lower()):
            mostrar_pelicula(pelicula)
            encontrada = True
    if not encontrada:
        print("no se encontraron resultados...")

#funcion para filtrar por director
def filtrar_director():
    encontrada = False

    director = validar_texto("Ingrese el director: ").lower()

    for pelicula in peliculas:
        if(director == pelicula["director"].lower()):
            mostrar_pelicula(pelicula)
            encontrada = True
    if not encontrada:
        print("no se encontraron resultados...")

#funcion para filtrar por año
def filtrar_decada():
    encontrada = False
    decada = validar_numero("Ingrese década (ej: 2000): ")

    for pelicula in peliculas:
        if str(decada)[:3] == str(pelicula["anio_estreno"])[:3]:
            mostrar_pelicula(pelicula)
            encontrada = True

    if not encontrada:
        print("no se encontraron resultados...")

#funcion para filtrar por estado -disponible, prestada, en proyección, dada de baja-
def filtrar_estado():
    encontrada = False
    estado = validar_estado("Ingrese el estado: ")

    for pelicula in peliculas:
        if(estado == pelicula["estado"].lower()):
            mostrar_pelicula(pelicula)
            encontrada = True

    if not encontrada:
        print("no se encontraron resultados...")
        
        
#buscar pelicula por titulo, director o año
def buscar_pelicula():
    dato_pelicula = input("Ingrese titulo, director o año de la pelicula: ").lower()

    for pelicula in peliculas:

        if(dato_pelicula == pelicula["titulo"].lower() or dato_pelicula == pelicula["director"].lower() 
           or dato_pelicula == str(pelicula["anio_estreno"])):
            print("Pelicula encontrada con exito!")
            mostrar_pelicula(pelicula)
            break
    else:
        print("pelicula no encontrada")


# FUNCIONES AUXILIARES

def buscar_pelicula_por_id(id_busqueda):

    for pelicula in peliculas:

        if pelicula["id"] == id_busqueda:
            return pelicula

    return None

def generar_id_pelicula():

    if len(peliculas) == 0:
        return 1

    ultimo_id = peliculas[-1]["id"]

    return ultimo_id + 1


def solicitar_pelicula_por_id():

    id_busqueda = validar_numero(
        "Ingrese id de la pelicula: "
    )

    pelicula = buscar_pelicula_por_id(id_busqueda)

    return pelicula



def pelicula_esta_dada_de_baja(pelicula):

    return pelicula["estado"] == "dada de baja"


#editar estado de una pelicula
def editar_estado():
    ver_todas_las_peliculas()

    pelicula = solicitar_pelicula_por_id()
    
    if pelicula:

            print("Película encontrada")
            mostrar_pelicula(pelicula)

            nuevo_estado = validar_estado("Ingrese nuevo estado -disponible, prestada, en proyección-: ")

            pelicula["estado"] = nuevo_estado

            print("Estado actualizado correctamente")

    else:
        print("Película no encontrada")


def dar_de_baja_pelicula():

    ver_todas_las_peliculas()
 
    pelicula = solicitar_pelicula_por_id()

    if pelicula:

        print("Película encontrada")
        mostrar_pelicula(pelicula)

        if pelicula_esta_dada_de_baja(pelicula):
            print("La pelicula ya está dada de baja")
            return

        opcion_estado = input(
            "Ingrese 1 para dar de baja o 2 para cancelar la operación: "
        )

        match opcion_estado:

            case "1":
                pelicula["estado"] = "dada de baja"
                print("Estado actualizado correctamente")

            case "2":
                print("Cancelando operación...")

            case _:
                print("Opción inválida")

    else:
        print("Película no encontrada") 

def menu_peliculas():

    while True:

        print("\n=== COLECCIÓN DE PELÍCULAS ===")
        print("1. Cargar película")
        print("2. Ver todas las películas")
        print("3. Buscar película")
        print("4. Filtrar por género")
        print("5. Filtrar por director")
        print("6. Filtrar por década")
        print("7. Filtrar por estado")
        print("8. Modificar película")
        print("9. Dar de baja película")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                cargar_pelicula()

            case "2":
                ver_todas_las_peliculas()

            case "3":
                buscar_pelicula()

            case "4":
                filtrar_genero()

            case "5":
                filtrar_director()

            case "6":
                filtrar_decada()

            case "7":
                filtrar_estado()

            case "8":
                editar_estado()

            case "9":
                dar_de_baja_pelicula()

            case "0":
                break

            case _:
                print("Opción inválida")