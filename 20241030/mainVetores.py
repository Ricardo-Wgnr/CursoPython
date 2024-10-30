#coding: utf-8

def aprovar_pessoa(nome):
    return nome+" APROVADO"

def antiguidade(pintura):
    if pintura[2]<1900:
        return True
    else:
        return False

def map1():
    nomes = ["Larissa", "Rafael", "Marcos","Joao"]

    situacao = list(map(aprovar_pessoa,nomes))
    print(situacao)
    print(nomes)

def filter1():
    pinturas = [
    ["Picasso", "Les demoiselles", 1907],
    ["Monet", "Lagoa dos lirios d’água", 1899],
    ["Renoir", "Duas irmãs", 1881] ,
    ["Tarcila", "Abaporu", 1928] ]

    print(pinturas)
    print()
    print("pinturas pós filtro:", list(filter(antiguidade, pinturas)))

def set1():
    numeros = [2,2,5,8]
    set_numeros = sorted(set(numeros))
    print(set_numeros)
    frutas = sorted({"maca", "uva", "banana", "maca", "morango"})
    print(frutas)

def set2():
    a = {2,2,5,8}
    b = {2,2,3,9}
    print(a.intersection(b))
    print(a.symmetric_difference(b))
    print(a.union(b))

if __name__ == "__main__":
    #map1()
    #filter1()
    set2()