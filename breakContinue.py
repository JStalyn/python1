
from ast import Num
from cgi import print_form
from cgitb import text


def run():
#    imprimir de dos en dos
#     for contador in range(1001):
#         if contador %2 != 0:
#             continue
#         print(contador)
# ejemplo brak
#     for i  in range(1000):
#         print(i)
#         if i == 909:
#             break
# imprime hasta una letra específica 
    # texto = input("escribe un texto ")
    # for letra in texto:
    #     if letra =='o':
    #         break
    #     print(letra)
    número = input("ingresá un número ")
    limite = len(str(número))
    limite = int(limite)
    contador = 0

    while contador < limite:
        if contador == 5:
            continue
        print(número[contador])
        contador += 1
           
   

if __name__ == '__main__':
    run()