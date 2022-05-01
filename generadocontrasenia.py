import random
def generar_contrasenia():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['☺', '☻', '♥', '♦', '♣', '♠', '♪', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracateres = MAYUS + MINUS + NUMS +CHARS

    contrasenia = []
    for i in range(15):
        carcarter_random = random.choice(caracateres)
        contrasenia.append(carcarter_random)

    contrasenia = "".join(contrasenia)
    return contrasenia

def run():
    contrasenia = generar_contrasenia()
    print("la contraseña es: "+ contrasenia)

if __name__ == "__main__":
    run()