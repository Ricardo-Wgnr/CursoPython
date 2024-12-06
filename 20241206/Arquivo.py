#coding: utf-8

class Arquivo(object):
    def __init__(self, cor, departamento, numMaxPastas):
        self.cor = cor
        self.departamento = departamento
        self.numMaxPastas = numMaxPastas
        self.estado = False
        self.pastas = []

    def receberPasta(self, pasta):
        self.pastas.append(pasta)
        self.estado = True

    def getPastas(self):
        for pasta in self.pastas:
            print(pasta.getPasta())

    def getArquivo(self):
        return self.cor, self.departamento, self.numMaxPastas

