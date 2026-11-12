import menu
import Gestion_stock

def main():
    Gestion_stock.inicializar()
    opcion = menu.mostrar_menu()
    while opcion !=4:
        if opcion ==1:
            Gestion_stock.cargar_stock()
        elif opcion ==2:
            Gestion_stock.mostrar_stock()
        elif opcion ==3:
            cat = menu.categoria()
            if cat in Gestion_stock.cantidades():
                Gestion_stock.contar(Gestion_stock.cantidades[cat])
            else:
                print("ingrese una categroia valida")
        elif opcion ==4:
            print("termino")
    else:
        print("ingrese una opcion valida")

if __name__ == "__main__":
    main()
