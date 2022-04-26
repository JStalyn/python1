def conversor(tipo_pesos,valor_dolar):
    pesosco = float(input('cantidad de pesos '+tipo_pesos+''))
    dolares = pesosco / valor_dolar
    dolares= round(dolares,2)
    dolares = str(dolares)
    print('tienes'+dolares )

menu = """
Bienvenido al conversor de modena ♫☼►..
1.-- pesos aguentinos
2.- pesos argentinos
3.- pesos mexicanos
"""
opcion = int(input(menu))
if opcion==1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24 )
else:
    print('ingresá nu´meros del 1 al tres nmms')

