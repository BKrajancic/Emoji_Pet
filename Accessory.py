import pygame
import random
from Entity import *


class Accessory(Entity):

    def __init__(self, x: int, y: int, w: int, h: int, mood="cowboy"):
        Entity.__init__(self, x, y, w, h)
        self.files = {
            "cowboy": pygame.image.load("sprites/hat.png").convert_alpha(),
            "sunglasses": pygame.image.load("sprites/sunglasses.png").convert_alpha()
        }

        if(mood not in self.files):
            mood = "cowboy"

        self.mood = mood
        random.seed(10)
        self.sprite = self.files[self.mood]
        self.x.set_motion(velocity=1, acceleration=0.01)
        self.y.set_motion(velocity=1, acceleration=-1)

        self.lifeTime = -1

    def get_rect(self):
        imagerect = self.sprite.get_rect()
        imagerect.left = self.x.position
        imagerect.bottom = self.y.position
        return imagerect

    def draw(self, screen):
        imagerect = self.get_rect()
        screen.blit(self.sprite, imagerect)

    def update(self, scene_width, scene_height, emoji, scene_main):
        this_rect = self.get_rect()
        other_rect = emoji.get_rect()

        if(not self.collide and self.collide_timer > 0):
            self.collide_timer -= 1
            self.collide = (self.collide_timer == 0)

        if(self.lifeTime == 0):
            self.dead = True
        elif(self.lifeTime > 0):
            self.lifeTime -= 1

        if (this_rect.colliderect(other_rect) and self.collide):
            if(emoji.mood in emoji.cool_moods):
                scene_main.yeet_accessory("happy")

            emoji.mood = self.mood
            self.dead = True

    def update_position(self, scene_width, scene_height):
        Entity.update_position(self, scene_width, scene_height)

    def yeet(self):
        self.bounce()
        self.x.set_motion(velocity=10*random.uniform(-1, 1), acceleration=0.01)
