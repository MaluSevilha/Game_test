# Importando bibliotecas
import pygame

# Importando arquivos
from config import FECHAR, INSTRUCAO, SALA_MOBS, FPS, VEL_CORRER, PRETO, PULANDO, GRAVIDADE, NA_PLATAFORMA, ALTURA
from config import VERMELHO
from sprites import Jogador, Plataforma
from assets import load_assets, toca_musica, CENARIO_INSTRUCAO, COMANDOS, FONTE

# Importando imagens do jogador
from assets import JOGADOR_DIREITA_IMG, JOGADOR_ESQUERDA_IMG, JOGADOR_PULA_DIREITA_IMG, JOGADOR_PULA_ESQUERDA_IMG

# Importando chaves das assets
from assets import CENARIO_INIT, INICIO_SOM, DESLIGANDO_LUZ

def tela_instrucao(tela):
    # Toca a musica principal
    # toca_musica('assets/sons/under_the_sea.mp3')

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    # Carregando o dicionário assets
    assets = load_assets()

    # Criando grupos
    all_sprites = pygame.sprite.Group()
    all_plataformas = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()

    # Adicionando ao dicionário groups
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiles'] = all_plataformas
    groups['all_tiros'] = all_tiros

    # Criando o jogador
    player = Jogador(groups, assets, 100, ALTURA - 59)
    all_sprites.add(player)

    # Criando plataforma
    plataforma = Plataforma(groups, assets)
    all_sprites.add(plataforma)
    all_plataformas.add(plataforma)

    # Variáveis necessárias para o jogo
    keys_down = {}
    vidas = 3
    state = INSTRUCAO

    # ===== Loop Principal =====
    while state != FECHAR and state != SALA_MOBS:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = FECHAR

            # Só verifica o teclado se está no estado de jogo
            if state == INSTRUCAO:

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
        colisoes = pygame.sprite.spritecollide(player, all_plataformas, False)

        # Para cada colisão
        if len(colisoes) > 0:
            # Se o player colidir de baixo para cima
            if player.rect.bottom > plataforma.rect.bottom:
                player.rect.top = plataforma.rect.bottom
                player.speedy += GRAVIDADE
            
            # Se o player colidir de cima para baixo
            else:
                player.rect.bottom = plataforma.rect.top
                player.speedy = 0
                player.state = NA_PLATAFORMA

                # Atualizando imagem do jogador
                if player.orientacao == 'direita':
                    player.image = assets[JOGADOR_DIREITA_IMG]
                
                else:
                    player.image = assets[JOGADOR_ESQUERDA_IMG]

        if player.state == NA_PLATAFORMA:
            if player.rect.right <= plataforma.rect.left or player.rect.left >= plataforma.rect.right:
                player.state = PULANDO
                player.speedy += GRAVIDADE
        
        if player.rect.right >= 875:
            state = SALA_MOBS

        # ----- Atualiza estado do jogo
        # Atualizando a posição do jogador
        player.update(state)
        all_tiros.update()

        # ----- Gera saídas
        tela.fill(PRETO)                                # Preenche com a cor preta
        tela.blit(assets[CENARIO_INSTRUCAO], (0, 0))
        tela.blit(assets[COMANDOS], (0,0))
        
        # ----- Coloca as vidas na tela 
        text_surface = assets[FONTE].render(chr(9829) * vidas, True, VERMELHO)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, ALTURA - 10)
        tela.blit(text_surface, text_rect)

        # Desenhando sprites
        all_sprites.draw(tela)

        # Atualiza o display
        pygame.display.update()                         # Mostra o novo frame para o jogador
    
    return state
