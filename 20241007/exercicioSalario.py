#coding: utf-8

def calculoComissao(vendas):
    comissao = 0.15*vendas
    return comissao

if __name__ == "__main__":

    nome = input("Insira o nome do vendedor: ")
    salario = float(input("Informe o salário: "))
    vendas = float(input("Informe o valor em vendas: "))

    comissao = calculoComissao(vendas)
    print(nome, "obteve", comissao, "de comissão e vai receber", salario+comissao)



    
