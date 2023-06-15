import pygame
import random

# Importando estados
from config import FECHAR, PULANDO, SALA_MOBS, SALA_BOSS, NA_PLATAFORMA, MORTO

# Importando variáveis relevantes
from config import ALTURA, VEL_CORRER, MAPA_MOBS, FPS, PRETO

# Importando classes
from sprites import Jogador, Tile, Inimigo

# Importando chaves de assets
from assets import load_assets, ACIDO, ACIDO_FUNDO, CENARIO_BASE, ND, MORTE_SOM

# Importando imagens dos jogadores
from assets import JOGADOR_DIREITA_IMG, JOGADOR_ESQUERDA_IMG, JOGADOR_PULA_DIREITA_IMG, JOGADOR_PULA_ESQUERDA_IMG

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
    all_inimigos = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()
    all_tiros_inimigos = pygame.sprite.Group()

    # Adicionando ao dicionário groups
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiles'] = all_tiles
    groups['all_acido'] = all_acido
    groups['all_blocos'] = all_blocos
    groups['all_tiros'] = all_tiros
    groups['all_inimigos'] = all_inimigos
    groups['all_tiros_inimigo'] = all_tiros_inimigos

    # Criando o jogador
    player = Jogador(groups, assets, 20, ALTURA - 50)
    all_sprites.add(player)

    # Criando inimigos
    # ---- Velocidades das balas
    velocidades_balas = [10, 9, 8]

    # ---- Posicionando os inimigos
    posicoes = [(305, 535), (599, 384), (494, 155), (846, 231), (815, 610)]

    # Colocando cada inimigo em uma posição
    for posicao in posicoes:
        # Definindo variáveis do inimigo
        x = posicao[0]
        y = posicao[1]
        vel_bala = random.choice(velocidades_balas)

        # Criando o inimigo
        inimigo = Inimigo(groups, assets, x, y, vel_bala)

        # Adicionando-o aos seus grupos
        all_sprites.add(inimigo)
        all_inimigos.add(inimigo)

    # Criando tiles
    for linha in range (len(MAPA_MOBS)):
        for coluna in range (len(MAPA_MOBS[linha])):
            tipo_tile = MAPA_MOBS[linha][coluna]
            tile = Tile(assets[tipo_tile], linha, coluna)
            all_tiles.add(tile)

            if tipo_tile == ACIDO or tipo_tile == ACIDO_FUNDO:
                all_acido.add(tile)
            elif tipo_tile != ND:
                all_blocos.add(tile)

    # Variáveis necessárias para o jogo
    keys_down = {}
    vidas = 3
    player_vivo = True
    state = SALA_MOBS

    while state != FECHAR and state != SALA_BOSS and state != MORTO:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica se fechou o jogo
            if event.type == pygame.QUIT:
                state = FECHAR
            
             # Só verifica o teclado se está no estado de jogo
            if state == SALA_MOBS:

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

        # Se colidir com a plataforma    
        colisoes_tiles = pygame.sprite.spritecollide(player, all_blocos, False)

        # Para cada colisão
        if len(colisoes_tiles) > 0:
            # Definindo uma colisão
            colisao = colisoes_tiles[0]

            # Definindo limites dos blocos
            esquerda_bloco = colisao.rect.left
            direita_bloco = colisao.rect.right

            # Se o player colidir de baixo para cima
            if player.rect.bottom > colisao.rect.bottom:
                player.rect.top = colisao.rect.bottom
                player.speedy = 0
            
            # Se o player colidir de cima para baixo
            elif player.rect.top < colisao.rect.top:
                player.rect.bottom = colisao.rect.top
                player.speedy = 0
                player.state = NA_PLATAFORMA

                # Atualizando imagem do jogador
                if player.orientacao == 'direita':
                    player.image = assets[JOGADOR_DIREITA_IMG]
                
                else:
                    player.image = assets[JOGADOR_ESQUERDA_IMG]
            
            # Impedindo que o player entre em um loop de colisões
            colisoes_tiles = []
        
        # Conferindo se colidiu no ácido
        colisao_acido = pygame.sprite.spritecollide(player, all_acido, False)

        # Tirando uma vida caso esteja em contato com ácido 
        if len(colisao_acido) > 0:
            # Perdendo uma vida
            vidas -= 1

            # Matando o jogador
            player.kill()

            # Tocando som de morte
            assets[MORTE_SOM].play()

            # Recriando o jogador
            if vidas > 0:
                player_vivo = False
            
            # Impedindo que tire mais de uma vez 
            colisao_acido = []

        colisao_tiros = pygame.sprite.spritecollide(player, all_tiros_inimigos, True)
        # Tirando uma vida caso esteja em contato com uma bala do inimigo 
        if len(colisao_tiros) > 0:
            # Perdendo uma vida
            vidas -= 1

            # Matando o jogador
            player.kill()

            # Tocando som de morte
            assets[MORTE_SOM].play()

            # Recriando o jogador
            if vidas > 0:
                player_vivo = False
            
            # Impedindo que tire mais de uma vez 
            colisao_tiros = []
        
        colisao_inimigos = pygame.sprite.spritecollide(player, all_inimigos, False)
        # Tirando uma vida caso esteja em contato com um inimigo 
        if len(colisao_inimigos) > 0:
            # Perdendo uma vida
            vidas -= 1

            # Matando o jogador
            player.kill()

            # Tocando som de morte
            assets[MORTE_SOM].play()

            # Recriando o jogador
            if vidas > 0:
                player_vivo = False
            
            # Impedindo que tire mais de uma vez 
            colisao_inimigos = []
        
        # Se o jogador está sem vidas
        if vidas < 0:
            state = MORTO
        # Se o jogador possui vidas
        else:
            # Recriando o jogador, caso esse tenha morrido
            if player_vivo == False:
                # Recriando o jogador
                player = Jogador(groups, assets, 20, ALTURA - 50)
                all_sprites.add(player)
                player_vivo = True

                # Dando reestart nas teclas apertadas
                keys_down = {}
        
        # Conferindo se o jogador saiu da plataforma
        if player.state == NA_PLATAFORMA:
            if player.rect.right <= esquerda_bloco or player.rect.left >= direita_bloco:
                player.state = PULANDO

        # Se o jogador aravessou a sala
        if player.rect.right >= 875:
            state = SALA_BOSS
    
        # ----- Atualiza estado do jogo
        player.update(state)
        all_tiros.update()
        all_tiros_inimigos.update()
        all_inimigos.update()

        # ----- Gera saídas
        tela.fill(PRETO)
        tela.blit(assets[CENARIO_BASE], (0, 0))

        # Desenhando os tiles, os personagens e o fundo
        all_tiles.draw(tela)
        all_sprites.draw(tela)

        pygame.display.update()

    return state
