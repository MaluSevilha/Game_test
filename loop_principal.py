# Importando bibliotecas usadas
import pygame

# Importando variáveis e funções de outros arquivos
from config import WIDTH, HEIGHT, INICIO, FECHAR, MORTO, JOGANDO, INSTRUCAO

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fishing Fox')


# ----- Loop Principal
state = INICIO
while state != FECHAR:
    # Começa a tela de início
    if state == INICIO:
        state = tela_inicial(window)

    # # Abre a tela de instruções
    # elif state == INSTRUCAO:
    #     lista_return = instrucao(window)
    #     state = lista_return

    # # Abre a tela do jogo
    # elif state == JOGANDO:
    #     lista_return = game_screen(window)

    # # Abre a tela de Game Over
    # elif state == MORTO:
    #     lista_return = game_over(window)

    # # Encerra o pygame
    # else:
    #     state = FECHAR

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados