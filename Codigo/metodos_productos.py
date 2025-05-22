# Se definen las funciones que sirven para manipular los productos

NOMBRE = 0 # producto[0]: NOMBRE, producto[1]: CATEGORIA, producto[2]: PRECIO

"""
Genera un producto a partir del nombre, categoria y precio ingresados por teclado
Ingresa el producto a la lista de productos
Parámetros:
productos(list): lista de productos
Retorna:-
""" 
def ingresar_producto ( productos ):
	print ("--- NUEVO PRODUCTO ---")
	while True:
		nombre = input("Ingrese el nombre del producto: ").strip()
		if nombre != "":
			break
		print("ERROR: NOMBRE DE PRODUCTO ESTA VACIA")

	while True:
		categoria = input("Ingrese la categoría del producto: ").strip()
		if categoria != "":
			break
		print("ERROR: NOMBRE DE LA CATEGORIA ESTA VACIA")

	while True:
		#Bloque para atrape el error de conversion de cadena a entero
		try:
			precio = int(input("Ingrese el precio del producto (sin centavos): "))
			if precio < 0:
				print("ERROR: EL PRECIO INGRESADO ES NEGATIVO")
				continue
			break
		except ValueError:
			print("ERROR: EL PRECIO NO ES UN VALOR ENTERO")

	producto = [nombre, categoria, precio]
	
	# Insertar producto en la lista de productos ordenado por nombre
	producto_fue_insertado = False
	for indice in range(len(productos)):#i va de 0 hasta len(productos)-1
		# compara ignorando mayúsculas/minúsculas
		if nombre.lower() < productos[indice][NOMBRE].lower():  
			productos.insert (indice, producto)
			producto_fue_insertado = True
			break
	# Si no fue ingresado producto en la lista de productos,
	# debido a que al compararlo no hubo otro nombre menor alfabeticamente,
	# Simplemente de agrega el producto al final de la lista productos 
	if not producto_fue_insertado:
		productos.append(producto)

"""
Muestra por terminal la lista de productos
con el formato: nombre|categoria|precio
Parámetros:
productos(list): lista de productos
Retorna:-
""" 
def mostrar_productos ( productos ) :
    if len (productos) == 0:
        print ("No hay productos registrados.")
        return

    print ("--- LISTA DE PRODUCTOS REGISTRADOS ---")
    # Empieza a enumerar desde 1 el i, y va deserializando producto de la lista_productos
    for indice, producto in enumerate( productos , start = 1 ):
        nombre, categoria, precio = producto
        print(f"{indice}. NOMBRE: {nombre} | CATEGORÍA: {categoria} | PRECIO: ${precio}")

"""
Busca en la lista de productos los productos que coinciden con el nombre de productos
ingresado por teclado. Luegos los muestra por terminal en caso de encontrarlo
Parámetros:
productos(list): lista de productos
Retorna:-
""" 
def buscar_producto ( productos ):
	print ("--- BUSQUEDA DE PRODUCTO ---")
	# Borra espacios de los bordes y lo paso a minusculas
	nombre = input("Ingresar el nombre del producto a buscar: ").strip().lower()
	if nombre == "":
		print("ERROR: NOMBRE DE PRODUCTO A BUSCAR ESTA VACIA")
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
		print(" NOMBRE DE PRODUCTO NO ESTA EN EL INVENTARIO")

"""
Elimina un producto de la lista de productos a partir de la posicion mostrada por terminal
Parámetros:
productos(list): lista de productos
Retorna:-
""" 
def eliminar_producto ( productos ):
	print ("--- ELIMINACION DE PRODUCTO ---")
	if len(productos) == 0:
		print ("INVENTARIO ESTÁ VACIO")
		return

	mostrar_productos(productos)  
	while True:
		try:
			indice = int(input("Ingrese el número del producto a eliminar: "))
			if 1 <= indice and indice <= len(productos):
				#Se resta 1 porque la posicion en la lista empieza en 0 
				eliminado = productos.pop ( indice - 1 ) 
				break
			else:
				print("ERROR: OPCION DE LA LISTA DE PRODUCTOS FUERA DE RANGO")
		except ValueError:
			print("ERROR: INGRESO DE UN NUMERO NO ENTERO")

