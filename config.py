# Importando bibliotecas usadas
from os import path

# Estabelece o caminho que contem as figuras, sons e fontes
CENARIOS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'cenarios')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'sons')
TILES_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'tiles')
JOGADOR_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'jogador')
PLATAFORMA_DIR = path.join(path.dirname(__file__), 'assets', 'imagens')

# Dados gerais do jogo.
LARGURA = 900            # Largura da tela
ALTURA = 750             # Altura da tela
LARGURA_JOGADOR = 37.5   # Largura do jogador
ALTURA_JOGADOR = 45      # Altura do jogador
TILE = 38              # Tamanho de um tile [37,5 x 37,5]
FPS = 60                 # Frames por segundo

# Velocidades para o jogo
VEL_CORRER = 5
VEL_PULO = 20
GRAVIDADE = 1

# Chaves para os tiles
BASE = 'grama base'
DIR = 'grama direita'
QUINA_DIR = 'quina direita'
ESQ = 'grama esquerda'
QUINA_ESQ = 'quina esquerda'
ND = 'vazio'
ACIDO = 'acido'

# Criando mapas para tiles [24x20]
MAPA_MOBS = [
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, ESQ, BASE, BASE, BASE, DIR, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, ESQ, BASE, BASE],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [BASE, BASE, DIR, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, ESQ, BASE, BASE, DIR, QUINA_DIR, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, QUINA_ESQ, ESQ, BASE, BASE, BASE, DIR, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, ESQ, BASE, BASE, BASE],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [BASE, BASE, BASE, BASE, DIR, QUINA_DIR, ACIDO, ACIDO, ACIDO, ACIDO, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ACIDO, ACIDO, ACIDO, ACIDO, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND]
]

MAPA_BOSS = [
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND]
]

# Cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Estados para controle do fluxo da aplicação
# ---- Estados para encerramento do jogo
MORTO = -1
FECHAR = 1

# ---- Estados para a abertura das salas
SALA_BOSS = 2
SALA_MOBS = 6
INSTRUCAO = 5
INICIO = 0

# ---- Estado para definir o que o usuário está fazendo no início
ESPERA = 3
GANHOU = 4

# ---- Estados para acompanhar o jogador
NO_CHAO = 7
PULANDO = 8 
NA_PLATAFORMA = 9