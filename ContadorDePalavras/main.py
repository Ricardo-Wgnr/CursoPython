#coding: utf-8

'''
Abertura de arquivo por redirecionamento
Contar palavras
Guardar em arquivo
'''

dicionario = {}
caracteresBases = '",.!?;:-()'
caracteresExtras = "'"
caracteresRemover = caracteresExtras + caracteresBases
while(True):
    try:   
        linha = input().split()
        if (linha != ""):
            for i in range(len(linha)):
                palavra = (linha[i].strip(caracteresRemover)).lower()
                if (len(palavra) >= 3):
                    k = dicionario.get(palavra)
                    if (k == None):
                        dicionario[palavra] = 1
                    else:
                        dicionario[palavra] += 1
    except EOFError as Er:
        break

dicionarioOrdenado = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse= True))
for chave, valor in dicionarioOrdenado.items():
    print(chave,valor)