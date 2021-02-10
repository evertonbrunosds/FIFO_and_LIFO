from Pilha import Pilha
from Fila import Fila

class Main():
    @staticmethod
    def main():
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.empilhar('B')
        pilha.empilhar('C')
        pilha.empilhar('D')
        while (not pilha.estaVazia()):
            print('Elemento da PILHA: ' + pilha.desempilhar())
        print('---------------------------------------')
        fila = Fila()
        fila.inserir('A')
        fila.inserir('B')
        fila.inserir('C')
        fila.inserir('D')
        while (not fila.estaVazia()):
            print('Elemento da FILA: ' + fila.remover())

Main.main()