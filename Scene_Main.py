from Emoji import Emoji
from typing import List
import pygame
from pygame.locals import *
import sys
import math
from Hat import *
from INTERACTION import *
from Interaction_Handler import *


class Scene_Main():
    def __init__(self):
        pygame.init()

        self.w = 320
        self.h = 320
        self.windowSurface = pygame.display.set_mode(
            (self.w, self.h))
        self.emoji = Emoji(x=160, y=160, w = 128, h = 128)
        self.items: List[Entity] = [
            Hat(x=50, y=50, w = 128, h = 128)
        ]

        self.interaction_handler = Interaction_Handler()

    def loop(self):
        while True:
            pygame.time.Clock().tick(60)
            self.input()
            self.update()
            self.render()

    def update(self):
        self.emoji.update(self.w, self.h)
        self.emoji.update_position(self.w, self.h)

        for item in self.items:
            item.update(self.w, self.h, self.emoji)
            item.update_position(self.w, self.h)

    def render(self):
        BLACK = (0, 0, 0)
        self.windowSurface.fill(BLACK)
        self.emoji.draw(self.windowSurface)

        for item in self.items:
            item.draw(self.windowSurface)

        pygame.display.flip()

    def input(self):
        actions: List[Tuple[INTERACTION, int]] = self.interaction_handler.get()

        for interaction, speed in actions:
            if interaction is INTERACTION.BUTTON_L:
                self.items.append(Hat(x=10, y=50, w = 128, h = 128))
            elif interaction is INTERACTION.BUTTON_R:
                print("R")
            elif interaction is INTERACTION.EXIT:
                pygame.quit()
                sys.exit()
            else:
                raise NotImplementedError()
