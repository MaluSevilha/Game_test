import pygame
from assets import JOGADOR_DIREITA_IMG
from config import ALTURA_JOGADOR, LARGURA_JOGADOR, ALTURA, LARGURA, VEL_PULO, NO_CHAO, PULANDO, GRAVIDADE

class jogador(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Definindo a imagem da vara
        self.image = assets[JOGADOR_DIREITA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        self.rect = self.image.get_rect()
        self.rect.centerx =  LARGURA_JOGADOR / 2
        self.rect.bottom = ALTURA_JOGADOR - 10

        # Cria variáveis do jogador e grupos
        self.speedy = 0
        self.speedx = 0
        self.state = NO_CHAO
        self.groups = groups
        self.assets = assets
    
    def update(self):
        # Atualização da posição da vara
        self.rect.y += self.speedy
        self.rect.x += self.speedy
        self.speedy += GRAVIDADE

        # Mantem dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA
        elif self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
        elif self.rect.top < 0:
            self.rect.top = 0

    def pular(self):
        if self.state == NO_CHAO:
            self.speedy -= VEL_PULO
            self.state = PULANDO