#-*- coding: utf-8 -*-

t_str= "Eu gosto de Python. "
t2_str = "Vamos estudar python. "
#abertura e gravacao
ft=open("ArqTexto.dat","w")
ft.write(t_str)
ft.write("\n")
ft.write(t2_str)
ft.write("\n")
ft.close()

t3_str = "Append. "
ft2 = open("ArqTexto.dat","a")
ft2.write(t3_str)
ft2.write("\n")
ft2.close()

#Abertura e leitura
ft2 = open("ArqTexto.dat","r")
linhas = ft2.readlines()
ft2.close()
#Impressão
for i in range(len(linhas)):
    print(linhas[i],end = "")
print()