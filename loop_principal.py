# Importando bibliotecas usadas
import pygame

# Importando variáveis e funções de outros arquivos
from config import LARGURA, ALTURA, INICIO, FECHAR, GANHOU, SALA_MOBS, INSTRUCAO, SALA_BOSS
from tela_inicial import tela_inicial
from tela_vitoria import tela_vitoria
from tela_instrucao import tela_instrucao
from tela_mobs import tela_mobs

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Não apague a luz')


# ----- Loop Principal
state = INICIO
while state != FECHAR:
    # Começa a tela de início
    if state == INICIO:
        state = tela_inicial(tela)
    
    # Abre a sala de instrução
    elif state == INSTRUCAO:
        state = tela_instrucao(tela)

    # Abre a sala dos mobs
    elif state == SALA_MOBS:
        state = tela_mobs(tela)
    
    # Abre a sala do boss
    elif state == SALA_BOSS:
        state = FECHAR
    
    # Abre a tela de vitória
    elif state == GANHOU:
        state = tela_vitoria(tela)

    # # Abre a tela de Game Over
    # elif state == MORTO:
    #     lista_return = game_over(window)

    # Encerra o pygame
    else:
        state = FECHAR

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados