import pygame
import random
#initialize

s_w = 800
s_h = 600
d_s = pygame.display.set_mode((s_w, s_h))
#icon and title
pygame.display.set_caption("abominatogus")
icon = pygame.image.load("discord.png")
pygame.display.set_icon(icon)
#background 
#background = pygame.image.load("bagground.png")
#bullet
bullet = pygame.image.load("cicle.png")
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 0.7
bullet_state = "ready"
#player
mouse = pygame.image.load("mousiee.png")
mousex = 370
mousey = 480
mousex_change = 0
mousey_change = 0


#other player
cat = pygame.image.load("cateo2.png")
catx = random.randint(0,800)
caty = random.randint(50, 150)
catx_change = 0
caty_change = 0

def player(x, y):
    d_s.blit(mouse,(x, y))


def person(x, y):
    d_s.blit(cat,(x, y))

def fokinfire(x, y):
    global bullet_state
    bullet_state = "fire"
    d_s.blit(bullet, (x+16, y+10))











#game loop
run = True
while run:
    
    d_s.fill((0, 0, 0))
    #backgrounds
    
    #d_s.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        #check keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mousex_change = -2
            if event.key == pygame.K_RIGHT:
                mousex_change = 2
            if event.key == pygame.K_UP:
                mousey_change = -2
            if event.key == pygame.K_DOWN:
                mousey_change = 2
            if event.key == pygame.K_SPACE:
                fokinfire(mousex, bullety) 
  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mousex_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                mousey_change = 0


         #check keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                catx_change = -2
            if event.key == pygame.K_d:
                catx_change = 2
            if event.key == pygame.K_w:
                caty_change = -2
            if event.key == pygame.K_s:
                caty_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                catx_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                caty_change = 0


    #other characters


    catx += catx_change
    caty += caty_change
    mousex += mousex_change
    mousey += mousey_change
#mouse
    if mousex <=0:
        mousex = 0
    elif mousex >= 768:
        mousex = 768
    if mousey <=0:
        mousey = 0
    elif mousey >= 568:
        mousey = 568
        
#cat
    if catx <=0:
        catx = 0
    elif catx >= 768:
        catx = 768
    if caty <=0:
        caty = 0
    elif caty >= 568:
        caty = 568



    #bullet
    if bullet_state is "fire":
        fokinfire(mousex, bullety)
        bullety -= bullety_change


    player(mousex, mousey)
    person(catx, caty)
    pygame.display.update()
