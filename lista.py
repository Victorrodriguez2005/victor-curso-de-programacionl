calificaciones = [85, 92, 78, 95, 88, 70, 90]

suma_calificaciones = 0
for calificacion in calificaciones:
    suma_calificaciones += calificacion

promedio = suma_calificaciones / len(calificaciones)

nota_mas_alta = max(calificaciones)
nota_mas_baja = min(calificaciones)

print("--- Analisis de Calificaciones ---")
print(f"Lista de calificaciones: {calificaciones}")
print(f"Suma total de calificaciones: {suma_calificaciones}")
print(f"Número de calificaciones: {len(calificaciones)}")
print(f"Promedio de calificaciones: {promedio:.2f}") 
print(f"Nota más alta: {nota_mas_alta}")
print(f"Nota más baja: {nota_mas_baja}")
print("-------------------------------")