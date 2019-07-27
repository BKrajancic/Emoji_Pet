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

        self.characters: List[Entity] = [
            Emoji(x=160, y=160),
            Hat(x=50, y=50)
        ]

        self.interaction_handler = Interaction_Handler()

    def loop(self):
        while True:
            pygame.time.Clock().tick(60)
            self.input()
            self.update()
            self.render()

    def update(self):
        for emoji in self.characters:
            emoji.update(self.w, self.h)
            emoji.update_position(self.w, self.h)

    def render(self):
        BLACK = (0, 0, 0)
        self.windowSurface.fill(BLACK)

        for emoji in self.characters:
            emoji.draw(self.windowSurface)

        pygame.display.flip()

    def input(self):
        actions: List[Tuple[INTERACTION, int]] = self.interaction_handler.get()

        for interaction, speed in actions:
            if interaction is INTERACTION.BUTTON_L:
                print("L")
            elif interaction is INTERACTION.BUTTON_R:
                print("R")
            elif interaction is INTERACTION.EXIT:
                pygame.quit()
                sys.exit()
            else:
                raise NotImplementedError()
