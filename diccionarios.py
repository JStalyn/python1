def run():
    mi_diccionario = {
        'llave1':1,
        'llave2': 2,
        "llave3": 3    
    }
   # print (mi_diccionario["llave 1"])
    poblaicon_pasis={
        "Argentina": 44_938_712,
        "Brasil": 444938712,
        "Colombia" : 50372424
    }
    print(poblaicon_pasis["Argentina"])
## imprime las llaves
    for pais in poblaicon_pasis.keys():
        print(pais)
    #imprimee los valores de las llaves
    for pais in poblaicon_pasis.values():
        print (pais )
    for pais, poblacion in poblaicon_pasis.items():
        print(pais +" "+ str(poblacion))
     
if __name__ == "__main__":
    run()