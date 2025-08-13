# Datos personales
nombre = input("Por favor, ingresa tu nombre: ")

edad = int(input("Por favor, ingresa tu edad: "))
ciudad = input("Por favor, ingresa tu ciudad de nacimiento: ")

datos_personales = (nombre, edad, ciudad)

nombre_desempaquetado, edad_desempaquetada, ciudad_desempaquetada = datos_personales

print(f"El usuario {nombre_desempaquetado}, de {edad_desempaquetada} años, nació en {ciudad_desempaquetada}.")