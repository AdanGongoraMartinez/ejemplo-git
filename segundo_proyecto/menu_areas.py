import area_cuadrado

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Calcular área de un cuadrado")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            lado = float(input("Ingrese el lado del cuadrado: "))
            print("El área del cuadrado es:", area_cuadrado.calcular_area_cuadrado(lado))
        elif opcion == '2':
            # Lógica para la opción 2
            print("Has seleccionado la opción 2.")
        elif opcion == '3':
            # Lógica para la opción 3
            print("Has seleccionado la opción 3.")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()

