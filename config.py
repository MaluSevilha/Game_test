# Importando bibliotecas usadas
from os import path

# Estabelece o caminho que contem as figuras, sons e fontes

# Dados gerais do jogo.
WIDTH = 500     # Largura da tela
HEIGHT = 600    # Altura da tela
FPS = 60        # Frames por segundo

# Estados para controle do fluxo da aplicação
MORTO = -1
INICIO = 0
FECHAR = 1
JOGANDO = 2
INSTRUCAO = 3