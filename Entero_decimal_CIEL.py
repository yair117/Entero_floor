from math import *
def verificar_numero():
    try:
        num = float(input("INGRESA EL NUMERO: "))
        if num == int(num):
            print("El numero es entero.")
        else:
            numero_inmediato = ceil(num)
            print("El entero inmediato inferior de", num," es ",numero_inmediato)
    except ValueError:
        print("Por favor, ingresa un número válido.")

verificar_numero()