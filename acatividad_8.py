products = []

while True:
    print("-"*10+"Control de productos"+"-"*10)
    print("1) Agregar producto\n2) Modificar prodcuto existente\n3) Eliminar producto\n4)Ver productos\n5) Salir")
    op = input("Ingrese una opcion: ")
    match op:
        case '1':
            print("-" * 10 + "Agregar producto" + "-" * 10)
            prod = input("Ingrese su nuevo producto: ")
            products.append(prod)
            print(f"\nProducto {prod} agreagado correctamente")
        case '2':
            if len(products) > 0:
                print("-" * 10 + "Modificar producto" + "-" * 10)
                while True:
                    print("Productos: [", end='')
                    for i in range(len(products)):
                        if i == len(products)-1: print(f"{products[i]}: {i}]\n")
                        else: print(f"{products[i]}: {i}", end=', ')
                    prod = int(input("Ingrese el indice del producto que quiere modificar: "))
                    if prod < len(products): break
                    else: print("\nLo siento, producto no encontrado, intente de nuevo")

                new_prod = input("Ingrese nuevo producto: ")
                products[prod] = new_prod
                print("\nProducto agregado!")

            else: print("\nLo siento, no hay productos registrados")
        case '3':
            print("-" * 10 + "Eliminar producto" + "-" * 10)
            print(f"Productos: {products}")
            prod = input("Ingrese producto que quiera eliminar: ")

            if prod in products:
                products.remove(prod)
                print("\nProducto eliminado")
            else: print("\nLo siento, producto no existente")
        case '4':
            for i in range(len(products)):
                if i == len(products) - 1: print(f"{products[i]}: {i}]\n")
                else: print(f"{products[i]}: {i}", end=', ')
        case '5':
            print("\nHasta pronto!")
            break
        case _: print("\nLo siento, intente de nuevo")