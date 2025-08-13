# Mi Lista de Compras

lista_compras = []
print("¡Bienvenido a tu Lista de Compras personal!")
print(f"Tu lista actual tiene {len(lista_compras)} artículos.")

print("\nAñadiendo los primeros tres artículos a tu lista...")
lista_compras.append("refresco")
lista_compras.append("jamon")
lista_compras.append("Pan")

print("\nAquí está tu lista de compras completa:")
for i, item in enumerate(lista_compras):
    print(f"{i + 1}. {item}")

print(f"\n¡Tienes un total de {len(lista_compras)} artículos en tu lista de compras!")