# ==================================
# SISTEMA DE CLIENTES Y PRODUCTOS
# ==================================

# Listas
clientes = []
productos = []

# Variable del menú
opcion = 0

# ==================================
# MENÚ PRINCIPAL
# ==================================

while opcion != 9:

    print("\n===== MENÚ =====")
    print("1. Registrar cliente")
    print("2. Registrar producto")
    print("3. Listar clientes")
    print("4. Listar productos")
    print("5. Buscar cliente")
    print("6. Buscar producto")
    print("7. Eliminar cliente")
    print("8. Eliminar producto")
    print("9. Salir")

    opcion = int(input("Seleccione una opción: "))

    # ==================================
    # REGISTRAR CLIENTE
    # ==================================

    if opcion == 1:

        id_cliente = input("Ingrese ID: ")

        repetido = False

        for cliente in clientes:
            if cliente["id"] == id_cliente:
                repetido = True

        if repetido == True:
            print("Cliente ya existe")

        else:
            nombre = input("Ingrese nombre: ")
            telefono = input("Ingrese teléfono: ")

            cliente = {
                "id": id_cliente,
                "nombre": nombre,
                "telefono": telefono
            }

            clientes.append(cliente)

            print("Cliente registrado")

    # ==================================
    # REGISTRAR PRODUCTO
    # ==================================

    elif opcion == 2:

        codigo = input("Ingrese código: ")

        repetido = False

        for producto in productos:
            if producto["codigo"] == codigo:
                repetido = True

        if repetido == True:
            print("Producto ya existe")

        else:
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            valor = float(input("Ingrese valor: "))

            producto = {
                "codigo": codigo,
                "nombre": nombre,
                "cantidad": cantidad,
                "valor": valor
            }

            productos.append(producto)

            print("Producto registrado")

    # ==================================
    # LISTAR CLIENTES
    # ==================================

    elif opcion == 3:

        print("\n===== CLIENTES =====")

        if len(clientes) == 0:
            print("No hay clientes")

        else:
            for cliente in clientes:
                print(cliente)

    # ==================================
    # LISTAR PRODUCTOS
    # ==================================

    elif opcion == 4:

        print("\n===== PRODUCTOS =====")

        if len(productos) == 0:
            print("No hay productos")

        else:
            for producto in productos:
                print(producto)

    # ==================================
    # BUSCAR CLIENTE
    # ==================================

    elif opcion == 5:

        buscar = input("Ingrese ID del cliente: ")

        encontrado = False

        for cliente in clientes:
            if cliente["id"] == buscar:
                print(cliente)
                encontrado = True

        if encontrado == False:
            print("Cliente no encontrado")

    # ==================================
    # BUSCAR PRODUCTO
    # ==================================

    elif opcion == 6:

        buscar = input("Ingrese código del producto: ")

        encontrado = False

        for producto in productos:
            if producto["codigo"] == buscar:
                print(producto)
                encontrado = True

        if encontrado == False:
            print("Producto no encontrado")

    # ==================================
    # ELIMINAR CLIENTE
    # ==================================

    elif opcion == 7:

        eliminar = input("Ingrese ID del cliente: ")

        for cliente in clientes:
            if cliente["id"] == eliminar:
                clientes.remove(cliente)
                print("Cliente eliminado")

    # ==================================
    # ELIMINAR PRODUCTO
    # ==================================

    elif opcion == 8:

        eliminar = input("Ingrese código del producto: ")

        for producto in productos:
            if producto["codigo"] == eliminar:
                productos.remove(producto)
                print("Producto eliminado")

    # ==================================
    # SALIR
    # ==================================

    elif opcion == 9:

        print("Programa finalizado")

    else:
        print("Opción inválida")