import pygame

from config import FECHAR, MORTO, SALA_MOBS, MAPA_MOBS, FPS, PRETO
from sprites import Jogador, Tile
from assets import load_assets, ACIDO, CENARIO_BASE

# Importando chaves de assets


def tela_mobs(tela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Importando as assets 
    assets = load_assets()
    
    # Criando grupos
    all_sprites = pygame.sprite.Group()
    all_tiles = pygame.sprite.Group()
    all_acido = pygame.sprite.Group()
    all_blocos = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()

    # Adicionando ao dicionário groups
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiles'] = all_tiles
    groups['all_acido'] = all_acido
    groups['all_blocos'] = all_blocos
    groups['all_tiros'] = all_tiros

    # Criando o jogador
    # player = Jogador(groups, assets)
    # all_sprites.add(player)

    # Criando tiles
    for linha in range (len(MAPA_MOBS)):
        for coluna in range (len(MAPA_MOBS[linha])):
            tipo_tile = MAPA_MOBS[linha][coluna]
            tile = Tile(assets[tipo_tile], linha, coluna)
            all_tiles.add(tile)

            if tipo_tile == ACIDO:
                all_acido.add(tile)
            else:
                all_blocos.add(tile)

    # Variáveis necessárias para o jogo
    keys_down = {}
    vidas = 3
    state = SALA_MOBS

    while state != FECHAR:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica se fechou o jogo
            if event.type == pygame.QUIT:
                state = FECHAR
    
    # ----- Atualiza estado do jogo
        all_sprites.update()

        # ----- Gera saídas
        tela.fill(PRETO)
        tela.blit(assets[CENARIO_BASE], (0, 0))

        # Desenhando os tiles, os personagens e o fundo
        all_tiles.draw(tela)
        all_sprites.draw(tela)

        pygame.display.update()

    return state
