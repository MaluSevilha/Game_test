# Importando bibliotecas
import pygame

# Importando arquivos
from config import FECHAR, INSTRUCAO, FPS, VEL_CORRER, PRETO, PULANDO
from sprites import jogador
from assets import load_assets, toca_musica, CENARIO_INSTRUCAO

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
    all_tiles = pygame.sprite.Group()
    all_vidas = pygame.sprite.Group()

    # Adicionando ao dicionário groups
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_vidas'] = all_vidas
    groups['all_tiles'] = all_tiles

    # Criando o jogador
    player = jogador(groups, assets)
    all_sprites.add(player)

    # Variáveis necessárias para o jogo
    keys_down = {}
    score = 0
    vidas = 3
    state = INSTRUCAO

    # ===== Loop Principal =====
    while state != FECHAR:
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

                    
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:

                    # Dependendo da tecla, altera a velocidade do anzol e da linha.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_d:
                            player.speedx -= VEL_CORRER
                        if event.key == pygame.K_a:
                            player.speedx += VEL_CORRER
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos sprites
        all_sprites.update(state)

        # ----- Gera saídas
        tela.fill(PRETO)                                # Preenche com a cor preta
        tela.blit(assets[CENARIO_INSTRUCAO], (0, 0))

        # Desenhando sprites
        all_sprites.draw(tela)

        # Atualiza o display
        pygame.display.update()                         # Mostra o novo frame para o jogador
    
    return state
