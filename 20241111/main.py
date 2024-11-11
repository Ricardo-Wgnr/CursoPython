#coding: utf-8

def testes():
    diarioNotas = {"Ana Julia": 5, "Igor": 7}
    print(diarioNotas["Ana Julia"])
    print(diarioNotas["Igor"])

    Preco={} #Dicionário que irá guardar preços de produtos
    Preco ["manga"] = 6
    Preco ["banana"] = 4
    Preco [ "maçã"] = 10
    print ( Preco [ "manga" ])
    print ( Preco [ "maçã" ])
    Preco ["manga"] = 7
    print(Preco["manga"])

    diarioNotas2 = {"Ricardo": []}
    diarioNotas2["Ricardo"].append(7)
    diarioNotas2["Ricardo"].append(8)
    print(diarioNotas2["Ricardo"])

if __name__ == "__main__":
    #testes()
    pass