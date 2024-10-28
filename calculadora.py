import os

# Calculadora simple en Python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    # Obtener la opción de operación y los números de las variables de entorno
    opcion = os.getenv("OPERACION", "1")  # Valor por defecto: "1" (Sumar)
    num1 = float(os.getenv("NUM1", 0)) # Si NUM1 no está definido, usará 0 como valor por defecto
    num2 = float(os.getenv("NUM2", 0))

    # Ejecutar la operación seleccionada
    if opcion == '1':
        print(f"{num1} + {num2} = {sumar(num1, num2)}")
    elif opcion == '2':
        print(f"{num1} - {num2} = {restar(num1, num2)}")
    elif opcion == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif opcion == '4':
        resultado = dividir(num1, num2)
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Opción no válida")

# Ejecutar la calculadora
calculadora()
