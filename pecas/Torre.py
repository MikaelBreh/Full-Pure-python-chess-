from Pecas import Pecas

class Torre(Pecas):
    def __init__(self):
        self.nome = 'Torre'
        self.emoji = '♜'
        self.proporcaoX = 1
        self.proporcaoY = 0
        self.podeVoltar = True
        self.distanciaIlimitada = True

