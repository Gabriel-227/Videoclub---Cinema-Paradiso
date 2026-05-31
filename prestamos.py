# MÓDULO: prestamos.py (Responsable: Gabriel)

from datetime import date, timedelta

#Impotar funcion de validacion 
from validaciones import validar_numero

#Importar listas Globales
from peliculas import peliculas
from socios import socios

#Lista Global vacia de prestamos 

prestamos = []


#funciones

def buscar_prestamos_id(id_buscar):
    """Busca un préstamo en la lista local por su ID y lo devuelve. Si no existe, devuelve None."""
    for prestamo in prestamos:
        if prestamo['id'] == id_buscar:
            return prestamo
    return None


def mostrar_prestamo(prestamo):
    """Imprime en pantalla un prestamo individual"""
    fecha_prestamo = prestamo['fecha_prestamo'].strftime('%d/%m/%y')s
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