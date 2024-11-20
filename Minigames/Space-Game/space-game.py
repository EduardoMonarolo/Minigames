import pygame
import random
pygame.init()

x = 1280
y = 720

janela = pygame.display.set_mode((x, y))  # determinando o tamanho de tela
pygame.display.set_caption('Simple Space')  # determinando o nome do jogo

# carregando recursos
bg = pygame.image.load(r"..\Minigames\Space-Game\bg.png").convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

inimigo = pygame.image.load(r"..\Minigames\Space-Game\inimigo.png").convert_alpha()
inimigo = pygame.transform.scale(inimigo, (80, 100))

nave = pygame.image.load(r"..\Minigames\Space-Game\nave.png").convert_alpha()
nave = pygame.transform.scale(nave, (130, 130))
nave = pygame.transform.rotate(nave, -90)

missil = pygame.image.load(r"..\Minigames\Space-Game\missil.png").convert_alpha()
missil = pygame.transform.scale(missil, (50, 50))

# posições iniciais
pos_inimigo_x = 1300
pos_inimigo_y = 360

pos_nave_x = 100
pos_nave_y = 300

vel_missil_x = 0
pos_missil_x = 140
pos_missil_y = 340

vida = 2  
pontos = 0

tiro = False
janela_aberta = True

fonte = pygame.font.SysFont('Arial', 25)
fonte_game_over = pygame.font.SysFont('Arial', 60)

nave_rect = nave.get_rect()
inimigo_rect = inimigo.get_rect()
missil_rect = missil.get_rect()

# funções auxiliares
def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]

def respawn_missil():
    tiro = False
    respawn_missil_y = pos_nave_y + 40
    respawn_missil_x = pos_nave_x + 40
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y, tiro, vel_missil_x]

def colisoes():
    global pontos, vida
    if nave_rect.colliderect(inimigo_rect):
        vida -= 1
        return True
    elif missil_rect.colliderect(inimigo_rect):
        pontos += 1
        return True
    else:
        return False

def tela_derrota(score):
    janela.fill((0, 0, 0))
    texto_derrota = fonte_game_over.render("Game Over", True, (255, 0, 0))
    texto_score = fonte.render(f"Final Score: {score}", True, (255, 255, 255))
    janela.blit(texto_derrota, (x // 2 - texto_derrota.get_width() // 2, y // 2 - 100))
    janela.blit(texto_score, (x // 2 - texto_score.get_width() // 2, y // 2))
    pygame.display.update()
    pygame.time.wait(2000)

# loop principal
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            janela_aberta = False

    # checar se o jogador perdeu todas as vidas
    if vida <= 0:
        tela_derrota(pontos)
        break

    # fundo e animação
    janela.blit(bg, (0, 0))
    rel_x = x % bg.get_rect().width
    janela.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        janela.blit(bg, (rel_x, 0))

    # movimentação
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_nave_y > 1:
        pos_nave_y -= 1
        if not tiro:
            pos_missil_y -= 1
    if tecla[pygame.K_DOWN] and pos_nave_y < 665:
        pos_nave_y += 1
        if not tiro:
            pos_missil_y += 1
    if tecla[pygame.K_SPACE]:
        tiro = True
        vel_missil_x = 2

    # respawn e colisões
    if pos_inimigo_x <= 0 or colisoes():
        pos_inimigo_x, pos_inimigo_y = respawn()
    if pos_missil_x >= 1300:
        pos_missil_x, pos_missil_y, tiro, vel_missil_x = respawn_missil()

    # atualizar posições
    nave_rect.y = pos_nave_y
    nave_rect.x = pos_nave_x

    missil_rect.y = pos_missil_y
    missil_rect.x = pos_missil_x

    inimigo_rect.y = pos_inimigo_y
    inimigo_rect.x = pos_inimigo_x

    x -= 1
    pos_inimigo_x -= 1
    pos_missil_x += vel_missil_x

    # desenhar elementos
    janela.blit(inimigo, (pos_inimigo_x, pos_inimigo_y))
    janela.blit(missil, (pos_missil_x, pos_missil_y))
    janela.blit(nave, (pos_nave_x, pos_nave_y))
    pontos_text = fonte.render(f'Score: {pontos}', True, (255, 255, 255))

    janela.blit(pontos_text, (20, 20))

    pygame.display.update()

pygame.quit()
