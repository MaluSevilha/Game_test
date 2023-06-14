import pygame
from assets import JOGADOR_DIREITA_IMG, JOGADOR_ESQUERDA_IMG, PULO_SOM
from assets import JOGADOR_PULA_DIREITA_IMG, JOGADOR_PULA_ESQUERDA_IMG, PLATAFORMA_BASE, BALA_IMG
from config import INSTRUCAO, ALTURA, LARGURA, VEL_PULO, NO_CHAO, PULANDO, GRAVIDADE, ALTURA_JOGADOR, TILE

class Bala(pygame.sprite.Sprite):
    # Construtor da classe
    def __init__(self, assets, centery, centerx, player):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Imagem da bala
        self.image = assets[BALA_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = centery

        # Para velocidade da bala
        if player.orientacao == 'direita':
            self.speedx = 10 
        else:
            self.speedx = - 10

    def update(self):
        # A bala só se move no eixo y
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.left < 0 or self.rect.right > LARGURA:
            self.kill()

class Jogador(pygame.sprite.Sprite):
    def __init__(self, groups, assets, posx, posy):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Definindo a imagem da vara
        self.image = assets[JOGADOR_DIREITA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        self.rect = self.image.get_rect()

        # Posiciona o jogador
        self.rect.centerx = posx
        self.rect.bottom = posy

        # Cria variáveis do jogador e grupos
        # ----- Atirar
        self.ultimo_tiro = pygame.time.get_ticks()
        self.tempo_tiro = 300

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
        
        else:
            # Em cima
            if self.rect.top < 0:
                self.rect.top = 0

    def pular(self):
        # Só pode pular quando estiver em contato com o chão
        if self.state != PULANDO:
            # Atualiza a imagem
            if self.orientacao == 'direita':
                self.image = self.assets[JOGADOR_PULA_DIREITA_IMG]
            else:
                self.image = self.assets[JOGADOR_PULA_ESQUERDA_IMG]
            
            # ATualiza o estado e a velocidade [no eixo y]
            self.speedy -= VEL_PULO
            self.state = PULANDO

            # Toca o som de pulo
            self.assets[PULO_SOM].play()
    
    def atirar(self):
        # Verifica se pode atirar
        agora = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde o último tiro.
        tempo_passado = agora - self.ultimo_tiro

        # Se já pode atirar novamente...
        if tempo_passado > self.tempo_tiro:
            # Marca o tick da nova imagem.
            self.ultimo_tiro = agora

            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            novo_tiro = Bala(self.assets, self.rect.centery, self.rect.centerx, self)
            self.groups['all_sprites'].add(novo_tiro)
            self.groups['all_tiros'].add(novo_tiro)
            # self.assets[TIRO_SND].play()

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

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile
        tile_img = pygame.transform.scale(tile_img, (TILE, TILE))

        # Define a imagem do tile
        self.image = tile_img

        # Define o rect do tile
        self.rect = self.image.get_rect()

        # Posiciona o tile com base na linha e coluna passada no "MAP"
        self.rect.x = TILE * column
        self.rect.y = TILE * row