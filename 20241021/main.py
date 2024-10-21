#coding: utf-8

def script01():
    vC = [1,3.4,'A', "IFSC"]
    print(vC)
    input("Pressione entrer para continuar")
    print("Inserção de 56 na posição 0")
    vC.insert(0, 56)
    print(vC)
    input("Pressione enter para continuar")
    print("Inserção de B na posição 3")
    vC.insert(3, 'B')
    print(vC)
    input("Inserção no final do vetor de 11")
    vC.append(11)
    print(vC)

    return vC

def script01Limpo():
    vC = [1,3.4,'A', "IFSC"]
    vC.insert(0, 56)
    vC.insert(3, 'B')
    vC.append(11)
    vC.append('A')

    return vC

def script02(vetA):
    print("Vetor recebido:", vetA)
    print("Valor removido:", vetA[2])
    vetA.remove(3.4)
    print(vet)
    print("Escolha a remoção do A:")
    escolha = input("Pressione 1 para primeira ocorrencia, outra tecla para todas:")
    if(escolha == '1'):
        vetA.remove('A')
    else:
        while('A' in vetA):
            vetA.remove('A')
    print(vetA)

def script03(vetB):
    print(vetB)
    del vetB[3]
    print(vetB)
    del vetB[1:3]
    print(vetB)

def script04():
    valores = list(range(1,11))
    anos = list(range(2020,2060,10))
    print(valores)
    valores.extend(anos)
    print(valores)

def script05():
    mercado = ["ouro", "bitcoin", "titulos", "Dólar", "Real"]
    print(mercado)
    #Para poder ordenar letras maiusculas e minusculas
    mercado.sort(key=str.casefold)
    print(mercado)

if __name__ == "__main__":
    vet = script01Limpo()
    script05()
