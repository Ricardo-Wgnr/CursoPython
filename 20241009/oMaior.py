#coding: utf-8

entrada = input()

a, b, c = entrada.split(" ")

a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b))/2
maiorABC = int((maiorAB+c+abs(maiorAB-c))/2)

print("{0} eh o maior".format(maiorABC))