def convertir_nota(nota):
    """
    Convierte una nota numerica (0-100) a una calificacion por letra.

    Rangos de calificacion:
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59

    Args:
        nota (int): La nota numérica a convertir, debe estar entre 0 y 100.

    Returns:
        str: La calificacion por letra (A, B, C, D, F).
    """
    if nota >= 90:
        return 'A'
    elif nota >= 80:
        return 'B'
    elif nota >= 70:
        return 'C'
    elif nota >= 60:
        return 'D'
    else:
        return 'F'

print(f"La nota 95.5 corresponde a la calificación: {convertir_nota(95.5)}")
print(f"La nota 82 corresponde a la calificación: {convertir_nota(82)}")
print(f"La nota 70 corresponde a la calificación: {convertir_nota(70)}")
print(f"La nota 65 corresponde a la calificación: {convertir_nota(65)}")
print(f"La nota 59 corresponde a la calificación: {convertir_nota(59)}")
print(f"La nota 100 corresponde a la calificación: {convertir_nota(100)}")
print(f"La nota 0 corresponde a la calificación: {convertir_nota(0)}")