#coding: utf-8

def Funcao_abertura_gravacao(): 
	#abertura e gravacao		
	t_str= "Eu gosto de Python. "
	t2_str = "Vamos estudar python. "	
	ft=open("ArqTexto.dat",'w')
	ft.write(t_str)
	ft.write('\n')
	ft.write(t2_str)
	ft.write('\n')
	ft.close()
	
def Funcao_abertura_anexacao(): 
	ft2=open("ArqTexto.dat",'a')
	t3_str = "Anexacao de arquivo"
	ft2.write(t3_str+'\n')
	ft2.close()

def Funcao_abertura_leitura():
	ft2 = open("ArqTexto.dat",'r')
	linhas = ft2.readlines()
	ft2.close()
	#Impressão
	print(linhas)
	'''
	for i in range(len(linhas)):
		print(linhas[i],end = '')
	print()
	'''

if __name__=="__main__": 
	#Funcao_abertura_gravacao()
	#Funcao_abertura_anexacao()
	Funcao_abertura_leitura()
	
	
