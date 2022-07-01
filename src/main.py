import pygame as pg
import constants as c
from block import *

score = 0

button = pygame.image.load("./resources/button.png")
button = pygame.transform.scale(button, (50, 50))

upgradeCost = 1
clickingPower = 1


def init():
    global screen, font, block, score
    pg.init()
    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
   
    pg.display.set_caption('Dirt Clicker')
    screen.fill('white')
    print('Beginning event logging...')
    print()
    block = Block()
    
    font=pg.font.Font(pg.font.get_default_font(),16)
    print('Game Start')

def main():
    init()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
            if event.type == pg.MOUSEBUTTONDOWN:
                handleclick(event.pos)
                    
        pg.display.update()
        screen.fill("white")
        screen.blit(block.sprite, (400, 300))
        screen.blit(font.render(str(score), False, "black"),(600, 350))
        screen.blit((button),(300, 330))
    pg.quit()
    print("Window closed, game successfully quit")

def handleclick(pos):
    global clickingPower, upgradeCost, score
    x, y = pos
    if x in range(400, 546) and y in range(300, 446):
        score += clickingPower
        
    if x in range(300, 300 + button.get_width()) and y in range (330, 330 + button.get_height()):
        if score >= upgradeCost: 
            clickingPower = clickingPower*2
            score-=upgradeCost
            upgradeCost = upgradeCost*6
            block.upgrade()
            
    

main()