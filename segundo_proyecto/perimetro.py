def calcular_perimetro_cuadrado():
    while True:
        try:
            lado = float(input("Ingresa la longitud del lado del cuadrado: "))
            return 4 * lado
        except ValueError:
            print("Error: Debes ingresar un número.")

def calcular_perimetro_rectangulo():
    while True:
        try:
            lado1 = float(input("Ingresa la longitud del primer lado del rectángulo: "))
            lado2 = float(input("Ingresa la longitud del segundo lado del rectángulo: "))
            return 2 * (lado1 + lado2)
        except ValueError:
            print("Error: Debes ingresar números.")

def calcular_perimetro_triangulo():
    while True:
        try:
            lado1 = float(input("Ingresa la longitud del primer lado del triángulo: "))
            lado2 = float(input("Ingresa la longitud del segundo lado del triángulo: "))
            lado3 = float(input("Ingresa la longitud del tercer lado del triángulo: "))
            return lado1 + lado2 + lado3
        except ValueError:
            print("Error: Debes ingresar números.")

def calcular_perimetro_circulo():
    while True:
        try:
            radio = float(input("Ingresa el radio del círculo: "))
            return 2 * math.pi * radio
        except ValueError:
            print("Error: Debes ingresar un número.")

print("Perímetro del cuadrado:", calcular_perimetro_cuadrado())
print("Perímetro del rectángulo:", calcular_perimetro_rectangulo())
print("Perímetro del triángulo:", calcular_perimetro_triangulo())
print("Perímetro del círculo:", calcular_perimetro_circulo())
