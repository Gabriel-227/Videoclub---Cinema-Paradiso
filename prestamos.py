# MÓDULO: prestamos.py (Responsable: Gabriel)

from datetime import date, timedelta

#Impotar funcion de validacion 
from validaciones import validar_numero

#Importar listas Globales
from peliculas import peliculas
from socios import socios

#Lista Global vacia de prestamos 

prestamos = []


#funciones Buscar y mostrar

def buscar_prestamos_id(id_buscar):
    """Busca un préstamo en la lista local por su ID y lo devuelve. Si no existe, devuelve None."""
    for prestamo in prestamos:
        if prestamo['id'] == id_buscar:
            return prestamo
    return None


def mostrar_prestamo(prestamo):
    """Imprime en pantalla un prestamo individual"""
    fecha_prestamo = prestamo['fecha_prestamo'].strftime('%d/%m/%y')
    fecha_pactada = prestamo['fecha_devolucion_pactada'].strftime('%d/%m/%y')
    
    # Validamos si la fecha real está vacía (None) o si ya tiene una fecha guardada
    if prestamo['fecha_devolucion_real'] != None:
        fecha_real = prestamo['fecha_devolucion_real'].strftime('%d/%m/%Y')
    else:
        fecha_real = 'No se ha devuelto todavia'
        
    print('-' * 50)
    print(f'ID Operación: {prestamo['id']} | Estado: {prestamo['estado'].upper()}')
    print(f'Pelicula ID: {prestamo['id_pelicula']} | Socio ID: {prestamo['id_socio']}')
    print(f'Prestado el dia: {fecha_prestamo} | Entrega pactada: {fecha_pactada}')
    print(f'Fecha de devulición: {fecha_real}')
    print('-' * 50)
    
# ALTA - REGISTRAR PRÉSTAMO NUEVO

def registrar_prestamo():
    print('\n=== REGISTRAR UN PRÉSTAMO NUEVO===')
    
    #Validar si el socio existe en socios.py
    id_socio = validar_numero('Ingrese el número de ID del Socio: ')
    socio_existe = False
    for socio in socios:
        if socio['id'] == id_socio:
            socio_existe = True
            break
        
    if socio_existe == False:
        print('El socio no esta registrado en el sistema.')
        return
    
    #Validar si la pelicula existe en peliculas.py
    id_pelicula = validar_numero('Ingrese el ID de la Película')
    pelicula_encontrada = None
    for pelicula in peliculas:
        if pelicula['id'] == id_pelicula:
            pelicula_encontrada = pelicula
            break
    
    if pelicula_encontrada == None:
        print('La película no existe en la colección.')
        return
    
    #Validar la regla de negocio: ¿Hay stock disponible?
    if pelicula_encontrada['estado'] !='disponible':
        print(f'La película no está disponible (Estado actual: {pelicula_encontrada['estado']}).')
        
    #Procesamiento automático de fechas
    fecha_hoy = date.today()
    fecha_pactada = fecha_hoy + timedelta(days=3)
    
    #Generar ID autoincremental unico para el préstamo
    if len(prestamos) == 0:
        nuevo_id = 1
    else:
        nuevo_id = prestamos[-1]['id'] + 1
        
    #Diccionario del nuevo préstamo 
    nuevo_prestamo = {
        'id': nuevo_id,
        'id_pelicula': id_pelicula,
        'id_socio': id_socio,
        'fecha_prestamo': fecha_hoy,
        'fecha-devolicoion-pactada': fecha_pactada,
        'fecha-devolucion-real': None,
        'estado': 'activo'
    }
    
    #Guardar en la lista y cambiar el estado de la pelicula
    prestamos.append(nuevo_prestamo)
    pelicula_encontrada['estado'] = 'prestada'
    
    print(f'¡Prestamo N° {nuevo_id} fue registrado con éxito!')
    
#VER PRÉSTAMOS ACTIVOS / BUSCAR

def prestamos_activos():
    print('\n=== LISTADO DE PRESTAMOS ACTIVOS ===')
    hay_prestamos_activos = False
    
    for prestamo in prestamos:
        if prestamo['estado'] == 'activo':
            mostrar_prestamo(prestamo)
            prestamos_activos = True
            
    if prestamos_activos == False:
        print('No hay prestamos activos registrados en este momento.')
        
def buscar_prestamo_por_socio():
    print('\n=== BUSCAR PRESTAMOS DE UN SOCIO ===')
    id_socio_buscar = validar_numero('Ingrese el número ID del socio: ')
    encontrado_uno = False
    
    for prestamo in prestamos:
        if prestamo['id_socio'] == id_socio_buscar:
            mostrar_prestamo(prestamo)
            encontrado_uno = True
    
    if encontrado_uno == False:
        print('No se encontraron registros de préstamos para el socio ingresado')
        
       
#Registrar Devolución 

def registrar_devolucion():
    print('\n=== REGISTRAR UNA DEVOLUCION ===')
    
    #Pedir el ID de la operación - Buscar el préstamo
    id_operacion = validar_numero('Ingrese el número de operación del préstamo: ')
    prestamo = buscar_prestamos_id(id_operacion)
    
    #Validar que el préstamo exista
    if prestamo == None:
        print('Error: no se encontró ninguna operación con ese ID.')
        return

    if prestamo['estado'] != 'activo':
        print('Esta operacion ya se encuntra cerrada la pelicula fue devuelta.')
        return
    
    #Procesar la devolución 
    prestamo['fecha_devolucion_real'] = date.today()
    prestamo['estado'] = 'devuelto'
    
    #Cambiar el estado de la película
    for pelicula in peliculas:
        if pelicula['id'] == prestamo['id_pelicula']:
            pelicula['estado'] = 'disponible'
            break
    print(f'¡Devolución procesada con éxito! Operación N° {id_operacion} cerrada.')
    print(f'La pelicula ID: {prestamo['id_pelicula']} vuelve a estar DISPONIBLE')