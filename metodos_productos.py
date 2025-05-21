# Se definen las funciones que sirven para manipular los productos

NOMBRE = 0 # producto[0]: NOMBRE, producto[1]: CATEGORIA, producto[2]: PRECIO

def ingresar_producto ( productos ):
	print ("--- NUEVO PRODUCTO ---")
	while True:
		nombre = input("Ingrese el nombre del producto: ").strip()
		if nombre != "":
			break
		print("El nombre no puede estar vacío.")

	while True:
		categoria = input("Ingrese la categoría del producto: ").strip()
		if categoria != "":
			break
		print("La categoría no puede estar vacía.")

	while True:
		#Bloque para atrape el error de conversion de cadena a entero
		try:
			precio = int(input("Ingrese el precio del producto (sin centavos): "))
			if precio < 0:
				print("El precio no puede ser negativo.")
				continue
			break
		except ValueError:
			print("Entrada inválida. Ingrese un número entero.")

	producto = [nombre, categoria, precio]
	productos.append (producto)


def mostrar_productos ( productos ) :
    if len (productos) == 0:
        print ("No hay productos registrados.")
        return

    print ("--- LISTA DE PRODUCTOS REGISTRADOS ---")
    # Empieza a enumerar desde 1 el i, y va deserializando producto de la lista_productos
    for indice, producto in enumerate( productos , start = 1 ):
        nombre, categoria, precio = producto
        print(f"{indice}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")


def buscar_producto ( productos ):
	print ("--- BUSQUEDA DE PRODUCTO ---")
	# Borra espacios de los bordes y lo paso a minusculas
	nombre = input("Ingresar el nombre del producto a buscar: ").strip().lower()
	if nombre == "":
		print("El término de búsqueda no puede estar vacío.")
		return

	encontrados = []
	for producto in productos:
		if nombre in producto[NOMBRE].lower(): 
			encontrados.append(producto)

	if len(encontrados) != 0:
		for indice, encontrado in enumerate ( encontrados , start = 1 ) :
			nombre, categoria, precio = encontrado
			print(f"{indice}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
	else:
		print("No se encontraron productos con ese nombre.")


def eliminar_producto ( productos ):
	print ("--- ELIMINACION DE PRODUCTO ---")
	if len(productos) == 0:
		print ("No hay productos para eliminar.")
		return

	mostrar_productos(productos)  
	while True:
		try:
			indice = int(input("Ingrese el número del producto a eliminar: "))
			if 1 <= indice and indice <= len(productos):
				#Se resta uno porque la posicion en la lista empieza en 0 realmente
				eliminado = productos.pop ( indice - 1 ) 
				break
			else:
				print("Número inválido. Intente nuevamente.")
		except ValueError:
			print("Entrada inválida. Ingrese un número entero.")

