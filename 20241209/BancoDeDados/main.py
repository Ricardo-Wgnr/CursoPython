#coding: utf-8
import sqlite3 as sq

def criarBancoDados():
    conexao = sq.connect('funcionarios.db')
    cursor = conexao.cursor()
    return conexao, cursor

def criarTabela():
    tabela = """CREATE TABLE IF NOT EXISTS funcionarios (id INTEGER PRIMARY KEY,nome TEXT NOT NULL,cargo TEXT NOT NULL,dataContratacao TEXT NOT NULL);"""
    return tabela

def inserirDados(conexao, cursor,i):
    nome = input('Nome: ')
    cargo = input('Cargo: ')
    dataContratacao = input('Data de Contratacao: ')
    cursor.execute("INSERT INTO funcionarios VALUES (?,?,?,?)", (i,nome,cargo,dataContratacao))
    conexao.commit()

if __name__ == '__main__':
    conexao, cursor = criarBancoDados()
    tabela = criarTabela()
    conexao.execute(tabela)
    conexao.commit()
    for i in range(2):
        inserirDados(conexao, cursor,i)


