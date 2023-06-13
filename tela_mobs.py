import pygame

# Importando estados
from config import FECHAR, NO_CHAO, PULANDO, SALA_MOBS, MAPA_MOBS, FPS, PRETO, VEL_CORRER, GRAVIDADE, ALTURA, NA_PLATAFORMA

# Importando classes
from sprites import Jogador, Tile

# Importando chaves de assets
from assets import load_assets, ACIDO, CENARIO_BASE, ND

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
    all_tiros = pygame.sprite.Group()

    # Adicionando ao dicionário groups
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiles'] = all_tiles
    groups['all_acido'] = all_acido
    groups['all_blocos'] = all_blocos
    groups['all_tiros'] = all_tiros

    # Criando o jogador
    player = Jogador(groups, assets, 100, ALTURA - 50)
    all_sprites.add(player)

    # Criando tiles
    for linha in range (len(MAPA_MOBS)):
        for coluna in range (len(MAPA_MOBS[linha])):
            tipo_tile = MAPA_MOBS[linha][coluna]
            tile = Tile(assets[tipo_tile], linha, coluna)
            all_tiles.add(tile)

            if tipo_tile == ACIDO:
                all_acido.add(tile)
            elif tipo_tile != ND:
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
            
             # Só verifica o teclado se está no estado de jogo
            if state == SALA_MOBS:

                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:

                    # Dependendo da tecla, altera a velocidade do anzol e da linha.
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

                        # Se o player estiver pulando ou não
                        player.speedx -= VEL_CORRER
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

                    # Dependendo da tecla, altera a velocidade do anzol e da linha.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_d:
                            player.speedx -= VEL_CORRER
                        if event.key == pygame.K_a:
                            player.speedx += VEL_CORRER

        # Se colidir com a plataforma    
        colisoes = pygame.sprite.spritecollide(player, all_blocos, False)

        # Para cada colisão
        if len(colisoes) > 0:
            # Definindo uma colisão
            colisao = colisoes[0]

            # Definindo limites dos blocos
            esquerda_bloco = colisao.rect.left
            direita_bloco = colisao.rect.right

            # Se o player colidir de baixo para cima
            if player.rect.bottom > colisao.rect.bottom:
                player.rect.top = colisao.rect.bottom
                player.speedy = 0
            
            # Se o player colidir de cima para baixo
            else:
                player.rect.bottom = colisao.rect.top
                player.speedy = 0
                player.state = NA_PLATAFORMA

                # Atualizando imagem do jogador
                if player.orientacao == 'direita':
                    player.image = assets[JOGADOR_DIREITA_IMG]
                
                else:
                    player.image = assets[JOGADOR_ESQUERDA_IMG]
            
            # Impedindo que o player entre em um loop de colisões
            colisoes = []

        if player.state == NA_PLATAFORMA:
            if player.rect.right <= esquerda_bloco or player.rect.left >= direita_bloco:
                player.state = PULANDO
        
        if player.rect.right >= 875:
            state = SALA_MOBS

        # ----- Atualiza estado do jogo
        # Atualizando a posição do jogador
        player.update(state)
        all_tiros.update()
    
    # ----- Atualiza estado do jogo
        player.update(state)
        all_tiros.update()

        # ----- Gera saídas
        tela.fill(PRETO)
        tela.blit(assets[CENARIO_BASE], (0, 0))

        # Desenhando os tiles, os personagens e o fundo
        all_tiles.draw(tela)
        all_sprites.draw(tela)

        pygame.display.update()

    return state
