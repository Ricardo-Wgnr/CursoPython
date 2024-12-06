import Pasta as p
import Arquivo as arq

if __name__ == "__main__":
    Pasta1 = p.Pasta()
    Pasta1.criarPastaVazia()
    Pasta1.getIdentificacao()
    for _ in range(3):
        Pasta1.receberArquivo()
    Pasta1.getDocumentos()

    arquivo = arq.Arquivo("vermelho", "mat", "10")
    print(arquivo.getArquivo())
    arquivo.receberPasta(Pasta1)
    arquivo.getPastas()