#coding: utf-8

nomes = ["Larissa", "Rafael", "Marcos","Joao"]

try:
    for i in range (4):
        print(nomes[i])
except IndexError as erro1:
    print("Houve um erro de indice:", erro1)
else:
    print("Não houve erro!")

print("Linha 11")