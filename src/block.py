from contextlib import redirect_stderr
import pygame
import utl

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet=pygame.image.load('./resources/Spritesheet.png')
        self.load_sprites()
        self.sprite=self.sprites['Dirt']
    def load_sprites(self):
        self.sprites = {}
        self.sprites['Dirt'] = utl.load_sprite(self.sprite_sheet, 310, 27, 73, 73)
        self.sprites['Grass'] = utl.load_sprite(self.sprite_sheet, 237, 27, 73, 73)
        self.sprites['Stone'] = utl.load_sprite(self.sprite_sheet, 383, 27, 73, 73) 
        self.sprites['Coal'] = utl.load_sprite(self.sprite_sheet, 310, 173, 73, 73)
        self.sprites['Gold'] = utl.load_sprite(self.sprite_sheet, 456, 100, 73, 73)
        self.sprites['Redstone'] = utl.load_sprite(self.sprite_sheet, 602, 100, 73, 73)
        self.sprites['Diamond'] = utl.load_sprite(self.sprite_sheet, 529, 100, 73, 73)
        
        for state in self.sprites.keys():
            self.sprites[state] = pygame.transform.scale2x(self.sprites[state])
        
