#coding: utf-8

class Computador(object):

    def __init__(self):
        self.placaV = None
        self.memoria = None
        self.marca = None
        self.set_computador()

    def set_computador(self):
        self.marca = input("Digite a marca do computador: ")
        self.memoria = input("Digite a quantidade de memória: ")
        self.placaV = input("Digite a placa de vídeo: ")

    def get_computador(self):
        print("Marca do computador:", self.marca)
        print("Memória do computador:", self.memoria)
        print("Placa de vídeo do computador:", self.placaV)

A = Computador()
A.get_computador()
