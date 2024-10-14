#coding: utf-8

def scr0():
    vA = [] # Vetor vazio e de tamanho 0
    vB = [ None ] * 5 # Vetor vazio de tamanho 5
    vC = [1 , 3.4 , "A" , " IFSC " ] #vetor de
    # tamanho 4 e com tipos diferentes
    print ( vA ) # Imprime o vetor vA
    print ( vB ) # Imprime o vetor vB
    print ( vC ) # Imprime o vetor vC

def scr1():
    tA = () # Tupla vazia, inútil porque não pode
    #sofrer alteração
    tB = (1 , 3.4 , "A" , " IFSC " ) #tupla de
    #tamanho 4 e com tipos diferentes
    print ( tA ) # Imprime a tupla tA
    print ( tB ) # Imprime a tupla tB

def saidaFuncao():
    a = 2.4
    b = 3.5
    return a,b #retorno de funcao é uma tupla

if __name__ == "__main__":
    #scr0()
    #scr1()
    #print(saidaFuncao())

    vC = [1,3.4,"A","IFSC"]
    for i in vC:
        print(type(i))