def mostrar_menu():
    print("Bienvendido al menu")
    print("1. cargar stock")
    print("2. mostrar total del stock")
    print("3. mostrar cantidad de productos")
    print("4. salir")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def categoria():
    cat = input("Ingrese el producto: ")
    return cat