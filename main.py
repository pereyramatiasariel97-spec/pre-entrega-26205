#El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos)
productos = []

menu = True

while menu:
    print("\n--------------------------------------")
    print("\033[35mSistema de Gestion de Productos\033[m")
    print("--------------------------------------")
    print("\033[32m1) Agregar producto\033[m")
    print("\033[32m2) Mostrar Productos\033[m")
    print("\033[32m3) Buscar producto\033[m")
    print("\033[32m4) Eliminar Producto\033[m")
    print("\033[32m5) Salir del sistema\033[m")
    
    operacion = input('\n\033[35mQue operacion quiere realizar? :\033[m ').strip()
    
    # OPERACION 1 -------------------------------------------------------------------------------------------------
    if operacion == "1":
        print('\n\t Agregar Producto Nuevo')
     
        producto_valido = False
        while not producto_valido: #Ejecuta el bucle hasta que la condicion sea verdadera
            nombre = input("\nNombre del Producto: ").strip()
            if nombre != "":
                producto_valido = True
            else:
                print("\nERROR:\nEl nombre del producto NO puede estar vacio. Intente otra vez.\n")
        
        categoria_valida = False
        while not categoria_valida:
            categoria = input("Categoria del Producto: ").strip()
            if categoria != "":
                categoria_valida = True
            else:
                print("\nERROR:\nLa categoria del producto no puede estar vacia. Intente otra vez.\n")
        
        precio_valido = False
        while not precio_valido:
            precio_str = input("Precio del producto: ").strip()
            if precio_str.isdigit():
                precio = int(precio_str)
                precio_valido = True
            else:
                print("\nERROR:\nIngrese solo números enteros (mayor o igual a 0).\n")
        
        # Guardar el producto
        nuevo_producto = [nombre, categoria, precio]
        productos.append(nuevo_producto)
        print(f"\n¡Éxito! El producto '{nombre}' fue registrado correctamente.")
        
    # OPERACION 2 -------------------------------------------------------------------------------------------------
    elif operacion == "2":
        print("\n--- LISTA DE PRODUCTOS REGISTRADOS ---")
            
            # Verificar si la lista está vacía con un condicional
        if len(productos) == 0:
            print("No hay productos registrados en el sistema.")
        else:
            # Recorrer
            posicion = 1
            for prod in productos:
                print(f"{posicion}ID. Producto: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")
                posicion += 1
    
    
    # OPERACION 3 -------------------------------------------------------------------------------------------------
    
    elif operacion == "3":
        print("\n--- BUSCAR PRODUCTOS ---")

        if len(productos) == 0:
            print("\nEl sistema no contiene productos registrados")
        else:
            busqueda_valida = False
            while not busqueda_valida:
                busqueda = input("Ingrese el nombre del producto a buscar: ").strip()
                if busqueda != "":
                    busqueda_valida = True
                else:
                    print("Error: El nombre no puede estar vacío. Intente nuevamente.")
    
            encontrado = False
            posicion = 1
            for prod in productos:
                if busqueda.lower() in prod[0].lower():
                    print(f"[{posicion}ID] Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")
                    encontrado = True
                posicion += 1
        
            if not encontrado:
                print(f"No se encontro el producto: '{busqueda}'")
        
    # OPERACION 4 -------------------------------------------------------------------------------------------------
    
    elif operacion == "4":
        print("---ELIMINAR PRODUCTO")
        
        if len(productos) == 0:
            print("\nEl sistema no contiene productos registrados")
        else:
            print('Productos disponibles: ')
            posicion = 1
            for prod in productos:
                print(f"{posicion}ID. Producto: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")
                posicion += 1    
    
            eliminar_valido = False
            while not eliminar_valido:
                seleccion = input("\n Ingrese el ID. del producto que decea eliminar: ").strip()
                
                if seleccion.isdigit():
                    indice = int(seleccion)
                    
                    if indice >= 1 and indice <= len(productos):
                        eliminado = productos.pop(indice - 1)
                        print(f"\n El producto '{eliminado[0]}' se elimino correctamente.")
                        eliminar_valido = True
                    else:
                        print(f"Error: El numero debe de estar entre 1 y {len(productos)}")
                else:
                    print("Error: Debe de ingresar un numero entero valido.")            
    
            
    # OPERACION 5 -------------------------------------------------------------------------------------------------
    elif operacion == "5":
        print("\n\033[35mSaliendo del sistema de gestión. ¡Hasta luego!\033[0m")
        menu = False
    
    else:
        print("\nOperacion no valida")