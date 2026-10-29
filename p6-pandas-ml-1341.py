import pandas as pd
import numpy as np



serie_amigos = ["jesus", "jazmin", "alonso", "zeus", "eliseo", "el adrian", "molly"]
print("---serie listado de amigos  NC 1341")

# Pasamos la lista directamente para que cada nombre ocupe su propia fila
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
print("serie  listado  valor de billetes MX NC 1341")
amigos = pd.Series(serie_billetes)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
serie_bletras = ["veinte", "cincuenta", "cien", "docientos", "quinientos", "mil"]
print("serie  listado  valor de billetes MX NC 1341")
tablabilletes = pd.Series(serie_bletras, index=serie_billetes)
print(tablabilletes)

#diccionario dataframe
# diccionario de vavlor monedas y nombre
print("datos de diccionario a dataframeen pandas")
dic_monedas={
    "serie_billetes" : [20, 50, 100, 200, 500, 1000],
    "serie_bletras" : ["veinte", "cincuenta", "cien", "docientos", "quinientos", "mil"]
}

tablayaret=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("casa  de cambio valeria yaretzi NC 1341")