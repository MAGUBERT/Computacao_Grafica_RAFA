import pygame
import sys
import random

pygame.init()

largura = 1000
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGUINHO ALEATÓRIO')

PRETO = (0, 0, 0)
tamanho_fonte = 40 
fonte = pygame.font.SysFont("Arial", tamanho_fonte, bold=True)

def cor_aleatoria(diferente_de=None):
    while True:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if c != diferente_de:
            return c

def velocidade():
    return random.randint(3,10)

texto1_conteudo = "MATHEUS"
texto1_cor = cor_aleatoria()
texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
texto1_rect = texto1.get_rect(center=(largura//3, altura//2))
v1x = velocidade()
v1y = velocidade()

texto2_conteudo = "GUBERT"
texto2_cor = cor_aleatoria(diferente_de=texto1_cor)
texto2 = fonte.render(texto2_conteudo, True, texto2_cor)
texto2_rect = texto2.get_rect(center=(2*largura//3, altura//2))
v2x = velocidade()
v2y = velocidade()

clock = pygame.time.Clock()

def movimento(rect, vx, vy):
    rect.x += vx
    rect.y += vy
    bateu = False
    
    if rect.left <= 0:
        rect.left = 0
        vx = abs(velocidade())
        bateu = True
    elif rect.right >= largura:
        rect.right = largura
        vx = -abs(velocidade())
        bateu = True
        
    if rect.top <= 0:
        rect.top = 0
        vy = abs(velocidade())
        bateu = True
    elif rect.bottom >= altura:
        rect.bottom = altura
        vy = -abs(velocidade())
        bateu = True
        
    return vx, vy, bateu

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    v1x, v1y, bateu1 = movimento(texto1_rect, v1x, v1y)
    v2x, v2y, bateu2 = movimento(texto2_rect, v2x, v2y)

    if bateu1:
        texto1_cor = cor_aleatoria(texto1_cor)
        texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
    if bateu2:
        texto2_cor = cor_aleatoria(texto2_cor)
        texto2 = fonte.render(texto2_conteudo, True, texto2_cor)

    if texto1_rect.colliderect(texto2_rect):
        v1x, v1y = -v1x, -v1y
        v2x, v2y = -v2x, -v2y
        
        texto1_cor = cor_aleatoria(texto1_cor)
        texto2_cor = cor_aleatoria(texto2_cor)
        texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
        texto2 = fonte.render(texto2_conteudo, True, texto2_cor)
        
        texto1_rect.x += v1x
        texto1_rect.y += v1y
        texto2_rect.x += v2x
        texto2_rect.y += v2y

   
    tela.fill(PRETO)
    tela.blit(texto1, texto1_rect)
    tela.blit(texto2, texto2_rect)
    
    clock.tick(60)
    pygame.display.flip()
   
pygame.quit()
sys.exit()