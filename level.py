import pygame
from settings import *
from tile import Tile
from player import Player

class Level:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()
    def setup_level(self):
        for row_index,row in enumerate(LEVEL_MAP): 
            #get index and actual information of row
            #enumerate used to know what the index of row becasue to get the position we don't need string
            for col_index,col in enumerate(row):
                x= col_index * TILE_SIZE
                y= row_index * TILE_SIZE
                if col == 'X':
                    Tile((x,y),[self.visible_sprites]) #(x,y) = pos | [self.visible_sprites] = groups --> Tile(pos, groups)
                if col == 'P':
                    Player((x,y),[self.visible_sprites])




    def run(self): # draw them
        self.visible_sprites.draw(self.display_surface)
