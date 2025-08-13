def calcular_descuento_tienda(precio_original):
    descuento = 0

    if precio_original >= 100:
        descuento = 0.20  
        print(f"¡Felicidades! Se aplica un 20% de descuento por una compra de {precio_original:.2f}€ o más.")
    
    elif precio_original >= 50:
        descuento = 0.10
        print(f"¡Genial! Se aplica un 10% de descuento por una compra de {precio_original:.2f}€ o más.")
    
    else:
        print(f"Tu compra es de {precio_original:.2f}€. No aplica descuento en esta ocasión.")

    precio_final = precio_original * (1 - descuento)

    print(f"El precio original era: {precio_original:.2f}€")
    print(f"El precio final con descuento es: {precio_final:.2f}€")
    print("-" * 30)

print("--- Ejemplo 1: Compra de 120€ ---")
calcular_descuento_tienda(120)

print("--- Ejemplo 2: Compra de 75€ ---")
calcular_descuento_tienda(75)

print("--- Ejemplo 3: Compra de 30€ ---")
calcular_descuento_tienda(30)

print("--- Ejemplo 4: Compra de 100€ ---")
calcular_descuento_tienda(100)

print("--- Ejemplo 5: Compra de 50€ ---")
calcular_descuento_tienda(50)
