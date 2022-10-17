Menu = """
Bienvenido al Conversor de Monedas 🤑

1 - Pesos colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(Menu))

def convertir(valor_dolar, pais):
    pesos = float(input("Cuantos pesos " + pais + " tienes?: "))
    dolares = round((pesos / valor_dolar),2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")

if opcion == 1:
    convertir(3875, "Colombianos")
elif opcion == 2:
    convertir(65, "Argentinos")
elif opcion == 3:
    convertir(20, "Mexicanos")
else:
    print("Elige una opcion correcta por favor")