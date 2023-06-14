import pygame

# Importando biblioteca de aleatoriedade
import random

# Importando funções
from assets import load_assets, toca_musica

# Importando estados
from config import MORTO, FECHAR, PRETO, FPS, INICIO

# Importando chaves
from assets import CENARIO_GAMEOVER, JUMPSCARE

def game_over(tela):
        
    assets = load_assets()
    state = MORTO
    
    # Toca música do game over
    # toca_musica('assets/sons/som_game_over.mp3')

    # Colocando background
    tela.fill(PRETO)
    tela.blit(assets[CENARIO_GAMEOVER], (0,0))

    # Depois inverte o display.
    pygame.display.flip()

    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # ===== Loop principal =====
    rodando = True
    while rodando and state != FECHAR:

        # Ajusta a velocidade do jogo.
        relogio.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc)
        for event in pygame.event.get():
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                state = FECHAR
                rodando = False

            # Verifica se pressionou uma tecla
            if event.type == pygame.KEYDOWN:
                # Verifica se pressionou espaço
                if event.key == pygame.K_SPACE:
                    # Pegando o instante do click em espaço
                    espaco = pygame.time.get_ticks()

                    # Tirando um número aleatório
                    chance = random.randint(0, 100)

                    # 5% de chance de dar um jumpscare
                    if chance < 5:
                        # Tempo passado
                        tempo = (pygame.time.get_ticks() - espaco)/1000

                        # Tirando jumpscare
                        while tempo < 2.5:
                            # Mudando a tela conforme o tempo
                            if tempo <= 2:
                                # Colocando tela preta
                                tela.fill(PRETO)
                            else:  
                                # Colocando jumpscare
                                tela.fill(PRETO)
                                tela.blit(assets[JUMPSCARE], (0,0))

                            # Depois inverte o display.
                            pygame.display.flip()

                            # Atualiza o tempo
                            tempo = (pygame.time.get_ticks() - espaco)/1000
                    
                    # Voltando ao início
                    state = INICIO
                    rodando = False

    # Retornando o estado
    return state