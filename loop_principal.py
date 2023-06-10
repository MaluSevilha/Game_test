# Importando bibliotecas usadas
import pygame

# Importando variáveis e funções de outros arquivos
from config import WIDTH, HEIGHT, INICIO, FECHAR, GANHOU, JOGANDO
from tela_inicial import tela_inicial

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Não apague a luz')


# ----- Loop Principal
state = INICIO
while state != FECHAR:
    # Começa a tela de início
    if state == INICIO:
        state = tela_inicial(tela)

    # Abre a tela do jogo
    elif state == JOGANDO:
        # state = tela_jogando(window)
        pygame.quit() 
    
    # Abre a tela do jogo
    elif state == GANHOU:
        # state = tela_vitoria(window)
        pygame.quit() 

    # # Abre a tela de Game Over
    # elif state == MORTO:
    #     lista_return = game_over(window)

    # Encerra o pygame
    else:
        state = FECHAR

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados