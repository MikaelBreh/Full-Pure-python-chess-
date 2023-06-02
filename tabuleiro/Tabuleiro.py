class Tabuleiro():
    def __init__(self):
        BASELINHA = [0] * 8
        self.matrixTabuleiro = [(BASELINHA)]*8

    def mostrarTabuleiro(self):
        for linha in range(8):
                print(self.matrixTabuleiro[linha])

