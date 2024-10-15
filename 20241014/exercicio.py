#coding: utf-8

if __name__ == "__main__":

    entradas = input()
    entradasSep = entradas.split()
    resultados = []

    for i in range(0, len(entradasSep)):
        resultados.append(float(entradasSep[i]) * 3)

    print(resultados)