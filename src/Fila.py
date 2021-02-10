class Elo():
    def __init__(self, elemento):
        self.elemento = elemento
        self.eloAnterior = None
        self.eloPosterior = None
    def pegarElemento(self):
        return self.elemento
    def pegarEloAnterior(self):
        return self.eloAnterior
    def pegarEloPosterior(self):
        return self.eloPosterior
    def alterarEloAnterior(self, eloAnterior):
        if (eloAnterior == None):
            self.alterarEloAnterior = None
        else:
            self.eloAnterior = eloAnterior
            eloAnterior.eloPosterior = self
    def alterarEloPosterior(self, eloPosterior):
        if (eloPosterior == None):
            self.eloPosterior = None
        else:
            self.eloPosterior = eloPosterior
            eloPosterior.eloAnterior = self

class Fila():
    def __init__(self):
        self.primeiroElo = None
        self.ultimoElo = None
    def estaVazia(self):
        return self.primeiroElo == None
    def inserir(self, elemento):
        novoElo = Elo(elemento)
        if (self.estaVazia()):
            self.primeiroElo = novoElo
        else:
            self.ultimoElo.alterarEloPosterior(novoElo)
        self.ultimoElo = novoElo
    def remover(self):
        if (self.estaVazia()):
            return None
        else:
            elemento = self.primeiroElo.pegarElemento()
            self.primeiroElo = self.primeiroElo.pegarEloPosterior()
            if (self.estaVazia()):
                self.ultimoElo = None
            else:
                self.primeiroElo.alterarEloAnterior(None)
            return elemento