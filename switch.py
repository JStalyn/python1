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

>>> nomre = input ("¿cuál es tu nombre ?")
¿cuál es tu nombre ?facundo
>>> nombre.capitaliza()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nombre' is not defined. Did you mean: 'nomre'?
>>> nomre.capitalize() 
'Facundo'
>>> nombre = "francisco "
>>> nombre 
'francisco '
>>> nombre[0]
'f'
>>> nombre[0:3] 
'fra'
>>> nombre[3:5]
'nc'
>>> nombre[3:5:1]
'nc'
>>> nombre[2:5]
'anc'
>>> nombre[::-1] 
' ocsicnarf'
>>> nombre = nombre.strip()
>>> nombre
'francisco'
>>> nombre[::-1]
'ocsicnarf'