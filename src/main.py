import pygame as pg
import constants as c
from block import *

score = 0

def init():
    pg.init()
    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    pg.display.set_caption('Dirt Clicker')
    screen.fill('white')
    print('Beginning event logging...')
    print()
    block = Block()
    screen.blit(block.sprite, (400, 300))
    font=pg.font.FONT(pg.font.get_default_font(),16)
    print('Game Start')

def main():
    init()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
            if event.type == pg.MOUSEBUTTONDOWN:
                handleclick()
                    
        pg.display.update()
    pg.quit()
    print("Window closed, game successfully quit")

def handleclick(x, y):
    if x in range(400, 546) and y in range(300, 446):
        score +=1
    

main()