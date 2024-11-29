#coding: utf-8

import requests 		#Usado para baixar o arquivo. 
import os, shutil
import sys
'''
Baixa o arquivo Testes do site em formato zip e depois obtém dados da pasta Teste
'''
def Selecao_Arquivos(): 	
	CaminhoPasta = os.getcwd()
	#print(os.getcwd())
	url = 'https://docente.ifsc.edu.br/louis.augusto/Textos.zip'
	r = requests.get(url, allow_redirects=True)
	with open("Textos.zip", mode="wb") as file:
		file.write(r.content)
	shutil.unpack_archive("Textos.zip")	#Extrai os arquivos 
	#Obtenção dos arquivos contidos na pasta Textos
	CaminhoPastaTextos = CaminhoPasta+os.sep+"Textos"
	#Mudança do cursor para a pasta Textos
	Pasta_atual = os.chdir("Textos")
	#Arquivos no interior da pasta Textos. 
	ArquivosPastaTextos = os.listdir()
	#Remoção dos arquivos indesejados	
	ArquivosIndesejados = ['pg67979.txt']
	for i in range(len(ArquivosIndesejados)): 
		if ArquivosIndesejados[i] in ArquivosPastaTextos: 
			ArquivosPastaTextos.remove(ArquivosIndesejados[i])	
	print("Arquivos selecionados: ")
	for i,j in enumerate(ArquivosPastaTextos):
		print(f"Livro {i+1}: {j} ")
	print()	
	return ArquivosPastaTextos 
		
def Abertura_Arquivos(ListaArquivos): 
	ListaReferenciaArquivos = []
	for NomeArq in ListaArquivos: 
		try: 
			RefArquivo = open(NomeArq, 'r', encoding = 'utf-8')			
		except IOError as IOEr: 
			print("Erro na abertura do arquivo ", NomeArq)
			print(IOEr)
		else: 
			print(NomeArq, "aberto corretamente")	
			ListaReferenciaArquivos.append(RefArquivo)
	print()
	return ListaReferenciaArquivos	
	
def Fechamento_Arquivos(ListaReferenciaArquivos): 
	print("Fechamento de arquivos:") 
	for NomeArq in ListaReferenciaArquivos: 
		if not NomeArq.closed:
			print("Fechamento de ", NomeArq.name)
			NomeArq.close()
	return True	
	
def MontagemDicionarioPalavras(ListaReferenciaArquivos):
	Dicionario = {}
	TamanhoMinimoPalavra = 5
	CaracteresBasicos = '",.!?: -;()“”‘’—'
	CaracteresExtras = "'"	
	CaracteresRemover = CaracteresBasicos+CaracteresExtras
	NomeProprio = ["harry",'ron', 'j.k','hagrid', "hermione", "voldemort", 'dumbledore', 'snape','mcgonagall', 'rowling','hogwarts','potter','valancy', 'neville', 'ginny']			 
	for arq in ListaReferenciaArquivos: 
		print("Leitura do livro ", arq.name)		
		while True:
			linha = arq.readline()		
			if not linha: 
				break
			palavras = linha.split()
			if palavras!="": 
				for i in range(len(palavras)):
					Palavra = (palavras[i].strip(CaracteresRemover)).lower()
					if Palavra not in NomeProprio: 
						if (len(Palavra))>=TamanhoMinimoPalavra: 							 
							k = Dicionario.get(Palavra)
							if k == None: 
								Dicionario[Palavra]=1
							else: 
								Dicionario[Palavra]+=1 	
	Dicionario_Decrescente = dict(sorted(Dicionario.items(), key=lambda item: item[1], reverse=True))
	#Retorno para a pasta pai
	os.chdir("..")
	with open('FrequenciaPalavras.dat', 'w') as arq:
		contador = 0
		for chave, valor in Dicionario_Decrescente.items(): 
			try: 
				valor = int(chave)
			except ValueError: 
				strg = f"{contador+1} - {chave} - {valor}\n"
				if contador<2000: 
					arq.write(strg)
					contador+=1
				
					
			
	


if __name__=="__main__": 
	Arquivos = Selecao_Arquivos()
	ListaReferenciaArquivos = Abertura_Arquivos(Arquivos)
	MontagemDicionarioPalavras(ListaReferenciaArquivos)	
	Fechamento_Arquivos(ListaReferenciaArquivos)
	


