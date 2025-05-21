# Pre_Entrega
# Nombre: Jose Miguel 
# Apellido: Paz Portilla

#De metodos_productos.py importa los metodos: 
#ingresar_producto, mostrar_productos, buscar_producto, eliminar_producto.
from metodos_productos import ( ingresar_producto , 
	mostrar_productos , buscar_producto , eliminar_producto )

#De menu.py importa los metodos: 
#limpiar_pantalla, mostrar_menu, ejecutar_opcion, ingresar_opcion.
from menu import ( limpiar_pantalla , mostrar_menu , 
	ejecutar_opcion , ingresar_opcion )
    
#Funcion principal
def main () :

	productos = [] 
	volver_al_menu = True
	
	while volver_al_menu == True : 
		limpiar_pantalla () 
		mostrar_menu () 
		opcion = ingresar_opcion ()
		volver_al_menu = ejecutar_opcion ( opcion , productos ) 
	
	limpiar_pantalla ()
	print("\n\n\t\t¡PROGRAMA FINALIZADO!\n\n")
		

if __name__ == "__main__":
    main()
    
