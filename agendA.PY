agenda_contactos = {
    "danel": "0412-0670987",
    "carlos": "0414-9780987"
}

print("¡Bienvenido a tu Agenda de Contactos Simple!")
print("Contactos actuales:")
for nombre, telefono in agenda_contactos.items():
    print(f"- {nombre}: {telefono}")
print("-" * 30) # Linea separadora para mejorar la legibilidad

# Pedimos al usuario que ingrese el nombre del contacto que desea buscar.
nombre_buscado = input("Ingresa el nombre del contacto que deseas buscar: ")

# Usamos una estructura if-else para verificar si el nombre existe en el diccionario.
if nombre_buscado in agenda_contactos:
    # Si el contacto existe, mostramos su número de teléfono.
    telefono_encontrado = agenda_contactos[nombre_buscado]
    print(f"¡Contacto encontrado! El teléfono de {nombre_buscado} es: {telefono_encontrado}")
else:
    # Si el contacto no se encuentra, mostramos un mensaje indicando que no fue encontrado.
    print(f"Lo siento, '{nombre_buscado}' no se encuentra en la agenda. Contacto no encontrado.")

print("\n¡Gracias por usar la agenda!")