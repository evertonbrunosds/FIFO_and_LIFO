class Elo():
    def __init__(self, elemento, eloAnterior):
        self.elemento = elemento
        self.eloAnterior = eloAnterior
    def pegarElemento(self):
        return self.elemento
    def pegarEloAnterior(self):
        return self.eloAnterior

class Pilha():
    def __init__(self):
        self.ultimoElo = None
    def estaVazia(self):
        return self.ultimoElo == None
    def empilhar(self, elemento):
        self.ultimoElo = Elo(elemento, self.ultimoElo)
    def desempilhar(self):
        if (self.estaVazia()):
            return None
        else:
            elemento = self.ultimoElo.pegarElemento()
            self.ultimoElo = self.ultimoElo.pegarEloAnterior()
            return elemento