# Importando bibliotecas
import pygame

# Importando arquivos
from config import FPS, FECHAR, PRETO, ESPERA, GANHOU, INSTRUCAO
from assets import load_assets, toca_musica

# Importando chaves das assets
from assets import CENARIO_INIT, INICIO_SOM, DESLIGANDO_LUZ

# Fazendo a função da tela do jogo
def tela_inicial(tela):
    # Começo da função
    tempo_comeco = pygame.time.get_ticks()

    # Carrega o dicionário assets
    assets = load_assets()

    # Toca a música inicial
    toca_musica(assets[INICIO_SOM])

    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # ===== Loop principal =====
    pygame.mixer.music.play(loops = -1)
    
    rodando = True
    while rodando:
        # Define um estado inicial 
        state = ESPERA

        # Ajusta a velocidade do jogo.
        relogio.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                state = FECHAR
                rodando = False
            
            # Verifica se uma tecla foi pressionada
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Parando a música e tocando efeito sonoro
                assets[DESLIGANDO_LUZ].play()
                pygame.mixer.music.stop()

                # Mudando estados
                state = INSTRUCAO
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
            qnt_tempo = (pygame.time.get_ticks() - tempo_comeco)/1000

            # Confere se esperou 5 minutos
            if qnt_tempo >= 300:
                state = GANHOU
                rodando = False

    # Retorna o estado
    return state