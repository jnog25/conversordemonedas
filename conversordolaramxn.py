dolares = input("Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_dolar = 20.3
pesos = dolares * valor_dolar
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " Pesos")