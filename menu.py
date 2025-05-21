#Importa el módulo estándar os, esto proporciona 
#funciones para interactuar con el sistema operativo.
import os
import opciones

from metodos_productos import ( ingresar_producto, 
	mostrar_productos, buscar_producto, eliminar_producto)




def limpiar_pantalla():
	# os.system: Ejecuta un comando del sistema operativo 
	# como si se escribiera en la terminal.
	# Si el nombre del sistema operativo es windows utiliza cls,
	# sino utiliza clear para refrescar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu ():
    print ("--- MENÚ DE OPCIONES ---")
    print ("1. Ingresar un nuevo producto")
    print ("2. Ver productos registrados")
    print ("3. Buscar producto por nombre")
    print ("4. Eliminar un producto")
    print ("5. Salir")
    
def ingresar_opcion ():
	#.strip() elimina los espacios en blanco al inicio y al final de una cadena
	opcion = input ( "Seleccionar una opción (1-5): " ).strip()
	return opcion

def ejecutar_opcion ( opcion , productos ) :
	match opcion:
		case opciones.INGRESAR_NUEVO_PRODUCTO:
			limpiar_pantalla()
			ingresar_producto(productos)
		case opciones.MOSTRAR_PRODUCTOS_POR_TERMINAL:
			limpiar_pantalla()
			mostrar_productos(productos)
		case opciones.BUSCAR_PRODUCTO_POR_NOMBRE:
			limpiar_pantalla()
			buscar_producto(productos)
		case opciones.ELIMINAR_PRODUCTO_POR_INDICE:
			limpiar_pantalla()
			eliminar_producto(productos)
		case opciones.FINALIZAR_PROGRAMA:
			return False  # salir del programa
		case _:
			print("ERROR: OPCIÓN FUERA DEL RANGO")

	input("Presione ENTER para continuar")
	return True  # continuar el bucle
    
