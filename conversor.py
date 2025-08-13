
def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.

    Args:
        celsius (float): La temperatura en grados Celsius.

    Returns:
        float: La temperatura equivalente en grados Fahrenheit.
    """
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
    try:
        temperatura_celsius_str = input("Ingresa la temperatura en grados Celsius: ")
        temperatura_celsius = float(temperatura_celsius_str)

        temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
       
        print(f"\n{temperatura_celsius} grados Celsius equivalen a {temperatura_fahrenheit:.2f} grados Fahrenheit.")
        print("\n¡Conversión completada con éxito!")

    except ValueError:
        
        print("\nError: Por favor, ingresa un valor numérico válido para la temperatura.")
    except Exception as e:
        
        print(f"\nOcurrió un error inesperado: {e}")
