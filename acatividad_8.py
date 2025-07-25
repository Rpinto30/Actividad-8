products = []

while True:
    print("-"*10+"Control de productos"+"-"*10)
    print("1) Agregar producto\n2) Modificar prodcuto existente\n3) Eliminar producto\n4)Ver productos\n5) Salir")
    op = input("Ingrese una opcion: ")
    match op:
        case '5':
            print("\nHasta pronto!")
            break
        case _: print("\nLo siento, intente de nuevo")