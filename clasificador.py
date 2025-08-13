def clasificar_numero(numero):
  """
  Clasifica un numero como positivo, negativo o cero.

  Args:
    numero: El numero a clasificar (entero o flotante).
  """
  if numero > 0:
    print(f"El numero {numero} es positivo.")
  elif numero < 0:
    print(f"El numero {numero} es negativo.")
  else:
    print(f"El numero {numero} es cero.")

print
clasificar_numero(5)
clasificar_numero(-10)
clasificar_numero(0)
clasificar_numero(3.14)
clasificar_numero(-0.5)