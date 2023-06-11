# Importando bibliotecas necessárias
import pygame
from os import path

# Importando tamanho da tela
from config import LARGURA, ALTURA, LARGURA_JOGADOR, ALTURA_JOGADOR

# Importando caminhos
from config import CENARIOS_DIR, SND_DIR, JOGADOR_DIR

# Definindo chaves do dicionário assets
# ---- Cenários
CENARIO_INIT = 'cenario inicio'
CENARIO_VITORIA = 'cenario vitoria'
CENARIO_INSTRUCAO = 'cenario instrução'
CENARIO_BASE = 'cenario base'

# ---- Sons
INICIO_SOM = 'soundtrack inicial'
VITORIA_SOM = 'soundtrack_vitoria'

# ---- Efeitos sonoros
DESLIGANDO_LUZ = 'desligando luz'

# ---- Jogador
JOGADOR_DIREITA_IMG = 'jogador direita'
JOGADOR_PULA_DIREITA_IMG = 'jogador pular direita'

JOGADOR_ESQUERDA_IMG = 'jogador esquerda'
JOGADOR_PULA_ESQUERDA_IMG = 'jogador pular esquerda'

# Função que cria o dicionário assets
def load_assets():
    
    # Criando o dicionário assets e adicionando as imagens à ele
    assets = {}

    # Carregando imagens dentro do dicionário
    assets[CENARIO_INIT] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_ini.png')).convert()
    assets[CENARIO_INIT] = pygame.transform.scale(assets[CENARIO_INIT], (LARGURA, ALTURA))

    assets[CENARIO_VITORIA] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_vitoria.png')).convert()
    assets[CENARIO_VITORIA] = pygame.transform.scale(assets[CENARIO_VITORIA], (LARGURA, ALTURA))

    assets[CENARIO_BASE] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_principal.png')).convert()
    assets[CENARIO_BASE] = pygame.transform.scale(assets[CENARIO_VITORIA], (LARGURA, ALTURA))

    assets[CENARIO_INSTRUCAO] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_instrucao.png')).convert()
    assets[CENARIO_INSTRUCAO] = pygame.transform.scale(assets[CENARIO_VITORIA], (LARGURA, ALTURA))

    assets[JOGADOR_DIREITA_IMG] = pygame.image.load(path.join(JOGADOR_DIR), 'toad_direita.png')
    assets[JOGADOR_DIREITA_IMG] = pygame.transform.scale(assets[CENARIO_INIT], (LARGURA_JOGADOR, ALTURA_JOGADOR))

    assets[JOGADOR_PULA_DIREITA_IMG] = pygame.image.load(path.join(JOGADOR_DIR), 'toad_pula_direita.png')
    assets[JOGADOR_PULA_DIREITA_IMG] = pygame.transform.scale(assets[CENARIO_INIT], (LARGURA_JOGADOR, ALTURA_JOGADOR))

    assets[JOGADOR_ESQUERDA_IMG] = pygame.image.load(path.join(JOGADOR_DIR), 'toad_esquerda.png')
    assets[JOGADOR_ESQUERDA_IMG] = pygame.transform.scale(assets[CENARIO_INIT], (LARGURA_JOGADOR, ALTURA_JOGADOR))

    assets[JOGADOR_PULA_ESQUERDA_IMG] = pygame.image.load(path.join(JOGADOR_DIR), 'toad_pula_esquerda.png')
    assets[JOGADOR_PULA_ESQUERDA_IMG] = pygame.transform.scale(assets[CENARIO_INIT], (LARGURA_JOGADOR, ALTURA_JOGADOR))

    # Carregando efeitos sonoros dentro do dicionário
    assets[DESLIGANDO_LUZ] = pygame.mixer.Sound(path.join(SND_DIR, 'desligando_luz.mp3'))

    # Carregando nos soundtracks dentro do dicionário
    assets[INICIO_SOM] = path.join(SND_DIR, 'soundtrack_init.mp3')
    assets[VITORIA_SOM] = path.join(SND_DIR, 'soundtrack_vitoria.mp3')

    # Retorna o dicionários com as assets
    return assets

def toca_musica(file, volume = 0.5, loop = -1):
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)