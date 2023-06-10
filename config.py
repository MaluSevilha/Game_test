# Importando bibliotecas usadas
from os import path

# Estabelece o caminho que contem as figuras, sons e fontes
CENARIOS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'cenarios')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'sons')

# Dados gerais do jogo.
WIDTH = 600     # Largura da tela
HEIGHT = 500    # Altura da tela
FPS = 60        # Frames por segundo

# Cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Estados para controle do fluxo da aplicação
MORTO = -1
INICIO = 0
FECHAR = 1
JOGANDO = 2
ESPERA = 3
GANHOU = 4