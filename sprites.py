import pygame
from assets import JOGADOR_DIREITA_IMG
from config import ALTURA_JOGADOR, LARGURA_JOGADOR, ALTURA

class jogador(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Definindo a imagem da vara
        self.image = assets[JOGADOR_DIREITA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        # ---- Vara
        self.rect = self.image.get_rect()
        self.rect.centerx =  LARGURA_JOGADOR / 2
        self.rect.bottom = ALTURA_JOGADOR - 10

        # Cria variáveis da vara e grupos
        self.speedy = 0
        self.speedx = 0
        self.groups = groups
        self.assets = assets
    
    def update(self):
        # Atualização da posição da vara
        self.rect.y += self.speedy
        self.rect.x += self.speedy

        # Mantem dentro da tela
        if self.rect.top + ALTURA_JOGADOR - 10 < 0:
            self.rect.bottom = 10
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA