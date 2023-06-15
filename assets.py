# Importando bibliotecas necessárias
import pygame
from os import path

# Importando tamanho da tela e de compoentes
from config import LARGURA, ALTURA, LARGURA_JOGADOR, ALTURA_JOGADOR, TILE, ALTURA_INIMIGO, LARGURA_INIMIGO

# Importando caminhos
from config import CENARIOS_DIR, SND_DIR, JOGADOR_DIR, TILES_DIR, PLATAFORMA_DIR, INIMIGO_DIR, FONTE_DIR

# Definindo chaves do dicionário assets
# ---- Cenários
CENARIO_INIT = 'cenario inicio'
COMANDOS = 'comando'
CENARIO_VITORIA = 'cenario vitoria'
CENARIO_INSTRUCAO = 'cenario instrução'
CENARIO_BASE = 'cenario base'
CENARIO_GAMEOVER = 'cenario gameover'
JUMPSCARE_IMG = 'jumpscare img'

# ---- Tiles
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

# ---- Plataforma para instruções
PLATAFORMA_BASE = 'plataforma instruções'

# ---- Bala
BALA_IMG = 'imagem bala'

# ---- Sons
INICIO_SOM = 'soundtrack inicial'
VITORIA_SOM = 'soundtrack_vitoria'
GAMEOVER_SOM = 'soundtrack gameover'

# ---- Efeitos sonoros
DESLIGANDO_LUZ = 'desligando luz'
JUMPSCARE_SOM = 'jumpscare snd'
PULO_SOM = 'pulo som'
TIRO_SOM = 'tiro som'
MORTE_SOM = 'morte som'
DANO_INIMIGO_SOM = 'dano_inimigo'
MORTE_INIMIGO_SOM = 'morte inimigo som'

# ---- Jogador
JOGADOR_DIREITA_IMG = 'jogador direita'
JOGADOR_PULA_DIREITA_IMG = 'jogador pular direita'

JOGADOR_ESQUERDA_IMG = 'jogador esquerda'
JOGADOR_PULA_ESQUERDA_IMG = 'jogador pular esquerda'

# ---- Inimigo
INIMIGO_IMG = 'inimigo img'
TIRO_INIMIGO_IMG = 'tiro inimigo'

# ---- Fonte
FONTE = 'fonte'

