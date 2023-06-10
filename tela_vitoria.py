# Importando bibliotecas usadas
import pygame

# Importando variáveis de outros arquivos
from config import PRETO, FPS, INICIO, FECHAR, GANHOU
from assets import load_assets, toca_musica, CENARIO_VITORIA, VITORIA_SOM

# Criando função da tela de game over
def tela_vitoria(tela):
    # Definindo estado e importando as assets
    state = GANHOU
    assets = load_assets()
    
    # Toca música do game over
    toca_musica(assets[VITORIA_SOM])

    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # Background da tela inicial
    background = assets[CENARIO_VITORIA]

    # ----- Loop principal 
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

            # Verifica se clicou espaço
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = INICIO
                        rodando = False
        
        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(background, (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    # Retornando o estado
    return state