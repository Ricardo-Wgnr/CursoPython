#coding: utf-8

def script1():
	#Lista = list(range(6,13))
	for i in range(6,18,2):
		print(i)
	#print(Lista)

def script2():
	soma = 0
	quantidade = 0
	n = float(input("Entre com o valor inicial de n: "))
	while (n!=0):
		#print(f"Soma = {soma} e quantidade = {quantidade}")
		soma+=n
		quantidade=quantidade+1
		n = float(input("Entre com um valor para n, zero para sair: "))
	else: 	
		print("Entrada no else")
		print(f"Soma = {soma} e quantidade = {quantidade}")
		
	print("(Media = {:.2f})".format(soma/quantidade))	

def script2b():
	soma = 0
	quantidade = 0
	#n = float(input("Entre com o valor inicial de n: "))
	n = float(input())
	while (n!=0):
		#print(f"Soma = {soma} e quantidade = {quantidade}")
		soma+=n
		quantidade=quantidade+1
		n = float(input())
	else: 	
		print("Entrada no else")
		print(f"Soma = {soma} e quantidade = {quantidade}")
		
	print("(Media = {:.2f})".format(soma/quantidade))	


def script3():	
	#Entrada do numero pelo usuario.
	n = int(input("Entre com inteiro menor que 10: "))
	if (n<10): 
		contador = 0
		while(n<20):
			n+=1
			print(n)
			contador+=1
		else: #else para o while	
			print(f"Total de sucessores = {contador}")
	else: #else para o if
		print("O numero tinha que ser menor do que 10. ")	

def script4(): # inclui loop infinito até o usuario fazer o que é mandado	
	flag = False
	while True:
		print(flag) 
		if flag==True: 
			break	
		#Entrada do numero pelo usuario.
		n = int(input("Entre com inteiro menor que 10: "))
		if (n<10):
			flag = True 
			contador = 0
			while(n<20):
				n+=1
				print(n)
				contador+=1
			else: #else para o while	
				print(f"Total de sucessores = {contador}")
		else: #else para o if
			print("O numero tinha que ser menor do que 10. ")	


if __name__=="__main__":
	#script1()
	#script2b()
	#script3()
	script4()
