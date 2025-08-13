import datetime

año_actual = datetime.datetime.now().year

año_nacimiento_str = input("Por favor, introduce tu año de nacimiento: ")

año_nacimiento_int = int(año_nacimiento_str)

edad = año_actual - año_nacimiento_int

es_mayor_de_edad = edad >= 18

if es_mayor_de_edad:
    print(f"Tienes {edad} años. ¡Eres mayor de edad!")
else:
    print(f"Tienes {edad} años. Aun no eres mayor de edad.")
