def calcular_perimetro(figura, lados):
  """
  Función para calcular el perímetro de una figura geométrica.

  Parámetros:
    figura (str): Tipo de figura geométrica ("triangulo", "cuadrado", "rectangulo", "circulo").
    lados (list): Lista que contiene la longitud de cada lado de la figura.

  Retorno:
    float: El perímetro de la figura geométrica.
  """

  if figura == "triangulo":
    if len(lados) != 3:
      raise ValueError("Un triángulo tiene 3 lados")
    return sum(lados)
  elif figura == "cuadrado":
    if len(lados) != 4:
      raise ValueError("Un cuadrado tiene 4 lados")
    if not all(lado == lados[0] for lado in lados):
      raise ValueError("Un cuadrado tiene todos sus lados iguales")
    return 4 * lados[0]
  elif figura == "rectangulo":
    if len(lados) != 4:
      raise ValueError("Un rectángulo tiene 4 lados")
    return 2 * (lados[0] + lados[2])
  elif figura == "circulo":
    if len(lados) != 1:
      raise ValueError("Un círculo tiene 1 radio")
    return 2 * math.pi * lados[0]
  else:
    raise ValueError("Figura no válida")

# Ejemplo de uso
perimetro_triangulo = calcular_perimetro("triangulo", [3, 4, 5])
print(f"Perímetro del triángulo: {perimetro_triangulo}")

perimetro_cuadrado = calcular_perimetro("cuadrado", [4, 4, 4, 4])
print(f"Perímetro del cuadrado: {perimetro_cuadrado}")

perimetro_rectangulo = calcular_perimetro("rectangulo", [5, 7, 5, 7])
print(f"Perímetro del rectángulo: {perimetro_rectangulo}")

perimetro_circulo = calcular_perimetro("circulo", [10])
print(f"Perímetro del círculo: {perimetro_circulo}")