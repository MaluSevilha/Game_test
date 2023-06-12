import pygame
from assets import JOGADOR_DIREITA_IMG, JOGADOR_ESQUERDA_IMG, JOGADOR_PULA_DIREITA_IMG, JOGADOR_PULA_ESQUERDA_IMG, PLATAFORMA_BASE
from config import INSTRUCAO, ALTURA, LARGURA, VEL_PULO, NO_CHAO, PULANDO, GRAVIDADE

class Jogador(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Definindo a imagem da vara
        self.image = assets[JOGADOR_DIREITA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        self.rect = self.image.get_rect()

        # Posiciona o jogador
        self.rect.centerx = 100
        self.rect.bottom = ALTURA - 59

        # Cria variáveis do jogador e grupos
        # ----- Velocidade
        self.speedy = 0
        self.speedx = 0

        # ----- Orientações
        self.orientacao = 'direita'

        # ----- Estado e grupos
        self.state = NO_CHAO
        self.groups = groups
        self.assets = assets
    
    def update(self, state):
        # Atualização da posição do jogador
        # ----- No eixo y
        if self.state == PULANDO:
            self.speedy += GRAVIDADE
        else:
            self.speedy = 0
        self.rect.y += self.speedy

        # ----- No eixo x
        self.rect.x += self.speedx

        # Mantem dentro da tela
        # ----- No eixo X
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        
        # ---- No eixo y
        # Caso esteja na tela de instruções
        if state == INSTRUCAO:
            # Embaixo
            if self.rect.bottom > ALTURA - 59:
                # Definindo imagem com base na orientação
                if self.orientacao == 'direita':
                    self.image = self.assets[JOGADOR_DIREITA_IMG]
                else:
                    self.image = self.assets[JOGADOR_ESQUERDA_IMG]

                # Redefinindo posição
                self.rect.bottom = ALTURA - 59

                # Mudando o estado
                self.state = NO_CHAO
            # Em cima
            if self.rect.top < 0:
                self.rect.top = 0

    def pular(self):
        # Só pode pular quando estiver em contato com o chão
        if self.state != PULANDO:
            if self.orientacao == 'direita':
                self.image = self.assets[JOGADOR_PULA_DIREITA_IMG]
            else:
                self.image = self.assets[JOGADOR_PULA_ESQUERDA_IMG]
            self.speedy -= VEL_PULO
            self.state = PULANDO

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Definindo a imagem da vara
        self.image = assets[PLATAFORMA_BASE]
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        self.rect = self.image.get_rect()

        # Posiciona o jogador
        self.rect.centerx = 500
        self.rect.bottom = 3*ALTURA / 4

        # ----- Grupos
        self.groups = groups
        self.assets = assets