# Importando bibliotecas usadas
from os import path

# Estabelece o caminho que contem as figuras, sons e fontes
CENARIOS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'cenarios')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'sons')
FONTE_DIR = path.join(path.dirname(__file__), 'assets', 'fonte')
TILES_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'tiles')
JOGADOR_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'jogador')
INIMIGO_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'inimigos') 
ADICIONAIS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens')
VIDA_BOSS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'boss_vida')

# Dados gerais do jogo.
TILE = 38                   # Tamanho de um tile [37,5 x 37,5]
FPS = 60                    # Frames por segundo
LARGURA = 900               # Largura da tela
ALTURA = 750                # Altura da tela
LARGURA_JOGADOR = 37.5      # Largura do jogador
ALTURA_JOGADOR = 45         # Altura do jogador
LARGURA_INIMIGO = 37.5      # Largura do inimigo
ALTURA_INIMIGO = 45         # Altura inimigo   
LARGURA_BOSS = 316        # Largura do boss
ALTURA_BOSS = 250         # Altura do boss

# Velocidades para o jogo
VEL_CORRER = 5
VEL_PULO = 20
GRAVIDADE = 1

# Chaves para os tiles
BASE = 'grama base'
BASE_FUNDA = 'base funda'
DIR = 'grama direita'
QUINA_DIR = 'quina direita'
LADO_DIR = 'lado direita'
ESQ = 'grama esquerda'
QUINA_ESQ = 'quina esquerda'
LADO_ESQ = 'lado esquerda'
ND = 'vazio'
ACIDO = 'acido'
ACIDO_FUNDO = 'acido fundo'

# Criando mapas para tiles [24x20]
MAPA_MOBS = [
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, BASE, BASE, BASE, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, BASE, BASE, DIR],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ESQ, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, BASE, BASE, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, QUINA_ESQ, BASE, BASE, BASE, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, BASE, BASE, BASE, DIR],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [BASE, BASE, BASE, BASE, BASE, QUINA_DIR, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO],
    [BASE_FUNDA, BASE_FUNDA, BASE_FUNDA, BASE_FUNDA, BASE_FUNDA, LADO_DIR, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO]
]

MAPA_BOSS = [
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ESQ, BASE, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, QUINA_ESQ, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, QUINA_ESQ, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ESQ, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, QUINA_ESQ, BASE, BASE, QUINA_DIR, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND, ND],
    [BASE, BASE, BASE, BASE, BASE, QUINA_DIR, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO, ACIDO],
    [BASE_FUNDA, BASE_FUNDA, BASE_FUNDA, BASE_FUNDA, BASE_FUNDA, LADO_DIR, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO, ACIDO_FUNDO]
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