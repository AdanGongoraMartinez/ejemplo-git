def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

# from validador import validar

# def dividir(a, b):
#     es_valido, mensaje = validar(b)
#     if not es_valido:
#         return mensaje
#     else:
#         if b != 0:
#             return a / b
#         else:
#             return "No se puede dividir por cero"

# # Ejemplo de uso:
# resultado = dividir(10, 0)
# print(resultado)  # Salida: "No se puede dividir por cero"

# resultado = dividir(10, 5)
# print(resultado)  # Salida: 2.0