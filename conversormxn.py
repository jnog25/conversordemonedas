pesos = input("Cuantos pesos Mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 20.3
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " Dolares")