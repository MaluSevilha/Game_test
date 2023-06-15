import pygame

def tela_boss(tela):
    import pygame
import random

# Importando estados
from config import FECHAR, PULANDO, SALA_BOSS, MORTO, GANHOU

# Importando variáveis relevantes
from config import ALTURA, VEL_CORRER, MAPA_BOSS, FPS, VERMELHO, PRETO

# Importando classes
from sprites import Jogador, Tile, Inimigo

# Importando chaves de assets
from assets import load_assets, ACIDO, ACIDO_FUNDO, ND, FONTE, CENARIO_BASE

# Importando imagens dos jogadores
from assets import JOGADOR_DIREITA_IMG, JOGADOR_ESQUERDA_IMG, JOGADOR_PULA_DIREITA_IMG, JOGADOR_PULA_ESQUERDA_IMG

# Importando chaves de assets

def tela_boss(tela):
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
    all_tiros_boss = pygame.sprite.Group()

    # Adicionando ao dicionário groups
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiles'] = all_tiles
    groups['all_acido'] = all_acido
    groups['all_blocos'] = all_blocos
    groups['all_tiros'] = all_tiros
    groups['all_tiros_boss'] = all_tiros_boss

    # Criando o jogador
    player = Jogador(groups, assets, 20, ALTURA - 50)
    all_sprites.add(player)

    # Criando tiles
    for linha in range (len(MAPA_BOSS)):
        for coluna in range (len(MAPA_BOSS[linha])):
            tipo_tile = MAPA_BOSS[linha][coluna]
            tile = Tile(assets[tipo_tile], linha, coluna)
            all_tiles.add(tile)

            if tipo_tile == ACIDO or tipo_tile == ACIDO_FUNDO:
                all_acido.add(tile)
            elif tipo_tile != ND:
                all_blocos.add(tile)

    # Variáveis necessárias para o jogo
    keys_down = {}
    vidas = 3
    score = 0
    player_vivo = True

    # ===== Loop principal =====
    state = SALA_BOSS
    while state != FECHAR and state != GANHOU and state != MORTO:
        # Relógio
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica se fechou o jogo
            if event.type == pygame.QUIT:
                state = FECHAR
            
             # Só verifica o teclado se está no estado de jogo
            if state == SALA_BOSS:

                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:

                    # Dependendo da tecla, altera a velocidade do player
                    keys_down[event.key] = True
                    if event.key == pygame.K_w:
                        player.pular()
                    
                    if event.key == pygame.K_d:
                        # ----- Orientação
                        player.orientacao = 'direita'

                        # Atualizado velocidade
                        player.speedx += VEL_CORRER

                        # Se o player estiver pulando ou não
                        if player.state == PULANDO:
                            player.image = assets[JOGADOR_PULA_DIREITA_IMG]
                        else:
                            player.image = assets[JOGADOR_DIREITA_IMG]
                    
                    if event.key == pygame.K_a:
                        # ----- Orientação
                        player.orientacao = 'esquerda'

                        # Atualizado a velocidade
                        player.speedx -= VEL_CORRER

                        # Se o player estiver pulando ou não
                        if player.state == PULANDO:
                            player.image = assets[JOGADOR_PULA_ESQUERDA_IMG]
                        else:
                            player.image = assets[JOGADOR_ESQUERDA_IMG]
                
                # Se clicou com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Se clicou com o botão esquerdo
                    if event.button == 1:
                        player.atirar()
                    
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:

                    # Se a tecla não estiver no dicionário
                    if event.key not in keys_down:
                        keys_down[event.key] = False
                    
                    # Dependendo da tecla, altera a velocidade do anzol e da linha.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_d:
                            player.speedx -= VEL_CORRER
                        if event.key == pygame.K_a:
                            player.speedx += VEL_CORRER
    
            # ----- Atualiza estado do jogo
        player.update(state)
        all_tiros.update()
        all_tiros_boss.update()

        # ----- Gera saídas
        tela.fill(PRETO)
        tela.blit(assets[CENARIO_BASE], (0, 0))

        # Desenhando os tiles, os personagens e o fundo
        # ----- Coloca personagens
        all_sprites.draw(tela)

        # ----- Tiles
        all_tiles.draw(tela)

        # ----- Coloca as vidas na tela 
        text_surface = assets[FONTE].render(chr(9829) * vidas, True, VERMELHO)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, ALTURA - 10)
        tela.blit(text_surface, text_rect)

        # Inverte o display
        pygame.display.update()

    return state