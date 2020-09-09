import pygame
from pygame.sprite import Sprite
 
class Basket(Sprite):
    """A class to manage the basket."""
    
    def __init__(self, cg_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Basket,self).__init__()
        self.screen=screen
        self.cg_settings=cg_settings

        #load the ship img and get its rectangle
        self.image = pygame.image.load('images/basket (1).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #store a decimal value for the ship's center
        self.center =float(self.rect.centerx)
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        '''This function says take the background surface and draw it onto the screen 
        and position it at (x,y).
        blit(background,(x,y)) '''

    def update(self):
        """update basket position based on movement flag"""
        #update the ship's center value, not the rect.
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.cg_settings.basket_speed_factor 
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.center-=self.cg_settings.basket_speed_factor  
        #update the rect object from self.center
        self.rect.centerx = self.center

    