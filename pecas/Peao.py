from Pecas import Pecas

class Torre(Pecas):
    def __init__(self):
        self.nome = 'Peao'
        self.emoji = '♟'
        self.proporcaoX = 0
        self.proporcaoY = 1
        self.podeVoltar = False
        self.distanciaIlimitada = False

