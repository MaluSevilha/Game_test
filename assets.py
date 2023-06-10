# Importando bibliotecas necessárias
import pygame
from os import path

# Importando tamanho da tela
from config import WIDTH, HEIGHT

# Importando caminhos
from config import CENARIOS_DIR

# Definindo chaves do dicionário assets
# ---- Cenários
CENARIO_INIT = 'background'

# Função que cria o dicionário assets
def load_assets():
    
    # Criando o dicionário assets e adicionando as imagens à ele
    assets = {}

    assets[CENARIO_INIT] = pygame.image.load(path.join(CENARIOS_DIR, 'cenario_ini.png')).convert()
    assets[CENARIO_INIT] = pygame.transform.scale(assets[CENARIO_INIT], (WIDTH, HEIGHT))

    return assets

# def toca_musica(file, volume = 0.5, loop = -1):
#     pygame.mixer.music.load(path.join(file))
#     pygame.mixer.music.set_volume(volume)
#     pygame.mixer.music.play(loop)