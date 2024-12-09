#coding: utf-8

from ClassePasta import *
from ClasseArquivoPastaSuspensa import *
import time as t


def CriarPasta(QdeArquivos=5): 	
	Pasta1 = Pasta() #Crio a pasta
	Pasta1.CriarPastaVazia()	
	for _ in range(QdeArquivos):		
		Pasta1.Receber_arquivo()
	Pasta1.get_chaves_arquivos_pasta()
	return Pasta1				
		 	
def CriarArquivo(): 
	Arq1 = ArquivoPastaSuspensa("amarelo", "Pesquisa",NumMaxPastas=20)		
	return Arq1

def mostrarPastas(Pastas):
	for i, j in enumerate (Pastas):
		print(f"Pasta {i} com conteudo {j.conteudo}")
		for c,k in j.documento.items():
			print(f"\t chave: {c} e valor: {k}")

if __name__ == "__main__": 

	arquivoDePastas = []
	numPastasCriadas = 2
	arquivo1 = CriarArquivo()
	for i in range(numPastasCriadas):
		pastaSuspensa = CriarPasta()
		arquivo1.Pastas.append(pastaSuspensa)
		t.sleep(1.2) #parar para mudar momento unix
		print()
	mostrarPastas(arquivoDePastas)
	arquivo1.gravarArquivoPastaSuspensa()


		
