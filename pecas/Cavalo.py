from Pecas import Pecas

class Cavalo(Pecas):
    def __init__(self):
        self.nome = 'Cavalo'
        self.emoji = '♞'
        self.proporcaoX = 1
        self.proporcaoY = 2
        self.podeVoltar = True
        self.distanciaIlimitada = False

