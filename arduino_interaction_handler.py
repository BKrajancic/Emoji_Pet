from pygame.locals import *
import pygame
from INTERACTION import *
from typing import List, Tuple
import time
import grovepi


class Interaction_Handler():
    def __init__(self):
        self.buttonL_enabled = False
        self.buttonR_enabled = False
        self.rac1_enabled = False
        self.rac2_enabled = False
        self.us1_enabled = True
        self.us2_enabled = True

        if (self.buttonL_enabled):
            self.button_l = 3
            grovepi.pinMode(self.button_l, "INPUT")

        if (self.buttonR_enabled):
            self.button_r = 4
            grovepi.pinMode(self.button_r, "INPUT")

        if self.rac1_enabled or self.rac2_enabled:
            self.rac_max = 300
            self.grove_vcc = 5
            self.adc_ref = 5

        if (self.rac1_enabled):
            self.rac_1 = 0
            self.rac_1_prev = self.get_rotation(grovepi.analogRead(self.rac_1))
            grovepi.pinMode(self.rac_1, "INPUT")

        if (self.rac2_enabled):
            self.rac_2 = 1
            self.rac_2_prev = self.get_rotation(grovepi.analogRead(self.rac_2))
            grovepi.pinMode(self.rac_2, "INPUT")

        if (self.us1_enabled):
            self.us1_pin = 5
            self.us1_prev = grovepi.ultrasonicRead(self.us1_pin)

        if (self.us2_enabled):
            self.us2_pin = 6
            self.us2_prev = grovepi.ultrasonicRead(self.us2_pin)

    def get(self) -> List[Tuple[INTERACTION, int]]:
        events = pygame.event.get()
        interactions: List[Tuple[INTERACTION, int]] = []

        if (self.buttonL_enabled):
            if grovepi.digitalRead(self.button_l) == 1:
                interactions.append((INTERACTION.BUTTON_L, 0))

        if (self.buttonR_enabled):
            if grovepi.digitalRead(self.button_r) == 1:
                interactions.append((INTERACTION.BUTTON_R, 0))

        if (self.rac1_enabled):
            rac_1_rot = self.get_rotation(grovepi.analogRead(self.rac_1))
            delta = int(rac_1_rot - self.rac_1_prev)
            if (abs(delta) > 3):
                p = (INTERACTION.ROLL, delta * 3)
                interactions.append(p)
            self.rac_1_prev = rac_1_rot

        if (self.rac2_enabled):
            rac_2_rot = self.get_rotation(grovepi.analogRead(self.rac_2))
            delta = (int(rac_2_rot - self.rac_2_prev))
            if (abs(delta) > 3):
                p = (INTERACTION.ROLL, delta * 3)
                interactions.append(p)
            self.rac_2_prev = rac_2_rot

        if (self.us1_enabled):
            us1 = grovepi.ultrasonicRead(self.us1_pin)
            delta = int(self.us1_prev - us1)
            if (abs(delta) > 3):
                interactions.append((INTERACTION.ROLL, abs(delta)))

        if (self.us2_enabled):
            us2 = grovepi.ultrasonicRead(self.us2_pin)
            delta = int(self.us2_prev - us2)
            if (abs(delta) > 3):
                interactions.append((INTERACTION.ROLL, -abs(delta)))

        return interactions

    def get_rotation(self, rac_read):
        voltage = round((float)(rac_read) * self.adc_ref / 1023, 2)
        rac_deg = round((voltage * self.rac_max) / self.grove_vcc, 2)
        return rac_deg
