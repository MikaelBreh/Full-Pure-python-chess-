
tabuleiro = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],\
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],\
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],\
            ['♜', '♞', '♝', '♚', '♛', '♝', '♞', '♜']


def mostrarTabuleiroUsuario(tabuleiro):
    letrasLateral = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # Imprimir tabuleiro para o usuario no formato: letra da Coluna | casa |...
    for linha in range(8):
        print(f'{letrasLateral[linha]}  ', end="")
        for pecas in range(8):
            print('|', end="")
            if tabuleiro[linha][pecas] == ' ':
                print(pecas, end="")
            else:
                print(tabuleiro[linha][pecas], end="")
            if pecas == 7:
                print('|')



def moverPeca(tabuleiro):

    # Validar se a letra da coluna digitada (a-h) existe -
    # Parte 1 da Validacao: Esta dentro do tabuleiro
    def validarLetra(entrada):
        for letra in range(8):
            if entrada[0] == letrasLateral[letra]:
                return True
                break

    # Validar se numero da casa digitada (0-7) existe -
    # Parte 2 da Validacao: Esta dentro do tabuleiro
    def validarNumero(entrada):
        for numero in range(8):
            if int(entrada[1]) == numero:
                return True
                break

    # Verificar qual numero coluna (0-7) representa
    # a letra digitada pelo usuario (a-h)
    def validarLetraeRetornarNumero(entrada):
        for letra in range(8):
            if entrada[0] == letrasLateral[letra]:
                return letra
                break

    def validarMovimento(peca, posicaoInicial, posicaoFinal):

        def validarTorre():
            # Verificar se a coluna Inicial da Torre é a mesma da coluna Final ou
            # se a linha Inicial é a mesma da Linha Final
            # Validar tambem a rainha pois ela pode fazer o mesmo movimento da torre
            if peca == '♖' or peca == '♜' or peca == '♕' or peca == '♛':
                if posicaoInicial[0] == posicaoFinal[0] or posicaoInicial[1] == posicaoFinal[1]:
                    return True

        def validarBispo():
            # Verificar se quando se move 1 na coluna, tambem se move 1 na linha
            # ex: sempre que o bispo se move na posicao x ele precisa se mover a
            # mesma quantidade na posicao y
            # Validar tambem a rainha pois ela pode fazer o mesmo movimento do bispo
            if peca == '♗' or peca == '♝' or peca == '♕' or peca == '♛':
                diferencaQuantLetras = validarLetraeRetornarNumero(posicaoInicial) -\
                                       validarLetraeRetornarNumero(posicaoFinal)
                if int(posicaoInicial[1]) - int(posicaoFinal[1]) == diferencaQuantLetras\
                    or int(posicaoInicial[1]) - int(posicaoFinal[1]) == diferencaQuantLetras*-1:
                    return True

        def validarCavalo():
            # A logica do cavalo é que sempre que ele se mover 2x ele deve mover 1y
            # sempre que ele se mover 1x deve se mover 2y
            if peca == '♘' or peca == '♞':
                # Retornar quantas letras (colunas) o cavalo se moveu
                diferencaQuantLetras = validarLetraeRetornarNumero(posicaoInicial) -\
                                       validarLetraeRetornarNumero(posicaoFinal)

                # Retornar quantos Numeros (linhas) o cavalo se moveu
                diferencaQuantNumeros = int(posicaoInicial[1]) - int(posicaoFinal[1])

                # Validar se o cavalo se moveu 2 letras (colunas) ele tambem deve se mover 1 numero (linha)
                if diferencaQuantLetras == 2 or diferencaQuantLetras == -2:
                    if diferencaQuantNumeros == 1 or diferencaQuantNumeros == -1:
                        return True
                # Validar se o cavalo se moveu 1 letras (colunas) ele tambem deve se mover 2 numero (linha)
                elif diferencaQuantLetras == 1 or diferencaQuantLetras == -1:
                    if diferencaQuantNumeros == 2 or diferencaQuantNumeros == -2:
                        return True

        def validarRei():
            if peca == '♔' or peca == '♚':
                # Validar movimento similar ao da torre, porem se movendo apenas uma casa
                if posicaoInicial[0] == posicaoFinal[0] or posicaoInicial[1] == posicaoFinal[1]:
                    diferencaNum = int(posicaoInicial[1]) - int(posicaoFinal[1])
                    diferencaLetra = validarLetraeRetornarNumero(posicaoInicial) - \
                                     validarLetraeRetornarNumero(posicaoFinal)

                    if diferencaNum == 1 or diferencaNum == -1 or diferencaLetra == 1 or diferencaLetra == -1:
                        return True
                    else:
                        print('rei nao pode se mover mais de 1')

                # Validar movimento similar ao bispo, porem se movendo apenas uma casa em x e uma em y
                diferencaQuantLetras = validarLetraeRetornarNumero(posicaoInicial) - \
                                       validarLetraeRetornarNumero(posicaoFinal)
                if int(posicaoInicial[1]) - int(posicaoFinal[1]) == diferencaQuantLetras \
                        or int(posicaoInicial[1]) - int(posicaoFinal[1]) == diferencaQuantLetras * -1:
                    if diferencaQuantLetras == 1 or diferencaQuantLetras == -1:
                        return True
                    else:
                        print('rei nao pode se mover mais de 1 na diagonal')



        if validarTorre() == True or validarBispo() == True or validarCavalo() == True or validarRei() == True:
            return True



    # Letras que representam a Coluna
    letrasLateral = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # While que vai executar ate o jogo acabar, validando cada jogada
    while True:
        # Entrada do usuario de peça que deseja selecionar
        localSelecionado = input('\nDigite linha e depois numero da casa. Ex a1:  ').lower()
        # Entrada do usuario de para onde ele deseja levar a peça
        localMover = input('Digite o local para mover. Ex: c1.  ou digite: voltar:   ').lower()

        # Verificar se entrada de localMover é igual a voltar, se for voltar para a entrada localSelecionado
        # Se alguma das entradas for maior que 2 caracteres voltar tambem, pois segue o padrao coluna:casa (ex: A1)
        if localMover != 'voltar' and len(localSelecionado) < 3 and len(localMover) < 3:
            if validarLetra(localSelecionado) == True and validarLetra(localMover) == True and\
                validarNumero(localSelecionado) == True and validarNumero(localMover) == True:

                for listaLetras in range(8):
                    if localSelecionado[0] == letrasLateral[listaLetras]:
                        # Atribuir a peca a ser movida a uma variavel para mudarmos o lugar dela no tabuleiro
                        pecaMovida = tabuleiro[listaLetras][int(localSelecionado[1])]

                        # Se a peça que foi escolhida fez o movimento correto, será validado aqui
                        if validarMovimento(tabuleiro[listaLetras][int(localSelecionado[1])],
                                            localSelecionado, localMover) == True:

                            # Mudar local onde a peça foi selecionada e deixar vazio
                            tabuleiro[listaLetras][int(localSelecionado[1])] = ' '

                            for listaLetras1 in range(8):
                                if localMover[0] == letrasLateral[listaLetras1]:
                                    tabuleiro[listaLetras1][int(localMover[1])] = pecaMovida
                                    break

                            print(mostrarTabuleiroUsuario(tabuleiro))

            else:
                print('entrada incorreta')





mostrarTabuleiroUsuario(tabuleiro)
moverPeca(tabuleiro)














