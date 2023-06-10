# Importando bibliotecas
import pygame

# Importando arquivos
from config import FPS, JOGANDO, FECHAR, PRETO, ESPERA, GANHOU
from assets import load_assets, CENARIO_INIT

# Fazendo a função da tela do jogo
def tela_inicial(tela):

    # Toca a música inicial

    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # Background da tela inicial
    assets = load_assets()

    # ----- Loop principal
    # pygame.mixer.music.play(loops = -1)
    
    rodando = True
    while rodando:
        # Define um estado inicial 
        state = ESPERA

        # Ajusta a velocidade do jogo.
        relogio.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = FECHAR
                rodando = False
            
            # Verifica se uma tecla foi pressionada
            if event.type == pygame.KEYUP:
                state = JOGANDO
                rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(assets[CENARIO_INIT], (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
        # Confere se é para mudar de tela
        if state == JOGANDO:
            # Define que deve haver uma pausa
            pausa = True

            # Cria um loop para rodar segunda tela de início
            while pausa:
                # Tempo inicial
                tempo_inicial = pygame.time.get_ticks()

                # Tempo de espera
                sec = (pygame.time.get_ticks() - tempo_inicial)/1000

                # Quando passa o tempo
                if sec >= 1:
                    pausa = False

                # Coloca a imagem seguinte da raposa pulando na água
                tela.fill(PRETO)

                # Inverte o display
                pygame.display.flip()
        
        elif state == ESPERA:
            # Quanto tempo o jogador está esperando
            qnt_tempo = pygame.time.get_ticks()/1000

            # Confere se esperou 5 minutos
            if qnt_tempo >= 300:
                state = GANHOU
                rodando = False

    # Retorna o estado
    return state