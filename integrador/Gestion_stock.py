stock_productos = {
    "enlatados": [],
    "frutas": [],
    "congelados": [],
    "panaderia": []
}

stock_cantidades = {
    "enlatados": [],
    "frutas": [],
    "congelados": [],
    "panaderia": []
}

def inicializar():
    for cat in stock_productos:
        stock_productos[cat] = []
    for cat in stock_cantidades:
        stock_cantidades[cat] = []

def cargar_stock():
    cat = input("Ingrese la categoria: ")
    if cat in stock_productos:
        producto = input("Ingrese un tipo de producto: ")
        cantidad = input("Ingrese la cantidad: ")
        stock_productos[cat].append(producto)
        stock_cantidades[cat].append(cantidad)
        print("se cargo el producto")
    else:
        print("ingrese una cat valida")

def mostrar_stock():
    for cat in stock_productos:
        print(cat, ":")
        for i in range(len(stock_productos[cat])):
            print(stock_productos[cat][i], "y su cantidad es de: ", stock_cantidades[cat][i])

def contar(lista_productos):
    total = 0
    for lista_productos in total:
        producto = input("Ingrese una categoria: ")
        total = total + lista_productos
        print("la cantidad de productos que hay: "), len(stock_productos)
        print("la suma de las cantidades de los productos: "), total



    
            

        
    