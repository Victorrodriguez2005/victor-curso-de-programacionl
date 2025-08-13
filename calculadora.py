# CALCULADORA DE PROPINA

cuenta = float(input("ingrese el total de la cuenta:"))
porcentaje = float(input("ingrese el porcentaje de la propina:"))

propina = cuenta * (porcentaje/100)

total_pagar = cuenta + propina

print("el total a pagar incluyendo la propina es:", total_pagar)