# Função que cria o dicionário assets
def load_assets():
    
    # Criando o dicionário assets e adicionando as imagens à ele
    assets = {}

    # Carregando imagens dentro do dicionário
    # ---- Cenários
    assets[CENARIO_INIT] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_ini.png')).convert()
    assets[CENARIO_INIT] = pygame.transform.scale(assets[CENARIO_INIT], (LARGURA, ALTURA))
    assets[COMANDOS] = pygame.image.load(path.join(CENARIOS_DIR, 'comandos_instrucao.png')).convert()
    assets[COMANDOS] = pygame.transform.scale(assets[COMANDOS], (0.8*760, 0.8*375))

    assets[CENARIO_VITORIA] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_vitoria.png')).convert()
    assets[CENARIO_VITORIA] = pygame.transform.scale(assets[CENARIO_VITORIA], (LARGURA, ALTURA))

    assets[CENARIO_BASE] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_principal.png')).convert()
    assets[CENARIO_BASE] = pygame.transform.scale(assets[CENARIO_BASE], (LARGURA, ALTURA))

    assets[CENARIO_INSTRUCAO] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_instrucao.png')).convert()
    assets[CENARIO_INSTRUCAO] = pygame.transform.scale(assets[CENARIO_INSTRUCAO], (LARGURA, ALTURA))

    assets[CENARIO_GAMEOVER] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_gameover.png')).convert()
    assets[CENARIO_GAMEOVER] = pygame.transform.scale(assets[CENARIO_GAMEOVER], (LARGURA, ALTURA))

    assets[JUMPSCARE_IMG] = pygame.image.load(path.join(CENARIOS_DIR, 'jumpscare.png')).convert()
    assets[JUMPSCARE_IMG] = pygame.transform.scale(assets[JUMPSCARE_IMG], (LARGURA, ALTURA))

    # ---- Plataforma Instrução
    assets[PLATAFORMA_BASE] = pygame.image.load(path.join(PLATAFORMA_DIR, 'plataforma_teste.png')).convert_alpha()
    assets[PLATAFORMA_BASE] = pygame.transform.scale(assets[PLATAFORMA_BASE], (5*TILE, TILE))

    # ---- Bala
    assets[BALA_IMG] = pygame.image.load(path.join(PLATAFORMA_DIR, 'bala.png')).convert_alpha()
    assets[BALA_IMG] = pygame.transform.scale(assets[BALA_IMG], (15, 7.5))

    # ---- Tiles
    assets[BASE] = pygame.image.load(path.join(TILES_DIR, 'chao_basico.png')).convert_alpha()
    assets[BASE] = pygame.transform.scale(assets[BASE], (TILE, TILE))
    assets[BASE_FUNDA] = pygame.image.load(path.join(TILES_DIR, 'chao_profundo.png')).convert_alpha()
    assets[BASE_FUNDA] = pygame.transform.scale(assets[BASE_FUNDA], (TILE, TILE))

    assets[DIR] = pygame.image.load(path.join(TILES_DIR, 'chao_dir_max.png')).convert_alpha()
    assets[DIR] = pygame.transform.scale(assets[DIR], (TILE, TILE))
    assets[QUINA_DIR] = pygame.image.load(path.join(TILES_DIR, 'chao_dir_quina.png')).convert_alpha()
    assets[QUINA_DIR] = pygame.transform.scale(assets[QUINA_DIR], (TILE, TILE))
    assets[LADO_DIR] = pygame.image.load(path.join(TILES_DIR, 'direita_borda.png')).convert_alpha()
    assets[LADO_DIR] = pygame.transform.scale(assets[LADO_DIR], (TILE, TILE))

    assets[ESQ] = pygame.image.load(path.join(TILES_DIR, 'chao_esq_max.png')).convert_alpha()
    assets[ESQ] = pygame.transform.scale(assets[ESQ], (TILE, TILE))
    assets[QUINA_ESQ] = pygame.image.load(path.join(TILES_DIR, 'chao_esq_quina.png')).convert_alpha()
    assets[QUINA_ESQ] = pygame.transform.scale(assets[QUINA_ESQ], (TILE, TILE))
    assets[LADO_ESQ] = pygame.image.load(path.join(TILES_DIR, 'esquerda_borda.png')).convert_alpha()
    assets[LADO_ESQ] = pygame.transform.scale(assets[LADO_ESQ], (TILE, TILE))

    assets[ACIDO] = pygame.image.load(path.join(TILES_DIR, 'acido.png')).convert_alpha()
    assets[ACIDO] = pygame.transform.scale(assets[ACIDO], (TILE, TILE))
    assets[ACIDO_FUNDO] = pygame.image.load(path.join(TILES_DIR, 'acido_profundo.png')).convert_alpha()
    assets[ACIDO_FUNDO] = pygame.transform.scale(assets[ACIDO_FUNDO], (TILE, TILE))

    assets[ND] = pygame.image.load(path.join(TILES_DIR, 'vazio.png')).convert_alpha()
    assets[ND] = pygame.transform.scale(assets[ND], (TILE, TILE))

    # ---- Jogador
    assets[JOGADOR_DIREITA_IMG] = pygame.image.load(path.join(JOGADOR_DIR, 'toad_direita.png')).convert_alpha()
    assets[JOGADOR_DIREITA_IMG] = pygame.transform.scale(assets[JOGADOR_DIREITA_IMG], (LARGURA_JOGADOR, ALTURA_JOGADOR))

    assets[JOGADOR_PULA_DIREITA_IMG] = pygame.image.load(path.join(JOGADOR_DIR, 'toad_pula_direita.png')).convert_alpha()
    assets[JOGADOR_PULA_DIREITA_IMG] = pygame.transform.scale(assets[JOGADOR_PULA_DIREITA_IMG], (LARGURA_JOGADOR, ALTURA_JOGADOR))

    assets[JOGADOR_ESQUERDA_IMG] = pygame.image.load(path.join(JOGADOR_DIR, 'toad_esquerda.png')).convert_alpha()
    assets[JOGADOR_ESQUERDA_IMG] = pygame.transform.scale(assets[JOGADOR_ESQUERDA_IMG], (LARGURA_JOGADOR, ALTURA_JOGADOR))

    assets[JOGADOR_PULA_ESQUERDA_IMG] = pygame.image.load(path.join(JOGADOR_DIR, 'toad_pula_esquerda.png')).convert_alpha()
    assets[JOGADOR_PULA_ESQUERDA_IMG] = pygame.transform.scale(assets[JOGADOR_PULA_ESQUERDA_IMG], (LARGURA_JOGADOR, ALTURA_JOGADOR))

    # ---- Inimigo
    assets[TIRO_INIMIGO_IMG] = pygame.image.load(path.join(INIMIGO_DIR, 'tiro_inimigo.png')).convert_alpha()
    assets[TIRO_INIMIGO_IMG] = pygame.transform.scale(assets[TIRO_INIMIGO_IMG], (60, 30))

    assets[INIMIGO_IMG] = []
    for i in range(5):
        arquivo = 'inimigo_' + str(i) + '.png'
        imagem = pygame.image.load(path.join(INIMIGO_DIR, arquivo)).convert_alpha()
        imagem = pygame.transform.scale(imagem, (LARGURA_INIMIGO, ALTURA_INIMIGO))
        assets[INIMIGO_IMG].append(imagem)

    # ---- Fonte
    # Juntando a fonte do score à ele
    assets[FONTE] = pygame.font.Font(path.join(FONTE_DIR, 'PressStart2P.ttf'), 28)

    # Carregando efeitos sonoros dentro do dicionário
    assets[DESLIGANDO_LUZ] = pygame.mixer.Sound(path.join(SND_DIR, 'desligando_luz.mp3'))
    assets[JUMPSCARE_SOM] = pygame.mixer.Sound(path.join(SND_DIR, 'jumpscare.mp3'))
    assets[MORTE_SOM] = pygame.mixer.Sound(path.join(SND_DIR, 'morte.mp3'))

    assets[PULO_SOM] = pygame.mixer.Sound(path.join(SND_DIR, 'pulo.mp3'))
    assets[PULO_SOM].set_volume(0.2)

    assets[TIRO_SOM] = pygame.mixer.Sound(path.join(SND_DIR, 'tiro.mp3'))
    assets[TIRO_SOM].set_volume(0.2)

    assets[DANO_INIMIGO_SOM] = pygame.mixer.Sound(path.join(SND_DIR, 'dano_inimigo.mp3'))
    assets[DANO_INIMIGO_SOM].set_volume(0.35)

    assets[MORTE_INIMIGO_SOM] = pygame.mixer.Sound(path.join(SND_DIR, 'morte_inimigo.mp3'))
    assets[MORTE_INIMIGO_SOM].set_volume(0.5)

    # Carregando nos soundtracks dentro do dicionário
    assets[INICIO_SOM] = path.join(SND_DIR, 'soundtrack_init.mp3')
    assets[VITORIA_SOM] = path.join(SND_DIR, 'soundtrack_vitoria.mp3')
    assets[GAMEOVER_SOM] = path.join(SND_DIR, 'soundtrack_gameover.mp3')

    # Retorna o dicionários com as assets
    return assets

def toca_musica(file, volume = 0.5, loop = -1):
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)