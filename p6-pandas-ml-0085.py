import pandas as pd
import numpy as np

serie_amigos=["Alan","Ricardo","Johan","Scarlett","Christian","Iram","Gabriel"]
print("---serie listado de amigos  NC 0085")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("---serie listado de billetes  NC 0085")
billetes=pd.Series(serie_billetes)
print(billetes)

serie_billetes=[20,50,100,200,500,1000]
serie_billetreas=["veinte","cincuenta","cien","docientos","quinientos","mil"]
print("---serie listado nombre y valor de billetes MX NC 0085")
tablabilletes=pd.Series(serie_billetreas,serie_billetes)
print(tablabilletes)
# diccionario dataframe
# diccionario de valor monedas y nombre 
print("datos de diccionario a Dataframe en pandas")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_billetreas":["veinte","cincuenta","cien","docientos","quinientos","mil"]

} 

tablaRicardo=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablaRicardo)

print("casa de cambio de Ricardo Lopez NC 0085")