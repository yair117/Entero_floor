from math import *

def verificar_numero():
    try:
        num = float(input("Ingresa un número: "))
        if num == int(num):
            print("El número es entero.")
        else:
            entero_inferior = floor(num)
            print(f"El entero inmediato inferior de {num} es {entero_inferior}.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Llamada a la función
verificar_numero()