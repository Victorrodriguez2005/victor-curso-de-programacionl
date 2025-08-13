edad = 20  
esta_en_lista = True  

edad_minima_acceso = 18

if edad >= edad_minima_acceso and esta_en_lista:
    print("¡Acceso concedido! ¡Bienvenido a la fiesta!")
else:
    print("Acceso denegado. Asegurate de ser mayor de edad y de estar en la lista de invitados.")

print("\n--- Pruebas adicionales ---")

edad = 20
esta_en_lista = False
if edad >= edad_minima_acceso and esta_en_lista:
    print(f"Edad: {edad}, En lista: {esta_en_lista} -> ¡Acceso concedido!")
else:
    print(f"Edad: {edad}, En lista: {esta_en_lista} -> Acceso denegado.")

edad = 16
esta_en_lista = True
if edad >= edad_minima_acceso and esta_en_lista:
    print(f"Edad: {edad}, En lista: {esta_en_lista} -> ¡Acceso concedido!")
else:
    print(f"Edad: {edad}, En lista: {esta_en_lista} -> Acceso denegado.")

edad = 17
esta_en_lista = False
if edad >= edad_minima_acceso and esta_en_lista:
    print(f"Edad: {edad}, En lista: {esta_en_lista} -> ¡Acceso concedido!")
else:
    print(f"Edad: {edad}, En lista: {esta_en_lista} -> Acceso denegado.")

edad = 18
esta_en_lista = True
if edad >= edad_minima_acceso and esta_en_lista:
    print(f"Edad: {edad}, En lista: {esta_en_lista} -> ¡Acceso concedido!")
else:
    print(f"Edad: {edad}, En lista: {esta_en_lista} -> Acceso denegado.")