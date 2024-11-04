#coding: utf-8

while(True):
    try:
        numJogadores = float(input())
    except EOFError as err:
        break
    
    votos = list(map(float, input().split()))

    votosFav = 0
    votosCont = 0
    for i in votos:
        if (i == 1):
            votosFav += 1
        else :
            votosCont += 1
    if (votosFav >= ((2/3)*numJogadores)):
        print("impeachment")
    else:
        print("acusacao arquivada")
