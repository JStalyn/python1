from cgi import print_arguments
import random 


def run():
    numero_aleatorio = random.randint(1,100)
    numero_elejido = int(input("elige el número del uno al 100"))

    while numero_aleatorio!= numero_elejido:
        if numero_elejido < numero_aleatorio:
            print("el número es más grande")
            
        else:
            print("el número es má pequeño")
        numero_elejido = int(input("elige el núm  ")) 

    print("correcto")

if __name__ == '__main__':
    run()