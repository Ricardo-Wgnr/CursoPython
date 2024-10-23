#coding: utf:8

def compreensaoLista1():
    nomes = ["Larissa", "Rafael", "Marcos", "Joao"]
    nomesAprovados = [(nome + " Aprovado") for nome in nomes]
    print(nomesAprovados)

def compreensaoLista2():
    def eh_par(num):
        if (num%2):
            return False
        else:
            return True
    num2 = [i for i in range(20) if (eh_par(i))]
    print(num2)

if __name__ == "__main__":
#    compreensaoLista1()
    compreensaoLista2()