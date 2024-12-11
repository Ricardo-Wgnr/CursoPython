#coding: utf-8
import ComportaVedacao
import AlavancaAcionamento
import ValvulaAlimentacao
import time

class CaixaAcoplada(object):
    def __init__(self):
        self.nivelAgua = 0
        self.estado = 0 #0 vazio, 1 cheio
        self.nivelMax = 5.0 #valor em litros
        self.vazao = 0.5 #vazao = 0.5 litros/s
        self.nivelMin = 0.5
        self.vazaoSaida = 0.9

    def acionarBotao(self):
        pass

    def encherCaixa(self):
        print("Caixa enchendo..., volume inicial =", self.nivelAgua)
        while(self.nivelAgua < self.nivelMax):
            self.nivelAgua += self.vazao
            time.sleep(0.5)
            print("Nivel de agua =", self.nivelAgua)
        self.estado = 1

    def esvaziarCaixa(self):
        print("Caixa esvaziando..., volume inicial =", self.nivelAgua)
        while(self.nivelAgua > self.nivelMin):
            self.nivelAgua -= self.vazaoSaida
            time.sleep(0.5)
            print("Nivel de agua =", self.nivelAgua)
        self.estado = 0

    def getEstado(self):
        return self.estado