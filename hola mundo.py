#Calculadora 

print
num1_str = input("Ingresa el primer numero: ")

num2_str = input("Ingresa el segundo numero: ")

try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    print("Error: Por favor, asegurate de ingresar numeros validos.")
    exit()

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Indefinida (división por cero)" 

print("\n--- Resultados ---")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print("--- Fin de la Calculadora ---")

