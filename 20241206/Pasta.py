#coding: utf-8
import time as t
import datetime as dt

class Pasta(object):
    def __init__(self):
        self.identificacao = ""
        self.documentos = {}
        self.conteudo = ""
        self.estado = 0 # 0 = vazia, 1 com doc

    def criarPastaVazia(self):
        self.identificacao = input("Identificacao da pasta: ")
        self.identificacao = str(int(t.time())) #momento unix
        self.conteudo = input("Conteudo: ")
        self.estado = 0

    def getIdentificacao(self):
        print("id = ", self.identificacao)
        print("conteudo = ", self.conteudo)

    def receberArquivo(self):
        endereco = dt.datetime.now()
        nomeArquivo = input("Entre com o nome do arquivo: ")
        if self.documentos.get(nomeArquivo) == None:
            self.documentos[nomeArquivo] = endereco
            self.estado = 1
        else:
            print("Documento ja esta contido na pasta")

    def getDocumentos(self):
        if self.estado == 1:
            print("Relacao dos arquvios na pasta: ", self.identificacao)
            for chave, valor in self.documentos.items():
                print("\t chave =", chave, "valor =", valor)
        else:
            print("Pasta vazia")

    def removeDocumento(self):
        arquivo = input("Entre com o nome do arquivo a remover: ")
        docRemovido = None
        if self.documentos.get(arquivo) != None:
            docRemovido = self.documentos.pop(arquivo)
        else:
            print(f"Documento {arquivo} nao encontrado")
        return docRemovido

    def getPasta(self):
        return self.identificacao, self.conteudo, self.estado, self.documentos
