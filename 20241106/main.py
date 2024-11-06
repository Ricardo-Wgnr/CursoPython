#coding: utf-8

def ehMatriz(matriz):
    if type(matriz) == list:
        numLinhas = len(matriz)
        if type(matriz[0]) == list:
            numColunas = len(matriz[0])
            return numLinhas, numColunas
        else:
            return False
    else: 
        return False

def matriz1():
    mA = [ None ] * 4 
    for i in range (0 , 4):
        mA [ i ] = [ None ] * 3   
    print (mA)

    mB = [[1,2,3],["a","b","c"]]
    print (mB)

def criaMatriz(numLinhas, numColunas):
    matrizA = [None]*numLinhas
    for i in range(numLinhas):
        matrizA[i] = [None]*numColunas
    return matrizA

def preencheMatrizLinha(matriz):
    verificaMatriz = ehMatriz(matriz)
    if (verificaMatriz!= False):
        numLinhas, numColunas = verificaMatriz
        for i in range(numLinhas):
            for j in range (numColunas):
                matriz[i][j] = i*numColunas+j+1

def preencheMatrizColuna(matriz):
    verificaMatriz = ehMatriz(matriz)
    if (verificaMatriz!= False):
        numLinhas, numColunas = verificaMatriz
        for j in range(numColunas):
            for i in range (numLinhas):
                matriz[i][j] = j*numLinhas+i+1

def imprimirMatriz(M): 
    verificaMatriz = ehMatriz(M)
    if (verificaMatriz!= False):
        numLinhas, numColunas = verificaMatriz
        for i in range(numLinhas): 
            for j in range(numColunas): 
                print(M[i][j], end = " ")
            print()	

def compreensaoListasMatriz():
    matriz = [[i for i in range(1,7)] for j in range (5)]
    imprimirMatriz(matriz)

def preencherMatrizCompreensaoLinha(matriz):
    verificaMatriz = ehMatriz(matriz)
    if (verificaMatriz!= False):
        numLinhas, numColunas = verificaMatriz
        matriz = [[i*numColunas+j+1 for j in range (numColunas)] for i in range (numLinhas)]

    return matriz

def preencherMatrizCompreensaoColuna(matriz):
    verificaMatriz = ehMatriz(matriz)
    if (verificaMatriz!= False):
        numLinhas, numColunas = verificaMatriz
        matriz = [[j*numLinhas+i+1 for j in range (numColunas)] for i in range (numLinhas)]

    return matriz

if __name__ == "__main__":
    #matriz1()
    matriz = criaMatriz(4,3)
    matriz = preencherMatrizCompreensaoLinha(matriz)
    imprimirMatriz(matriz)
    print()
    matriz2 = criaMatriz(4,3)
    matriz2 = preencherMatrizCompreensaoColuna(matriz2)
    imprimirMatriz(matriz2)
    